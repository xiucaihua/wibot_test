#coding:utf-8
from Po.BasePage import BasePage
from selenium.webdriver.common.by import By
from libs.ShareModules import InsertLog
log=InsertLog()

class TeamManagementPage(BasePage):
    u"""企业管理列表页面"""

    mun_worktable_loc=(By.XPATH,"*//div[@class='ant-row']/div/ul/li[2]")                                                                    #企业工作台
    complanNmae_loc=(By.XPATH, "*//div[@class='ant-tree-treenode ant-tree-treenode-switcher-open ant-tree-treenode-selected']/span[3]")     #选中部门名称【演示部】
    button_addDepartment_loc=(By.XPATH,"*//div[@class='ant-row']/div[2]/button")                                                             #新增部门按钮
    input_departmentName_loc=(By.XPATH,"*//input[@id='name']")                                                                               #部门名称
    button_conmitAddDepartment_loc=(By.XPATH,"*//div[@class='ant-modal-footer']/button[2]")                                                  #'新增提交按钮'

    # 新增组织架构部门名称
    def add_department(self,departmentName):
        try:
            self.dr.find_element(*self.mun_worktable_loc).click()
            log.info("点击企业工作台元素成功")
            self.dr.find_element(*self.complanNmae_loc).click()
            log.info(u"点击演示部门元素成功")
            self.dr.find_element(*self.button_addDepartment_loc).click()
            log.info(u"点击新增部门按钮元素成功")
            self.dr.find_element(*self.input_departmentName_loc).send_keys(departmentName)
            log.info(u"输入部门名称元素成功")
            self.dr.find_element(*self.button_conmitAddDepartment_loc).click()
            log.info(u"点击新增部门提交元素成功")
        except BaseException as msg:
            # log.info(LogMessage.findElement + self.memberCenter_loc + LogMessage.Fail)
            self.get_screenshot_as_files("新增部门失败_error.png")
            print(msg)

class EmployeesManagement(BasePage):
    u"""员工管理页面"""
    addEmploye_Button_loc=(By.XPATH,"*//button[@class='ant-btn ant-btn-primary']/span[text()='新增员工']")                                  #新增员工按钮
