#!/usr/bin/env python
# coding=utf-8
from qh_anmeng import SSH_qh
import time

# final_path_data = r'E:\Study\pe-pp\Sequence_final_data'
# remote_path = '/work1/anmeng_work/zkl/'
# qh = SSH_qh()
# t = qh.connect()
# sftp = t.open_sftp()

with open('../kl_data/input_decriptor/input_Descriptor_4st.dat', 'r') as read_input_descriptor_dat:
    with open('../kl_data/descriptor.dat', 'r') as read_descriptor_dat:
        read_input_seq = read_input_descriptor_dat.readlines()
        read_seq = read_descriptor_dat.readlines()
        # print (read_seq)
        for index in read_input_seq:
            structure_seq = str(read_seq[int(index) - 1].strip().replace(' ', ''))
            print(structure_seq)

