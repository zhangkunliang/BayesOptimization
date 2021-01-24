import numpy as np
import pickle as pickle
import scipy
import combo
import os
import urllib


def download():
    if not os.path.exists('../Cnb_test_data/s5-210.csv'):

        if not os.path.exists('../Cnb_test_data'):
            os.mkdir('../Cnb_test_data')

        print('Downloading...')
        urllib.urlretrieve('http://www.tsudalab.org/files/s5-210.csv', '../Cnb_test_data/s5-210.csv')
        print('Done')


def load_data():
    download()
    A = np.asarray(np.loadtxt('Cnb_test_data/s5-210.csv', skiprows=1, delimiter=','))
    X = A[:, 0:3]
    t = -A[:, 3]
    return X, t


X, t = load_data()
X = combo.misc.centering(X)


class simulator:
    def __init__(self):
        _, self.t = load_data()

    def __call__(self, action):
        return self.t[action]


policy = combo.search.discrete.policy(test_X=X)
policy.set_seed(0)
res = policy.random_search(max_num_probes=20, simulator=simulator())
res = policy.bayes_search(max_num_probes=80, simulator=simulator(), score='TS',
                          interval=20, num_rand_basis=5000)
print ('f(x)=')
print(res.fx[0:res.total_num_search])
best_fx, best_action = res.export_all_sequence_best_fx()
print('current best')
print (best_fx)
print ('current best action=')
print(best_action)
print ('history of chosed actions=')
print(res.chosed_actions[0:res.total_num_search])

res.save('Cnb_test.npz')

del res

res = combo.search.discrete.results.history()
res.load('Cnb_test.npz')
