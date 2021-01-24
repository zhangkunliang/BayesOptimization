import multiprocessing
import numpy as np
import scipy
import combo
import time


# time_start = time.time()
def load_data():
    # A =  np.asarray(np.loadtxt('TC_lina_A4_R12_M8.txt',skiprows=0,delimiter=' ') )
    A = np.asarray(np.loadtxt('Cnb_test_data/conductivity.csv', skiprows=0, delimiter=','))
    X = A[:, 0:9]
    t = A[:, 9]
    return X, t


def get_result(kw):
    kw = int(kw)
    # result = []
    # Load the Cnb_test_data.
    # X is the N x d dimensional matrix.
    # Each row of X denotes the d-dimensional feature vector of search candidate.
    # t is the N-dimensional vector
    X, t = load_data()
    p, q = load_data()
    # Normalize the mean and standard deviation along the each column of X to 0 and 1, respectively
    X = combo.misc.centering(X)

    # Declare the class for calling the simulator.
    # In this tutorial, we simply refer to the value of t.
    # If you want to apply combo to other problems, you have to customize this class.
    class simulator:
        def __init__(self):
            _, self.t = load_data()

        def __call__(self, action):
            return self.t[action]

    policy = combo.search.discrete.policy(test_X=X)
    # set the seed parameter
    policy.set_seed(kw)

    res = policy.random_search(max_num_probes=20, simulator=simulator())

    res = policy.bayes_search(max_num_probes=80, simulator=simulator(), score='TS', interval=20, num_rand_basis=5000)

    best_fx, best_action = res.export_all_sequence_best_fx()
    history_fx = res.fx[0:res.total_num_search]
    history_action = res.chosed_actions[0:res.total_num_search]
    fx = best_fx.tolist()
    action = best_action.tolist()
    list_p = p.tolist()
    id = []
    for i in action:
        m = int(i)
        id.append(list_p[m])
    id_str = []
    for k in id:
        kp = []
        for ki in k:
            kp.append(str(int(ki)))
        str_id = ''.join(kp)
        id_str.append(str_id)
    h_fx = history_fx.tolist()
    h_action = history_action.tolist()
    h_id = []
    for j in h_action:
        n = int(j)
        h_id.append(list_p[n])
    h_id_str = []
    for h in h_id:
        hp = []
        for hi in h:
            hp.append(str(int(hi)))
        str_h_id = ''.join(hp)
        h_id_str.append(str_h_id)
    del res
    # result.append(action)
    # result.append(id_str)
    # result.append(fx)
    # result.append(h_action)
    # result.append(h_id_str)
    # result.append(h_fx)
    result = {'action': action, 'id_str': id_str, 'fx': fx, 'h_action': h_action, 'h_id_str': h_id_str, 'h_fx': h_fx}
    return result


if __name__ == "__main__":
    npool = 1
    pool = multiprocessing.Pool(npool)
    results = []
    for i in range(npool):
        results.append(pool.apply_async(get_result, (i,)))
    pool.close()
    pool.join()

    # g = r'/home/xiao/lina/result_A4_R12_M8_max.txt'
    g = r'Cnb_test_data/test2.csv'
    id_str = []
    fx = []
    h_id_str = []
    h_fx = []
    for res in results:
        result = res.get()
        id_str.append(result['id_str'])
        fx.append(result['fx'])
        h_id_str.append(result['h_id_str'])
        h_fx.append(result['h_fx'])
    for j in range(len(fx[0])):
        m = []
        m.append(str(j + 1))
        for k in range(npool):
            m.append(id_str[k][j])
            m.append(str(fx[k][j]))
            m.append(h_id_str[k][j])
            m.append(str(h_fx[k][j]))
        b = ','.join(m)
        with open(g, 'a+') as qdata:
            qdata.write(b + '\n')
    # time_end = time.time()
    # print('time cost', time_end - time_start, 's')
