# coding=utf-8
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import csv
import os
from PIL import Image
import shutil

matplotlib.use('Agg')
path = r'/home/ubuntu/disk1/Cxq/CNN/cnn_cnb512case/case512'
file_path = r'/home/ubuntu/disk1/Cxq/CNN/cnn_cnb512case/calculate_CNB_thermal_conductivity.py'
path_tu = r'/home/ubuntu/disk1/Cxq/CNN/cnn_cnb512case/tu'


def To2(x, n):
    """
    :param x: the value you want to convert
    :param n: keep n bits
    :return: binary value
    """

    X = x
    N = n
    m = bin(X)
    m = m.lstrip('0b')
    a = []
    L = []
    if len(m) < N:
        for i in range(N - len(m)):
            a.append('0')
        a = ''.join(a)
        k = a + m
    else:
        k = m
    for j in range(len(k)):
        L.append(k[j])
    return L


def get_input(n):
    """
    :param n: the value you want to convert
    :return: all case 'cnb.Cnb_test_data'
    """

    n = int(n)
    # path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'
    a = r'\cnb.Cnb_test_data'
    a = path + a
    total = []
    part_0 = []
    part_1 = []
    part_2 = []
    part_3 = []
    part_4 = []
    part_5 = []
    part_6 = []
    part_7 = []
    part_8 = []
    part_9 = []
    part_10 = []
    b2 = []
    num = []
    with open('cnb.Cnb_test_data', 'rb') as f:
        for line in f:
            la = ''.join(str(line))
            la = la.strip()
            la = la.split(' ')
            la = list(filter(None, la))
            total.append(la)
            if len(la) == 13:
                num.append(la)
                if float(la[5]) > 19.0 and float(la[5]) < 32.0 and float(la[6]) > 6.0 and float(la[6]) < 19.0:
                    part_1.append(la)
                elif float(la[5]) > 19.0 and float(la[5]) < 32.0 and float(la[6]) > 27.0 and float(la[6]) < 41.0:
                    part_2.append(la)
                elif float(la[5]) > 19.0 and float(la[5]) < 32.0 and float(la[6]) > 50.0 and float(la[6]) < 63.0:
                    part_3.append(la)
                elif float(la[5]) > 57.0 and float(la[5]) < 70.0 and float(la[6]) > 6.0 and float(la[6]) < 19.0:
                    part_4.append(la)
                elif float(la[5]) > 57.0 and float(la[5]) < 70.0 and float(la[6]) > 27.0 and float(la[6]) < 41.0:
                    part_5.append(la)
                elif float(la[5]) > 57.0 and float(la[5]) < 70.0 and float(la[6]) > 50.0 and float(la[6]) < 63.0:
                    part_6.append(la)
                elif float(la[5]) > 95.0 and float(la[5]) < 108.0 and float(la[6]) > 6.0 and float(la[6]) < 19.0:
                    part_7.append(la)
                elif float(la[5]) > 95.0 and float(la[5]) < 108.0 and float(la[6]) > 27.0 and float(la[6]) < 41.0:
                    part_8.append(la)
                elif float(la[5]) > 95.0 and float(la[5]) < 108.0 and float(la[6]) > 50.0 and float(la[6]) < 63.0:
                    part_9.append(la)
                else:
                    part_0.append(la)
    dic = {'part_1': part_1, 'part_2': part_2, 'part_3': part_3, 'part_4': part_4, 'part_5': part_5, 'part_6': part_6,
           'part_7': part_7, 'part_8': part_8, 'part_9': part_9}
    keys = list(dic.keys())
    b2 = To2(n, 9)
    for j in range(len(b2)):
        if b2[j] == '0':
            inter_num = keys[j]
            inter_list = dic[inter_num]
            for atom in inter_list:
                if atom[3] != '1':
                    atom[3] = '1'
    d = total
    name = ''.join(b2)
    ty = r'\cnb_'
    #    path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'

    g = path + ty + name + '\\' + 'cnb.Cnb_test_data'

    for k in d:
        b = ' '.join(k)
        b1 = b.lstrip("b'")  # 截掉字符串左边的空格或指定字符
        b2 = b1.strip("\\r\\n'")  # 返回移除字符串头尾指定的字符生成的新字符串
        with open(g, 'a+') as edata:
            edata.write(b2 + '\n')


def main():
    for i in range(3):
        series = ''.join(To2(i, 9))
        num = series.count('0')
        if num < 10:
            get_input(i)


def mkdir():
    """
    create all case 'cnb.Cnb_test_data' folders
    """

    # path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'
    for i in range(3):
        series = ''.join(To2(i, 9))  # 将序列中的元素以指定的字符连接生成一个新的字符串
        num = series.count('0')
        if num < 10:
            p = path + '\\cnb_' + series
            os.mkdir(p)


def cp_calculate_th():
    """
    copy 'calculate_CNB_thermal_conductivity.py' to all case folders
    """

    ty = r'/cnb_'
    #    path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'
    #    file_path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv\calculate_CNB_thermal_conductivity.py'
    for i in range(512):
        name = ''.join(To2(i, 9))
        g = path + ty + name
        shutil.copy(file_path, g)
        print('%s' % g)
    # mkdir()


