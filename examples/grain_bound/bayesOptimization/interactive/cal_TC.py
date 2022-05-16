#!/usr/bin/env python
# coding=utf-8
import numpy as np
from qh_anmeng import SSH_qh
import time
import os

# final_path_data = r'E:\Study\pe-pp\Sequence_final_data'
# remote_path = '/work1/anmeng_work/zkl/PPE'
# qh = SSH_qh()
# t = qh.connect()
# sftp = t.open_sftp()
path = r'E:\Study\pe-pp\PPE\Bo_PPE_1st'
thermal_c_path = r'D:\ProgramFiles\MyProject\combo\examples\grain_bound\bayesOptimization\kl_data\thermal_c'

# thermal_c.append(1.22)
# thermal_c.append(2.23)
f = open(thermal_c_path+'/'+'TC_3st.dat', 'a+')
array_seq = os.listdir(path)
print(array_seq)
for structure_seq in array_seq:
    print(structure_seq)
    os.chdir(path + '/' + structure_seq + '/')
    # os.system('cd '+path+'/'+structure_seq+'/')
    # os.getcwd()
    os.system('python ../../Main_thermal_conductivity3.0.py')
    time.sleep(3)
    with open(path + '/' + structure_seq + '/' + 'Thermal_conductivity.txt', 'r') as read_tc:
        readline = read_tc.readline().strip()
        f.write(str(readline) + '\n')
        print('成功读取%s热导率' % structure_seq)
# with open('../kl_data/input_decriptor/input_Descriptor_3st.dat', 'r') as read_input_descriptor_dat:
#     with open('../kl_data/descriptor.dat', 'r') as read_descriptor_dat:
#         read_input_seq = read_input_descriptor_dat.readlines()
#         read_seq = read_descriptor_dat.readlines()
#         print (read_input_seq)
#         for index in read_input_seq:
#             structure_seq = str(read_seq[int(index) - 1].strip().replace(' ', ''))
#             print(structure_seq)
#             os.chdir(path+'/'+structure_seq+'/')
#             # os.system('cd '+path+'/'+structure_seq+'/')
#             # os.getcwd()
#             os.system('python ../../Main_thermal_conductivity3.0.py')
#             time.sleep(3)
#             with open(path + '/' + structure_seq + '/' + 'Thermal_conductivity.txt', 'r') as read_tc:
#                 readline = read_tc.readline().strip()
#                 f.write(str(readline)+'\n')
#                 print('成功读取%s热导率' % structure_seq)


# eox = np.loadtxt('../../TC/Thermal_conductivity.txt')
# print('eox为%s'%eox)
