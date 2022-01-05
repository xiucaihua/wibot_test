#coding:utf-8
import unittest
from allfile.scripts.mergsheets import SheetClass

class MergSheet(unittest.TestCase):


    def test_6_mergSheet(self):
        """合并群组在线sheet"""
        sheetclass =SheetClass()
        sheetclass.mergeSheets("D://每日在群人数统计.xls", "./群人数在线统计综合.xlsx")


    def test_mergAssistantSheet(self):
        """合并助理在线情况sheet"""
        sheetclass =SheetClass()
        sheetclass.mergeSheets("D://每日助理在线情况统计.xls", "./每日助理在线情况统计.xlsx")