#coding:utf-8
import unittest
from Po.login_page.LoginPage import LoginPage
from configTools.ExcelTools import ExcelToos
from ddt import data,ddt
from time import sleep


@ddt
class testloginCase(unittest.TestCase):
    u"""登录功能"""

    excelToos=ExcelToos()

    def setUp(self):
        self.obj=LoginPage()
        self.obj.open_url()

    def tearDown(self):
        self.obj.close_broser()


    @data(*excelToos.getExcelTestData("D:\data.xls", 1, 1))
    def test_error_login_001(self,data):
        """错误用户密码登录"""
        userName, passWord = tuple(data)
        sleep(2)
        self.obj.login(userName,passWord)
        r=self.obj.get_account_password_error_msg()
        self.assertEqual(r,u"用户名或密码不正确")


    @data(*excelToos.getExcelTestData("D:\data.xls", 0, 1))
    def test_sucess_login_001(self,data):
        """正确用户密码登录"""
        userName, passWord = tuple(data)
        sleep(2)
        self.obj.login(userName,passWord)
        r=self.obj.get_success_msg()
        self.assertEqual(r,u"系统工作台")

