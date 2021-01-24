import os
import xlwt

path = r'E:\case\case512'
list_com = os.listdir(path)
# print(type(os.listdir(path)))
# print (list_com)
list_combine = []
list_thermal_conductivity = []
list_findfive = []
for i in list_com:
    # print(i)
    # print(type(i))
    list_combine.append(i[4:])
for k in list_combine:
    if k.count("1") == 5:
        list_findfive.append(k)
for t in list_findfive:
    with open(path + '\\' +'cnb_'+t + '\\' + 'Thermal_conductivity.txt') as file:
        t = file.readline()
        list_thermal_conductivity.append(t)
        file.close()
# print(list_combine)
# print(list_thermal_conductivity)
book = xlwt.Workbook()
sheet = book.add_sheet('sheetone')
# find five wakong in the whole Cnb_test_data.
for j in range(126):
    for k in range(9):
        sheet.write(j, k, list_findfive[j][k])
for t in range(126):
    sheet.write(t, 9, list_thermal_conductivity[t])
book.save('Cnb_test_data.xls')
