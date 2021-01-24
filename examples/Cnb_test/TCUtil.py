# -*- coding: UTF-8 -*-
import xlrd
from xlutils.copy import copy as xl_copy

path = r'/examples/1.xlsx'
bookname = r"D:\ProgramFiles\MyProject\combo\examples\grain_bound\data\1.xlsx"
sheetname = "Sheet1"


class test:
    def read_excel(self,bookname, sheetname):
        # 打开Excel文件
        wb = xlrd.open_workbook(bookname)
        sheet = wb.sheet_by_name(sheetname)
        dic={}
        for i in range(sheet.nrows - 1):
            lis = []
            for j in range(sheet.ncols):
                lis.append(sheet.cell(i + 1, j).value)
            dic[sheet.cell(i + 1, 0).value] = lis
        return dic

    # def remove_order(self, num, dic4, dic2):
    def remove_order(self, dic):
        #dic = self.read_excel()
        flag = False
        sum = 0
        for i in dic.keys():
            if dic[i][2] == 2 and dic[i][5] > 11.7:# 判定指定属性，确定删除行
                sum += 1
                dic.pop(i)
                dic.pop(i + 1)
                dic.pop(i + 2)
                self.updateExcle(dic, path, 'Sheet1', sum)
                flag = True
                break
        return flag

    def updateExcle(self, dic, bookname, sheetname, sum=0):
        wb = xlrd.open_workbook(bookname)
        sheet = wb.sheet_by_name(sheetname)
        new_wb = xl_copy(wb)  # 将原有的Excel，拷贝一个新的副本
        new_sheet = new_wb.get_sheet(0)
        m = 0
        for i in dic.keys():
            m += 1
            n = 0
            for j in dic[i]:
                new_sheet.write(m, n, j)
                n += 1
        # for h in range(m + 1, m + 1 + sum):
        #     m += 1
        #     n = 0
        #     for k in dic[i]:
        #         new_sheet.write(m, n, '')
        #         n += 1
        new_wb.save("new.xls")

t = test()
#t.read_excel(bookname, sheetname)
# #print dic
for i in range(100):
    t.remove_order(t.read_excel(bookname, sheetname))
    print i
