#coding:utf-8
import xlwt

workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(r'群组')
worksheet.write(0,0,'A1data')
worksheet.write(1,0,'A2data')
worksheet.write(2,0,'A2data')
worksheet.write(3,0,'A2data')
worksheet.write(4,0,'A2data')
workbook.save('D:\\群组在线人数统计.xls')

