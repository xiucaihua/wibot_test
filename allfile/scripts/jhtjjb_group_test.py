#coding:utf-8
import unittest
from allfile.po.loginPage.loginPage import LoginPage
from allfile.po.commonPage.commonPage import CommonPage
from allfile.commonFunction.commonFunction import CommmonFunction

class Bytjjh(unittest.TestCase):
    u"""建行，北银天津，江北，登录功能"""

    def setUp(self):
        self.obj = LoginPage()
        self.obj.open_url('https://wibot.work/login')


    def tearDown(self):
        self.obj.close_broser()

    def test_3_getBytj_Data(self):
        """获取北银天津在群人数总数统计"""
        driver = self.obj.jh_tj_jb_login("admin@bobtjhx.com", "Password123")
        self.commmonFunction = CommmonFunction(driver)
        self.commmonFunction.write_Date_index_wibot('12月北京银行天津河西支行', '12月北京银行天津河西支行')

    def test_4_gethzjh_Data(self):
        """获取腾建行杭州之江支行群在群人数统计"""
        driver = self.obj.jh_tj_jb_login('admin@ccbhzzj.com', 'Password123')
        self.commmonFunction=CommmonFunction(driver)
        self.commmonFunction.write_Date_index_wibot('12月建行杭州之江支行', '12月建行杭州之江支行')

    def test_5_getJb_Data(self):
        """获取江北支行在群人数总数统计"""
        driver = self.obj.jh_tj_jb_login("admin@HFcqjb.com", "Password123")
        self.commmonFunction = CommmonFunction(driver)
        self.commmonFunction.write_Date_index_wibot('12月江北支行', '12月江北支行')
