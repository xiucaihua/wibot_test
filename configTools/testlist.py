list = ["a",2,3,4]
dict = {"a":1,"b":2}

# for k,v in dict.items():
#     print(k,v)

# for index,item in enumerate(list):
#     print(index)
#     print(item)
#
#
# for index,value in enumerate(['apple', 'oppo', 'vivo']):
#         print(index,value)


# 导入相关模块
import xlrd
from xlutils import copy

# 1、使用xlrd打开Excel
workbook = xlrd.open_workbook("D://群组在线人数统计1.xls")
# 2、使用xlutils模块的copy复制打开的文件，并保留原格式
open_mb_file_cp = copy.copy(workbook)
# 3、使用下标定位的方式定位到Excel工作簿里的工作表
sheet_name = open_mb_file_cp.get_sheet(r"12月份腾信国际物流")
# 4、向表格写入新的数据
sheet_name.write(0,0,'新数据写入')
# 5、保存已改后的数据
open_mb_file_cp.save('D://群组在线人数统计1.xls')
print('写入新数据保存成功！')