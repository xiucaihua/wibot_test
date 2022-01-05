from pandas import pandas as pd
import openpyxl
import xlrd,xlwt
import tkinter

class SheetClass():

    #把excel中相同格式的sheet合并起来
    def mergeSheets(slef,fileName, savePath):
        # 读取excel
        df: pd.DataFrame = pd.read_excel(fileName, sheet_name=None)
        # 创建一个空的DataFrame，columns指定为excel的第一个sheet的columns
        tmpdf: pd.DataFrame = pd.DataFrame(columns=pd.read_excel(fileName).columns)
        # 获取excel的所有sheet
        sheets = df.keys()
        # 遍历sheet，把每个sheet的数据垂直合并起来
        for sheet in sheets:
            tmpdf = pd.concat([tmpdf, df.get(sheet)])
        # 将结果写入保存位置
        tmpdf.to_excel(savePath, index=False)
        print("写入成功！")



    """
    设置表格样式
    """
    def setExcelStyle(self,fileName,sheetName,saveFileName):
        workbook = openpyxl.load_workbook(fileName)
        sheet = workbook.get_sheet_by_name(sheetName)
        sheet.row_dimensions[1].height = 22
        sheet.column_dimensions['A'].width = 28
        sheet.column_dimensions['B'].width = 28
        workbook.save(saveFileName)

#
# if __name__ == '__main__':
#     o=SheetClass()
#     #o.setExcelStyle()
#     o.setExcelStyle('./合并后的.xlsx','Sheet1','./合并后的.xlsx')