import pandas as pd
import xlwt

data = pd.read_excel("demo.xlsx", header=0, sheet_name=0)
book=xlwt.Workbook()
book.add_sheet("sheet2")
# print Cnb_test_data
data_ = data[(data["type"] == 2) & (data["Z"] > 11.7)]
#print data_
for i in data_["a"]:
    data = data.drop([i - 1])
    data = data.drop([i])
    data = data.drop([i + 1])
#print Cnb_test_data
data.to_excel("1.xlsx", sheet_name='sheet2')
# for i in X.index:
#     # print i
#     print(X[i, :])
#     # if X[i,2] == 2 and X[i,5] > 11.9:
