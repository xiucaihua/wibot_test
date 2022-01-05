#coding:utf-8
import unittest
from allfile.po.loginPage.loginPage import LoginPage
from allfile.po.commonPage.commonPage import CommonPage
from allfile.commonFunction.commonFunction import CommmonFunction

class BJJHCQ_assistant(unittest.TestCase):
    u"""登录功能"""

    def setUp(self):
        self.obj = LoginPage()
        self.obj.open_url('https://wibot.work/login')


    def tearDown(self):
        self.obj.close_broser()

    def test_3_jh_login(self):
        """获取建行杭州之江支行助理在线情况"""
        driver = self.obj.wibot_assistant_active_login('admin@ccbhzzj.com', 'Password123')
        self.commmonFunction=CommmonFunction(driver)
        self.commmonFunction.writeDate_wibot_assistant('12月建行杭州之江支行', '12月建行杭州之江支行')


    def test_4_bytj_login(self):
        """获取北银天津助理状态情况"""
        driver = self.obj.wibot_assistant_active_login("admin@bobtjhx.com", "Password123")
        self.commmonFunction=CommmonFunction(driver)
        self.commmonFunction.writeDate_wibot_assistant('12月北京银行天津河西支行', '12月北京银行天津河西支行')

    def test_5_cqhc_login(self):
        """获取恒丰重庆合川支行助理状态情况"""
        driver = self.obj.wibot_assistant_active_login("admin@HFcqhc.com", "Password123")
        self.commmonFunction = CommmonFunction(driver)
        self.commmonFunction.writeDate_wibot_assistant('12月恒丰重庆合川支行', '12月恒丰重庆合川支行')

    def test_6_cqhf_login(self):
        """获取恒丰重庆江北支行助理状态情况"""
        driver = self.obj.wibot_assistant_active_login("admin@HFcqjb.com", "Password123")
        self.commmonFunction = CommmonFunction(driver)
        self.commmonFunction.writeDate_wibot_assistant('12月份恒丰重庆江北支行', '12月份恒丰重庆江北支行')