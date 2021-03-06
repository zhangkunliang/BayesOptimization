# coding=utf-8
import time

import ThermalConductivity as TC

##############################################
# case
k = 2
# 系统尺寸(nm)
thickness = 0.018
r = 3  ###0.407#nm纳米管半径
# 系统温度(K)
System_temp = 300
# 层数
number_layers = 80  ###60
# 固定层数
number_fixed = 3  ###2
# 热浴层数
number_bath = 3  ###6
# 单位换算
timestep = 5e-7  # ns
# 热流方向 heatflux_direction=1：x方向为热流方向；heatflux_direction=2：y方向为热流方向
heatflux_direction = 1  # 热流方向

# ---------------------计算热导率从此处开始计算----------------------#
print(30 * '-', 'Done!', 30 * '-')
tc = TC.ThermalConductivity()
for i in range(1, k + 1):
    relax_data = 'PPE_NPT.data'  # './0811/TC3.0/MoS2_NPT.data'
    tc.read_size(relax_data, i, thickness, r, heatflux_direction)

    # Read temperature profile for calculating temperature gradient
    temperaturefile = str(i) + "_temp_equ_" + str(
        System_temp) + "K.dat"  # './0811/TC3.0/'+str(i)+"_temp_equ_"+str(System_temp)+"K.dat"
    tc.temp_grad(temperaturefile, number_layers, number_fixed, number_bath, fit_factor=2, Plot=True)  # False)

    # Read input and output energies for calculating heat flux

    heatfluxfile = str(i) + "_Energy_equ_" + str(
        System_temp) + "K.dat"  # './0811/TC3.0/'+str(i)+"_Ener_equ_"+str(System_temp)+"K.dat"
    tc.heat_flux(heatfluxfile, timestep)

    '''   
    TempGrad_fator=1,use fitting temperature gradient.
    TempGrad_fator=2,without including highest and lowest temperatures,namely hot and cold bath.
    TempGrad_fator=3,use directly temperature difference.
    '''
    result = 'Thermal_conductivity.txt'  # "./0811/TC3.0/Thermal_conductivity.txt"
    tc.thermal_conductivity(result, TempGrad_fator=1)

    logname = 'log.txt'  # './0811/TC3.0/log.txt'
    tc.logfile(logname)
with open('Thermal_conductivity.txt', 'r') as read_to_avg:
    readline = read_to_avg.readlines()
    with open('Thermal_conductivity.txt', 'w') as write_to_avg:
        sum = 0
        count = 0
        len_readline = len(readline)
        for line in range(0, len_readline):
            len_array = len(readline[line].strip().split())
            for i in range(0, len_array):
                sum += float(readline[line].strip().split()[i])
                count += 1
        # print(count)
        res = "%1.5f" % (sum / count)
        write_to_avg.write(res)
print('平均热导率为：',res)
print(30 * '-', 'Done!', 30 * '-')
