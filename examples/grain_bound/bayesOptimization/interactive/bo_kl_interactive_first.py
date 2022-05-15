#!/usr/bin/env python
# coding=utf-8
from __future__ import print_function

import numpy as np
import pickle as pickle
import scipy
import combo
import time

num = 0


def load_data():
    A = np.loadtxt('../kl_data/descriptor.dat')
    print('A.shape为：')
    print(A.shape)
    X = A
    print('X.shape[0]为：')
    print(X.shape[0])  # 1024
    return X


log = open('../kl_data/log/bo_log', 'w')
time_log = open('../kl_data/log/time_log', 'w')

X = load_data()  # (运行顺序-1)
print('...')


class simulator:

    def __init__(self):  # (运行顺序-3)
        print('Call simulator')
        # self.t = np.zeros(X.shape[0])  # X.shape[0]为总结构的行数，返回给定形状和类型填充数为0的数组,[0,0,...]列，运行一次即可
        self.t = np.loadtxt('../kl_data/out/kl.out')
        # print(self.t)
        print('Hello!')

    # __call__函数：使类实例对象可以像调用普通函数那样，以”对象名()“的形式使用，(self,代表创建的类实例本身)
    def __call__(self, action):
        global num
        num = num + 1
        print(num)
        if num <= 26:  # 后面贝叶斯训练的次数
            print('action + 1为：')
            print(action + 1)  # 初始随机选取的十个结构的索引号，预测的序列号索引是从0开始的，故+1,传入的action是一个数组
            # print(num)
            structure_current = X[action, :]
            np.savetxt('../kl_data/input_decriptor/input_Descriptor_'+str(num)+'st.dat', action + 1,
                       fmt='%d')  # 将结构序列号存储到input_Descriptor.dat文件中,覆盖式修改、保存
            # 将热导率值复制给填充数组,self.t[action]表示self.t这个全为0的列的action的部分将其替换成其它数字
            # self.t[action] = [1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 2, 6, 2, 5, 7, 8, 2]
            self.t[action] = np.loadtxt('../kl_data/thermal_c/TC_2st.dat')
            print(self.t[action])  # [1. 2. 3. 2. 2. 2. 2. 2. 2. 2.] 以列的形式
            print(self.t[action].shape)  # (10L,)
            print(self.t)  # [0. 0. ...0.] (65536L,)
            print(self.t.shape)
            # 此行后为else的重复代码
            log.write(str(action + 1))
            log.write('\n')
            log.flush()
            print('X[action, :]为：')
            print(X[action, :])
            np.savetxt('../kl_data/out/kl.out', self.t, fmt='%1.5f')  # 将self.t[action]记录的热导率值存入
            return self.t[action]  # 返回批量热导率值
        else:
            print(action + 1)
            structure_current = X[action, :]
            np.savetxt('../kl_data/input_decriptor/input_Descriptor_'+str(num)+'st.dat', action + 1,
                       fmt='%d')  # 将结构序列号存储到input_Descriptor.dat文件中
            # 此行后为else的重复代码
            log.write(str(action + 1))
            log.write('\n')
            log.flush()
            print('X[action, :]为：')
            print(X[action, :])
            np.savetxt('../kl_data/out/kl_'+str(num)+'.out', self.t, fmt='%1.5f')  # 在原out文件基础上修改、存入数据
            return self.t[action]  # 返回下一个需要计算的结构的索引号


policy = combo.search.discrete.policy(test_X=X)

# set the seed parameter
policy.set_seed(10)

simulator = simulator()  # (运行顺序-2)

