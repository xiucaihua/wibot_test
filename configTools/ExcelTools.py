#coding:utf-8
from openpyxl import load_workbook
from openpyxl import  Workbook
from configparser import ConfigParser
import xlrd

class ExcelToos():

    """
    Excel数据驱动方法
    """
    def getExcelTestData(self,excelPath,sheetOfIndex,startRowNumer):
        # 打开Excel文件
        openExcelFile = xlrd.open_workbook(excelPath,)
        # 获取工作表
        getSheet = openExcelFile.sheet_by_index(sheetOfIndex)
        # 获取所有的行数
        rowNumber = getSheet.nrows
        # 数据List
        dataList = []

        for i in range(startRowNumer, rowNumber):
            # 从第二行开始遍历每一行
            dataList.append(getSheet.row_values(i))
            #print("每行的数据为：", getSheet.row_values(i))
            # 把每个单元格的数值存放到dataList中
        return dataList
