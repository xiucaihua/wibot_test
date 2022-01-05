#coding:utf-8
import unittest
from allfile.po.loginPage.loginPage import LoginPage
from allfile.po.commonPage.commonPage import CommonPage
from allfile.commonFunction.commonFunction import CommmonFunction

class ATxCd_assistant(unittest.TestCase):
    u"""企点群在线统计功能"""

    def setUp(self):
        self.obj = LoginPage()
        self.obj.open_url('https://qdtest.wisight.cn/login')


    def tearDown(self):
        self.obj.close_broser()

    def test_1_txwl_login(self):
        """获取腾信国际物流群助理在线情况"""
        driver = self.obj.qdtx_assistant_active_login('admin@QDtxgjwl.com', 'Password123')
        self.commmonFunction=CommmonFunction(driver)
        self.commmonFunction.writeDate_qdtest_assistant('12月份腾信国际物流', '12月份腾信国际物流')

    def test_2_cdzs_login(self):
        """获取企点采购助手助理在线情况"""
        driver = self.obj.qdtx_assistant_active_login("admin@QDcgzs.com", "Password123")
        self.commmonFunction=CommmonFunction(driver)
        self.commmonFunction.writeDate_qdtest_assistant('12月份企点采购助手', '12月份企点采购助手')