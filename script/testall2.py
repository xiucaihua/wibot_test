#coding:utf-8
import unittest
from configTools.gettime_copy2 import GetDatabj

class TestAll2(unittest.TestCase):

    def setUp(self):
        global allshili2
        allshili2=GetDatabj()
        allshili2.driver.get("https://wibot.work/login")
        allshili2.driver.implicitly_wait(10)
        allshili2.driver.maximize_window()

    def tearDown(self):
        allshili2.quitDriver()

    def test_getBytj_Data(self):
        """获取北银天津在群人数总数统计"""
        allshili2.login("admin@bobtjhx.com", "Password123")
        allshili2.write_Date_index('12月北京银行天津河西支行', '12月北京银行天津河西支行')

    def test_gethzjh_Data(self):
        """获取杭州建行在群人数总数统计"""
        allshili2.login("admin@ccbhzzj.com", "Password123")
        allshili2.write_Date_index('12月建行杭州之江支行', '12月建行杭州之江支行')