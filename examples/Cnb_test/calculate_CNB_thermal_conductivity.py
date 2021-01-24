import matplotlib.pyplot as plt
import numpy as np


# ------------------定义一个函数计算温度梯度--------------------#
def temp_grad(filename1, filename2):
    # filename1:原文件名，filename2：处理后要保存的文件名
    with open(filename1) as temp_11, \
            open(filename2, "w") as temp_12:
        # temp1=temp_11.read()
        # print(type(temp_11),type(temp1))
        for index, line in enumerate(temp_11, 1):
            # print(index)
            if index >= 6 and index <= 202:
                for line in temp_11:
                    temp_gradient = line.strip().split()
                    # print(temp_gradient)
                    coord = float(temp_gradient[0])  # x(nm)
                    coord1 = round(coord * (12.636 / 60), 4)
                    temperature = round(float(temp_gradient[3]), 4)  # T(K)
                    # print(coord,temperature)
                    temp_12.write(str(coord))
                    temp_12.write(" ")
                    temp_12.write(str(coord1))
                    temp_12.write(" ")
                    temp_12.write(str(temperature))
                    temp_12.write("\n")
    return


# temp_grad("2_temp_equ_300K.dat","2_temp_equ_300K.txt")


# ----------------------另一种温度梯度计算方法   L/温差------------------------#

# 定义另一种求温度梯度的方法
def L_T(filename):
    L = 12.636 - 12.636 / 60 * 12  # nm
    # wentidu=0.0
    global wentidu
    with open(filename)as wendu:
        for line in wendu:
            L_line = line.strip().split()
            if float(L_line[0]) == 7.0:
                print(L_line[2])
                hight_temp = float(L_line[2])  # K
            elif float(L_line[0]) == 54.0:
                print(L_line[2])
                low_temp = float(L_line[2])  # K
        # else:
        # 	print(1)
        wentidu = (hight_temp - low_temp) / L
        print(wentidu)
    return


# -----------------------定义一个计算热流的函数-------------------------#
def heat_flux(filename1, filename2):
    with open(filename1) as ener_1, \
            open(filename2, "w") as Q:
        timestep = 5e-7  # ns
        J2ev = 1.602763e-19  # ev转换为J
        for index, line in enumerate(ener_1):
            for line in ener_1:
                ener_11 = line.split()
                # print(ener_11[1],ener_11[2])
                # 将步数转换为时间ns
                Time = float(ener_11[0]) * timestep
                # 将能量平均并将ev转换为为J
                Energy = 0.5 * (float(ener_11[2]) - float(ener_11[1])) * J2ev
                # print(Energy)
                # 将时间与热流写入文件
                Q.write(str(ener_11[0]))
                Q.write(" ")
                Q.write(str(Time))
                Q.write(" ")
                Q.write(str(Energy))
                Q.write("\n")
        ener_1.close()
        Q.close()
    return


# heat_flux("2_Ener_equ_300K.dat","2_Ener_equ_300K.txt")

# ----------------------定义一个画温度分布的函数------------------------#
def plot_temp(filename2):
    # 绘制温度分布并拟合。
    temp_12 = open(filename2, "r")
    # print(temp_12.read())
    xmin = 2  # nm
    xmax = 10  # nm
    x1 = list()
    y1 = list()  # 全部
    x2 = list()
    y2 = list()  # 拟合
    for lines in temp_12:
        temp_gradient1 = lines.split()
        temp_gradient = list(map(eval, temp_gradient1))
        # print(temp_gradient)
        b = [1.0, 2.0, 3.0, 58.0, 59.0, 60.0]
        if temp_gradient[0] not in b:

            x1.append(temp_gradient[1])
            y1.append(temp_gradient[2])

            if float(temp_gradient[1]) >= xmin and float(temp_gradient[1]) <= xmax:
                x2.append(temp_gradient[1])
                y2.append(temp_gradient[2])
            # print(type(temp_gradient[1]))
    fit = np.polyfit(x2, y2, 1)  # 用1次多项式拟合
    fit_fn = np.poly1d(fit)
    print("拟合公式:", fit_fn)  # 拟合多项式
    print("斜率-温度梯度:", fit[0], "(K/nm)", "\n" + "截距:", fit[1], "(K)", "\n")
    global Temperature_gradient
    Temperature_gradient = fit[0]
    # -------坐标图
    # plt.scatter(x1,y1)
    # plt.plot(x2,fit_fn(x2),"r-",linewidth=4.0)
    # plt.title("Temperature profile")
    # plt.xlabel("Distance (nm)")
    # plt.ylabel("Temperature (K)")
    # plt.savefig(str(i)+"Temperature profile.png")
    # plt.show()
    # plt.close()
    return


