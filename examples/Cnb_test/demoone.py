import os
import xlwt
path=r'D:\Study\CNB\cnb512\cnb512\case512'
list_com=os.listdir(path)
#print(type(os.listdir(path)))
list_combine=[]
list_thermal_conductivity=[]
for i in list_com:
    #print(i)
    #print(type(i))
    list_combine.append(i[4:])
    with open(path+'\\'+i+'\\'+'Thermal_conductivity.txt') as file:
        t=file.readline()
        list_thermal_conductivity.append(t)
        file.close()
print(list_combine)
print(list_thermal_conductivity)
book=xlwt.Workbook()
sheet=book.add_sheet('sheetone')
for j in range(512):
    for k in range(9):
        sheet.write(j,k,list_combine[j][k])
for t in range(512):
    sheet.write(t,9,list_thermal_conductivity[t])
book.save('Cnb_test_data.xls')


