# -*-coding:utf-8-*-
import os
import time

remote_path = '/work1/anmeng_work/zkl'

# 提交随机序列的...
f = open('input_Descriptor_3st.dat', 'r')
readline = f.readlines()
len_num_sequence = len(readline)

read_descriptor_dat = open('descriptor.dat', 'r')
read_seq = read_descriptor_dat.readlines()

i = 0
while i < len_num_sequence:
    index = i
    # 每次提交两个任务
    while i < index + 2:
        structure_seq = str(read_seq[int(readline[i].strip()) - 1].strip().replace(' ', ''))
        print(structure_seq)
        os.chdir(remote_path + '/' + 'Bo_PPE_1st')
        os.mkdir(structure_seq)
        os.chdir(remote_path + '/' + 'Bo_PPE_1st' + '/' + structure_seq)
        os.system('cp ../../Sequence_final_data/' + structure_seq + '/*' + ' ' + './')
        os.system(
            'bsub -a intelmpi -e error.txt -o output.txt -J ' + structure_seq +
            ' -i TC.in -n 24 mpirun.lsf /home/anmeng/WORK1/lammps-3Mar20/src/lmp_mpi')
        time.sleep(2)
        i += 1
    time.sleep(7200)

# os.system("gnome-terminal -e 'bash -c \"ls; exec bash\"'")
