from __future__ import print_function

import numpy as np
import pickle as pickle
import scipy
import combo
import os
import urllib
import matplotlib.pyplot as plt

num = 0


def load_data():
    A = np.loadtxt('descriptor.dat')
    print (A.shape)
    X = A
    print (X.shape[0])
    return X


log = open('bo_log', 'w')

# Load the Cnb_test_data.
# X is the N x d dimensional matrix. Each row of X denotes the d-dimensional feature vector of search candidate. 
# t is the N-dimensional vector that represents the corresponding negative energy of search candidates. 
# ( It is of course unknown in practice. )
X = load_data()


# Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
# X = combo.misc.centering( X )

# Declare the class for calling the simulator. 
# In this tutorial, we simply refer to the value of t. 
# If you want to apply combo to other problems, you have to customize this class. 
class simulator:

    def __init__(self):
        print ('Call simulator')
        self.t = np.zeros(X.shape[0])
        # self.t =  np.loadtxt('mao_03.out')
        print ('Hello!')

    def __call__(self, action):
        global num
        num = num + 1
        print (num)
        if num <= 26:
            print(action + 1)
            structure_current = X[action, :]
            np.savetxt('input_Descriptor.dat', action + 1, fmt='%d')
            os.system('ifort -o F90_ReadThermalConductance_For_Combo.exe F90_ReadThermalConductance_For_Combo.f90')
            os.system('./F90_ReadThermalConductance_For_Combo.exe>out.f90')
            os.system('mv out.f90 ./out_' + str(num) + '.f90')
            etot = np.loadtxt('G_300_01.dat')
            os.system('mv G_300_01.dat ./G_300_01_' + str(num) + '.dat')
            self.t[action] = -etot
            log.write(str(action + 1))
            log.write('\n')
            log.flush()
            print (X[action, :])
            print (etot)
            np.savetxt('mao_03.out', self.t, fmt='%1.4f')
            return self.t[action]

        else:
            print (action + 1)
            structure_current = X[action, :]
            np.savetxt('input_Descriptor.dat', action + 1, fmt='%d')
            log.write(str(action + 1))
            log.write('\n')
            log.flush()
            print (X[action, :])
            np.savetxt('mao_03.out', self.t, fmt='%1.4f')
            return self.t[action]


# Design of policy

# Declaring the policy by 
policy = combo.search.discrete.policy(test_X=X)
# test_X is the set of candidates which is represented by numpy.array.
# Each row vector represents the feature vector of the corresponding candidate

# set the seed parameter 
policy.set_seed(10)

simulator = simulator()

''' 1st step (random sampling) '''
actions = policy.random_search(max_num_probes=1, num_search_each_probe=10, simulator=None)
t = simulator(actions)
policy.write(actions, t)
combo.search.utility.show_search_results(policy.history, 10)

''' 2st step (random sampling) '''
actions = policy.random_search(max_num_probes=1, num_search_each_probe=10, simulator=None)
t = simulator(actions)
policy.write(actions, t)
combo.search.utility.show_search_results(policy.history, 10)

''' 3rd step (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search results

predictor = policy.predictor
training = policy.training

actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10,
                              predictor=predictor, training=training,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search results

''' 4-th step (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search results

predictor = policy.predictor
training = policy.training

actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10,
                              predictor=predictor, training=training,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search results

with open('predictor.dump', 'w') as f:
    pickle.dump(policy.predictor, f)
policy.training.save('training.npz')
policy.history.save('history.npz')

''' delete policy'''
del policy

policy = combo.search.discrete.policy(test_X=X)
policy.load('history.npz', 'training.npz', 'predictor.dump')

''' 5-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 6-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 7-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 8-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 9-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 10-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 11-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 12-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 13-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 14-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 15-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 16-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 17-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 18-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 19-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 20-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 21-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 22-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 23-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 24-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

''' 25-th probe (bayesian optimization) '''
actions = policy.bayes_search(max_num_probes=1, num_search_each_probe=10, predictor=predictor,
                              simulator=None, score='EI', interval=0, num_rand_basis=0)
t = simulator(actions)  # experiment
policy.write(actions, t)  # record new observations
combo.search.utility.show_search_results(policy.history, 10)  # describe search result

# res=policy.history

# plt.plot(res.fx[0:res.total_num_search])

# plt.savefig('Cnb_test.png', dpi = 300)
