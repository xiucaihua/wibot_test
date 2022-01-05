#coding:utf-8
import unittest
from configTools.gettime_copy2 import GetDatabj

class TestAll(unittest.TestCase):

    def setUp(self):
        global allshili
        allshili=GetDatabj()
        allshili.driver.get("https://qdtest.wisight.cn/login")
        allshili.driver.implicitly_wait(10)
        allshili.driver.maximize_window()

    def tearDown(self):
        allshili.quitDriver()


    def test_getQDtxgjwl_Data(self):
        """获取腾信国际物流群在群人数统计"""
        allshili.login("admin@QDtxgjwl.com", "Password123")
        allshili.write_Date_index('12月份腾信国际物流', '12月份腾信国际物流')

    def test_getQDcgzs_Data(self):
        """获取企点采购助手群在群人数统计"""
        allshili.login("admin@QDcgzs.com", "Password123")
        allshili.write_Date_index('12月份企点采购助手', '12月份企点采购助手')