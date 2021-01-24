import os
import xlwt

path = r'E:\case\classify'
list_com = os.listdir(path)
book = xlwt.Workbook()
sheet = book.add_sheet('sheetone')

w=0
for i in list_com:
    list_soncom = os.listdir(path + "\\" + i)
    list_res = []
    for j in list_soncom:
        list_split = j.split('.png')[0]
        list_res.append(list_split)
        # print (len(list_res))
        # print list_res
        #print (list_res[0])
    for k in range(len(list_res)):
        #print (list_res[k])
        sheet.write(w, k,list_res[k])
    w=w+1
book.save('data2.xls')


#
#
# # print(list_combine)
# # print(list_thermal_conductivity)

# find five wakong in the whole Cnb_test_data.

# for j in range(126):
#     for k in range(9):
#         sheet.write(j, k, list_findfive[j][k])
# for t in range(126):
#     sheet.write(t, 9, list_thermal_conductivity[t])

