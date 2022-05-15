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
    A = np.loadtxt('../test_data/descriptor.dat')
    print('A.shape为：')
    print(A.shape)  # (1024L,11L)
    X = A
    print('X.shape[0]为：')
    print(X.shape[0])  # 1024
    return X


X = load_data()
action = [21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40]
# data = np.zeros(X.shape[0])
data = np.loadtxt('../test_data/kl.out')
np.savetxt('../test_data/input_Descriptor_2st.dat', action , fmt='%d')  # 将结构序列号存储到input_Descriptor.dat文件中
# 将热导率值复制给填充数组,self.t[action]表示self.t这个全为0的列的action的部分将其替换成其它数字
# data[action] = [1, 2, 3, 2, 2, 2, 2, 2, 2, 2, 4, 4, 3, 2, 6, 2, 5, 7, 8, 2]
# print(data[action])  # [1. 2. 3. 2. 2. 2. 2. 2. 2. 2.] 以列的形式
# print(data[action].shape)  # (10L,)
# print(data)  # [0. 0. ...0.] (65536L,)
# print(data.shape)
# print('X[action, :]为：')
# print(X[action, :])
np.savetxt('../test_data/kl.out', data, fmt='%1.5f')  # 将self.t[action]记录的热导率值存入
