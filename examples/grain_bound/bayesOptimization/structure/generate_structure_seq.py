# -*-coding:utf-8-*-
import os

final_path_data = r'E:\Study\pe-pp\Sequence_final_data'
with open('descriptor.dat', 'w') as write_dat:
    for file in os.listdir(final_path_data):
        file_array = list(file)
        for i in file_array:
            write_dat.write(i+' ')
        write_dat.write('\n')
    write_dat.close()