# main()


def writexy():
    """
    write all atoms xyz to csv file
    """

    ty = r'/cnb_'
    # path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'

    for i in range(512):
        name = ''.join(To2(i, 9))
        g = path + ty + name + '/cnb.Cnb_test_data'

        with open(g, mode='rt', encoding='utf8') as f:
            reader = csv.reader(f)
            f1 = open(path + ty + name + '/' + 'x1.csv', 'a')
            f2 = open(path + ty + name + '/' + 'y1.csv', 'a')
            f3 = open(path + ty + name + '/' + 'x2.csv', 'a')
            f4 = open(path + ty + name + '/' + 'y2.csv', 'a')
            f5 = open(path + ty + name + '/' + 'x3.csv', 'a')
            f6 = open(path + ty + name + '/' + 'y3.csv', 'a')
            for item in reader:
                la = ''.join(str(item))
                la = la.strip()
                la = la.split(' ')
                la = list(filter(None, la))
                if len(la) == 13:
                    if '1' in la[3]:
                        x1 = la[5]
                        f1.write(x1)
                        f1.write('\n')
                        f1.close
                        y1 = la[6]
                        f2.write(y1)
                        f2.write('\n')
                        f2.close
                    elif '2' in la[3]:
                        x2 = la[5]
                        f3.write(x2)
                        f3.write('\n')
                        f3.close
                        y2 = la[6]
                        f4.write(y2)
                        f4.write('\n')
                        f4.close
                    elif '3' in la[3]:
                        x3 = la[5]
                        f5.write(x3)
                        f5.write('\n')
                        f5.close
                        y3 = la[6]
                        f6.write(y3)
                        f6.write('\n')
                        f6.close


# writexy()


def mkdir_tu(filename):
    """
    through thermal.txt create folders
    """

    #    path_tu = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv\tu'
    with open(filename) as filtu:
        for line in filtu:
            line = line.strip()
            p = path_tu + '/' + line
            os.mkdir(p)


# mkdir_tu('thermal.txt')


def plot(filename):
    """
    draw the atoms picture
    """

    ty = r'/cnb_'
    #    path = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv'
    #    pathtu = r'D:\Program Files\JetBrains\namidai\cnb_wenjian_huatu_redaolv\tu'
    pathtu = path_tu
    with open(filename) as filtu:
        tu_path = []
        for line in filtu:
            line = line.strip()
            tu_path.append(line)
    for i in range(512):
        name = ''.join(To2(i, 9))
        if name == '000000000':
            x1 = pd.read_csv(path + ty + name + '/' + 'x1.csv')
            y1 = pd.read_csv(path + ty + name + '/' + 'y1.csv')
        else:
            x1 = pd.read_csv(path + ty + name + '/' + 'x1.csv')
            y1 = pd.read_csv(path + ty + name + '/' + 'y1.csv')
            x2 = pd.read_csv(path + ty + name + '/' + 'x2.csv')
            y2 = pd.read_csv(path + ty + name + '/' + 'y2.csv')
            x3 = pd.read_csv(path + ty + name + '/' + 'x3.csv')
            y3 = pd.read_csv(path + ty + name + '/' + 'y3.csv')

        plt.cla()
        if name == '000000000':
            plt.scatter(x1, y1, s=15, cmap=plt.cm.gray)
            plt.axis('off')
            plt.rcParams['figure.figsize'] = (5.4, 5.0)
            # plt.rcParams['savefig.dpi'] = 100
            plt.savefig(path + ty + name + '/' + 'c.png')
            # plt.savefig(pathtu + '\\' + tu_path[i] + '\\' + 'cc.png')
            plt.close
            size_m = 150
            size_n = 100
            image = Image.open(path + ty + name + '/' + 'c.png')
            image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
            image_size.save(pathtu + '/' + tu_path[i] + '/' + tu_path[i] + '.png')
            # image_size.save('/home/ubuntu/disk1/Cxq/CNN/cnn_cnb512case/images' + '/' + tu_path[i] + '.png')
        else:
            plt.scatter(x1, y1, s=15, cmap=plt.cm.gray)
            plt.scatter(x2, y2, s=15, cmap=plt.cm.gray)
            plt.scatter(x3, y3, s=15, cmap=plt.cm.gray)
            plt.axis('off')
            plt.rcParams['figure.figsize'] = (5.4, 5.0)
            # plt.rcParams['savefig.dpi'] = 100
            plt.savefig(path + ty + name + '/' + 'c.png')
            # plt.savefig(pathtu + '\\' + tu_path[i] + '\\' + tu_path[i] + '.png')
            plt.close
            size_m = 150
            size_n = 100
            image = Image.open(path + ty + name + '/' + 'c.png')
            image_size = image.resize((size_m, size_n), Image.ANTIALIAS)
            image_size.save(pathtu + '/' + tu_path[i] + '/' + tu_path[i] + '.png')
            # image_size.save('/home/ubuntu/disk1/Cxq/CNN/cnn_cnb512case/images' + '/' + tu_path[i] + '.png')


# mkdir()
# main()
# cp_calculate_th()
# writexy()
mkdir_tu('thermal.txt')
plot('thermal.txt')
