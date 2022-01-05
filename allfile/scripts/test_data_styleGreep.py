#coding:utf-8
import unittest
from allfile.scripts.mergsheets import SheetClass
from allfile.scripts.data_styleGreep import GreepData


class StyleGreep(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    #清除表格里面的非真实群组数据
    def test_7_greepData(self):
        """清除掉非真实群组信息"""
        greepData = GreepData()
        listData = greepData.getDifferent('./群人数在线统计综合.xlsx', 0)
        greepData.deleteRow('./群人数在线统计综合.xlsx', 'Sheet1', listData, './删除后保留的数据.xlsx')

    #设置第一列单元格合并
    def test_8_setExcelStyle(self):
        """设置第一列单元格合并"""
        greepData = GreepData()
        greepData.mergeCell("./删除后保留的数据.xlsx", "./群组合并单元格的.xlsx")

    #设置表格的最终样式
    def test_9_setcolsSize(self):
        """设置第一第二列宽度"""
        sheetClass = SheetClass()
        sheetClass.setExcelStyle('./群组合并单元格的.xlsx', 'Sheet1', './群组每日在群情况统计(所有公司).xlsx')

    # 设置助理第一列单元格合并
    def test_zassistant_setExcelStyle(self):
        """设置第一列单元格合并"""
        greepData = GreepData()
        greepData.mergeAssistantCell("./每日助理在线情况统计.xlsx", "./助理合并单元格的.xlsx")

    # 设置助理表格的最终样式
    def test_zassistant_setcolsSize(self):
        """设置第一第二列宽度"""
        sheetClass = SheetClass()
        sheetClass.setExcelStyle('D:\\FramWork\\allfile\\run\\助理合并单元格的.xlsx', 'Sheet1', 'D:\\FramWork\\allfile\\run\\每日助理在线情况统计(所有公司).xlsx')