# temp_grad("2_temp_equ_300K.dat","2_temp_equ_300K.txt")
# plot_temp("2_temp_equ_300K.txt")

# -----------------------定义一个画热流的函数----------------------#
def plot_heatflux(filename2):
    with open(filename2) as Q:
        xmin = 0.1  # ns
        xmax = 4.9  # ns
        x1 = list()
        y1 = list()  # 全部
        x2 = list()
        y2 = list()  # 拟合
        for lines in Q:
            Q_t = list(map(eval, lines.split()))
            x1.append(Q_t[1])
            y1.append(Q_t[2])
            # 拟合
            if float(Q_t[1]) >= xmin and float(Q_t[1]) <= xmax:
                x2.append(Q_t[1])
                y2.append(Q_t[2])
    fit = np.polyfit(x2, y2, 1)  # 用1次多项式拟合
    fit_fn1 = np.poly1d(fit)
    print("拟合公式：", fit_fn1)
    print("热流为：", fit[0], "(J/ns)")
    print("截距为：", fit[1], "(J)\n")
    global Heat_flux
    Heat_flux = fit[0]
    # -------坐标图
    # plt.plot(x1,y1,"o",linewidth=9.0)
    # plt.plot(x2,fit_fn1(x2),"r-",linewidth=3.0)
    # plt.title("Heat flux (J/ns)")
    # plt.xlabel("Time (ns)")
    # plt.ylabel("Energy (J)")
    # plt.savefig(str(i)+"Heat flux.png")
    # plt.show()
    # plt.close()
    return Heat_flux


# temp_grad("2_temp_equ_300K.dat","2_temp_equ_300K.txt")
# plot_temp("2_temp_equ_300K.txt")

# heat_flux("2_Ener_equ_300K.dat","2_Ener_equ_300K.txt")
# plot_heatflux("2_Ener_equ_300K.txt")

# #----------------------定义一个计算热导率的函数---------------------#
# def Thermal_conductivity(filename3):
# #filename3为你要存储热导率的文件名
# 	with open(filename3,"a+") as tc_k:
# 		A=2.85e-18#(m2)
# 		# def TC(Heat_flux,Temperature_gradient,A=2.85e-18):
# 		k=-Heat_flux/(A*Temperature_gradient)
# 		print('热导率值为:'+str(round(k,4)),'W/m-K\n')#round(要输出的值,保留几位小数)
# 		tc_k.write(str(round(k,4)))
# 		if i == 3:
# 			tc_k.write('\n')
# 		else:
# 			tc_k.write(' ')


# ----------------------定义一个计算热导率的函数---------------------#
def Thermal_conductivity(filename3):
    # filename3为你要存储热导率的文件名
    with open(filename3, "a+") as tc_k:
        A = 6.8096 * 0.35e-18  # 2.85e-18#(m2)
        # def TC(Heat_flux,Temperature_gradient,A=2.85e-18):
        # k=-Heat_flux/(A*Temperature_gradient)
        # 另一种温度梯度计算方法
        k = Heat_flux / (A * wentidu)
        print('热导率值为:' + str(round(k, 4)), 'W/m-K\n')  # round(要输出的值,保留几位小数)
        tc_k.write(str(round(k, 4)))
        if i == 3:
            tc_k.write('\n')
        else:
            tc_k.write(' ')


# ---------------------计算热导率从此处开始计算----------------------#
for i in range(1):
    if i == 0:
        temp_grad("1_temp_equ_300K.dat", "1_temp_equ_300K.txt")
        plot_temp("1_temp_equ_300K.txt")
        heat_flux("1_Ener_equ_300K.dat", "1_Ener_equ_300K.txt")
        plot_heatflux("1_Ener_equ_300K.txt")
        L_T("1_temp_equ_300K.txt")
        Thermal_conductivity("Thermal_conductivity.txt")
    elif i == 2:
        temp_grad("2_temp_equ_300K.dat", "2_temp_equ_300K.txt")
        plot_temp("2_temp_equ_300K.txt")
        heat_flux("2_Ener_equ_300K.dat", "2_Ener_equ_300K.txt")
        plot_heatflux("2_Ener_equ_300K.txt")
        L_T("2_temp_equ_300K.txt")
        Thermal_conductivity("Thermal_conductivity.txt")
    else:
        temp_grad("3_temp_equ_300K.dat", "3_temp_equ_300K.txt")
        plot_temp("3_temp_equ_300K.txt")
        heat_flux("3_Ener_equ_300K.dat", "3_Ener_equ_300K.txt")
        plot_heatflux("3_Ener_equ_300K.txt")
        L_T("3_temp_equ_300K.txt")
        Thermal_conductivity("Thermal_conductivity.txt")
