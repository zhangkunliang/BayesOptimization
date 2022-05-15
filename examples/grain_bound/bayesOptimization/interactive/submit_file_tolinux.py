#!/usr/bin/env python
# coding=utf-8
from qh_anmeng import SSH_qh
import time

final_path_data = r'E:\Study\pe-pp\Sequence_final_data'
remote_path = '/work1/anmeng_work/zkl'
qh = SSH_qh()
t = qh.connect()
sftp = t.open_sftp()
num_sequence = ['12463', '52063', '8534', '45053', '64247', '12660', '9845', '33560', '23976', '20498']
with open('descriptor.dat', 'r') as read_descriptor_dat:
    read_seq = read_descriptor_dat.readlines()
    len_num_sequence = len(num_sequence)
    # print (read_seq)
    for i in range(0, len_num_sequence):
        structure_seq = str(read_seq[int(num_sequence[i]) - 1].strip().replace(' ', ''))
        print(structure_seq)
        sftp.mkdir(remote_path + '/' + 'random_2st_20' + '/' + structure_seq)
        sftp.put(final_path_data + '/' + structure_seq + '/' + structure_seq + '.data',
                 remote_path + '/' + 'random_2st_20' + '/' + structure_seq + '/' + structure_seq + '.data')
        sftp.put(final_path_data + '/' + structure_seq + '/' + 'TC.in',
                 remote_path + '/' + 'random_2st_20' + '/' + structure_seq + '/' + 'TC.in')
        time.sleep(2)
