#coding:utf-8
import unittest
from Po.login_page.LoginPage import LoginPage
from Po.worktable_page.team_management_page.TeamManagementPage import TeamManagementPage
from libs.ShareBusiness import login_B



class TeamManagementTest(unittest.TestCase):
    u"""组织架构管理"""

    def setUp(self):
        driver = login_B("admin@long.com","Password123")
        self.obj_tmp = TeamManagementPage(driver)  # 组织架构管理页

    def test_addstudent_success(self):
        """正常添加组织架构名称"""
        self.obj_tmp.add_department("组织架构")
        # self.assertEqual(msg,"admin")

    def tearDown(self):
        self.obj_tmp.close_broser()