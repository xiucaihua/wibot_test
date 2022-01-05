#coding:utf-8
import csv

"""
读取csv文件中的所有的数据
@:param csvPath csv文件路径
@:param mode  文件读写模式
@:return rows 列表形式返回所有数据
"""
def csvRead(csvPath,mode):
    with open(csvPath,mode) as csvfile:
        reader = csv.reader(csvfile)
        rows = [row for row in reader]
    return  rows



"""
读取csv文件中的所有的数据
@:param csvPath csv文件路径
@:param mode  文件读写模式
@:param index 读取的行坐标
@:return rows 列表形式返回读取的行的数据
"""
def readIndexof(csvPath,mode,index):
    with open(csvPath,mode) as csvfile:
        reader = csv.reader(csvfile)
        column = [row[index] for row in reader]
    return column




"""
正常读取CSV的数据
"""

with open(r"D:\data.csv", encoding="gb18030", errors="ignore") as f:
    as_csv = csv.reader((line.replace('\0', '') for line in f), delimiter=",")
    for i in as_csv:
        print(i)