''' 1st step (random sampling) '''
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
start_time = time.time()
actions = policy.random_search(max_num_probes=1, num_search_each_probe=20, simulator=None)  # 搜索一次，每次搜索10个结构
t = simulator(actions)  # (运行顺序-4)  t表示调用simulator函数后得到的下一个需要计算的结构的索引号值，运行十次
policy.write(actions, t)  # t代表selt.t[action]这一列热导率的值
# print('policy=', policy)
combo.search.utility.show_search_results(policy.history, 20)
current_time = time.time()
print('1st step (random sampling)用时：' + str(current_time - start_time) + "s")
time_log.write(str(current_time - start_time))
time_log.write('\n')
print('------------------------------------')
''' 2st step (random sampling) '''
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
start_time = time.time()
actions = policy.random_search(max_num_probes=1, num_search_each_probe=20, simulator=None)
t = simulator(actions)
policy.write(actions, t)
combo.search.utility.show_search_results(policy.history, 20)
current_time = time.time()
print('2st step (random sampling)用时：' + str(current_time - start_time) + "s")
time_log.write(str(current_time - start_time))
time_log.write('\n')
print(' ''随机搜索结束'' ')
print('------------------------------------')
''' 3rd step (bayesian optimization) '''
print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
start_time = time.time()
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 20)  # describe search results
current_time = time.time()
print('''3st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
time_log.write(str(current_time - start_time))
time_log.write('\n')
print('''0003-th EI贝叶斯优化结束''')
print('------------------------------------')

predictor = policy.predictor
training = policy.training
#
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start_time = time.time()
# actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20,
#                               predictor=predictor, training=training,
#                               simulator=None, score='EI', interval=0, num_rand_basis=0)
# t = simulator(actions)  # experiment
# policy.write(actions, t)  # record new observations
# combo.search.utility.show_search_results(policy.history, 20)  # describe search results
# current_time = time.time()
# print('''4st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
# time_log.write(str(current_time - start_time))
# time_log.write('\n')
# print(' ''0004-th EI贝叶斯优化结束'' ')
# print('------------------------------------')
#
# ''' 4-th step (bayesian optimization) '''
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start_time = time.time()
# actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20,
#                               simulator=None, score='EI', interval=0, num_rand_basis=0)
# t = simulator(actions)  # experiment
# policy.write(actions, t)  # record new observations
# combo.search.utility.show_search_results(policy.history, 20)  # describe search results
# current_time = time.time()
# print('''5st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
# time_log.write(str(current_time - start_time))
# time_log.write('\n')
# print('''0005-th EI贝叶斯优化结束''')
# print('------------------------------------')

# predictor = policy.predictor
# training = policy.training
#
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start_time = time.time()
# actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20,
#                               predictor=predictor, training=training,
#                               simulator=None, score='EI', interval=0, num_rand_basis=0)
# t = simulator(actions)  # experiment
# policy.write(actions, t)  # record new observations
# combo.search.utility.show_search_results(policy.history, 20)  # describe search results
# current_time = time.time()
# print('''6st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
# time_log.write(str(current_time - start_time))
# time_log.write('\n')
# print('''0006-th EI贝叶斯优化结束''')
# print('------------------------------------')
#
# with open('predictor.dump', 'w') as f:
#     pickle.dump(policy.predictor, f)
# policy.training.save('training.npz')
# policy.history.save('history.npz')
#
# ''' delete policy'''
# del policy
#
# policy = combo.search.discrete.policy(test_X=X)
# policy.load('history.npz', 'training.npz', 'predictor.dump')
#
# ''' 5-th probe (bayesian optimization) '''
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start_time = time.time()
# actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20, predictor=predictor,
#                               simulator=None, score='EI', interval=0, num_rand_basis=0)
# t = simulator(actions)  # experiment
# policy.write(actions, t)  # record new observations
# combo.search.utility.show_search_results(policy.history, 20)  # describe search result
# current_time = time.time()
# print('''7st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
# time_log.write(str(current_time - start_time))
# time_log.write('\n')
# print('''0007-th EI贝叶斯优化结束''')
# print('------------------------------------')
#
# ''' 6-th probe (bayesian optimization) '''
# print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
# start_time = time.time()
# actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=20, predictor=predictor,
#                               simulator=None, score='EI', interval=0, num_rand_basis=0)
# t = simulator(actions)  # experiment
# policy.write(actions, t)  # record new observations
# combo.search.utility.show_search_results(policy.history, 20)  # describe search result
# current_time = time.time()
# print('''8st step (bayesian optimization)用时：''' + str(current_time - start_time) + "s")
# time_log.write(str(current_time - start_time))
# time_log.write('\n')
# print('''0008-th EI贝叶斯优化结束''')
# print('------------------------------------')


# 最多探索25次就结果就达到收敛，分开写达到交互式提交的目的，分开运行simulator()，需要一步步自己输入
# res=policy.history

# plt.plot(res.fx[0:res.total_num_search])

# plt.savefig('Cnb_test.png', dpi = 300)
