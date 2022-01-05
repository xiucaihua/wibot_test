#coding:utf-8
from allfile.po.BasePage import BasePage
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from libs.ShareModules import InsertLog
log=InsertLog()


class CommonPage(BasePage):

    # 元素层
    servicePack_menu = (By.XPATH, "//*[@id='root']/section/header/div/div[1]/ul/li[2]/span")              # 服务套件
    groupManage_menu = (By.XPATH, "//*[@id='root']/section/section/aside/div/ul/li[2]/span/span")         # 群组管理
    pageTurnselect=(By.XPATH, "//span[@class='ant-select-selection-item']")                               #翻页下拉
    selectPageofNmber=(By.XPATH, "//div[@class='ant-select-item ant-select-item-option'][2]")             #每页显示50条
    firstGroupName=(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/span") #群组列表第一条数据
    afterTurnPageSize=(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span") #翻页显示后的所有群组数据

    #点击服务套件菜单
    def click_servicePack_menu(self):
        try:
            self.driver.find_element(*self.servicePack_menu).click()
            log.info(u'点击服务套件成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击服务套件.png")


    #点击群组管理菜单
    def click_groupManage_menu(self):
        try:
            self.driver.find_element(*self.groupManage_menu).click()
            log.info(u'点击群组管理成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击群组管理.png")

    #点击翻页显示下拉框
    def click_pageTurnselect(self):
        try:
            self.driver.find_element(*self.pageTurnselect).click()
            log.info(u'点击下拉选择翻页成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击翻页显示下拉框.png")

    #选择翻页条数，每页50条
    def click_selectPageofNmber(self):
        try:
            self.driver.find_element(*self.selectPageofNmber).click()
            global groupName
            groupName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 群组名称
            log.info(u'成功选择每页显示50条数据！')
        except BaseException as msg:
            self.get_screenshot_as_files(u"选择每页显示50条.png")

    #显示群组管理列表页面数据
    def groupNameLlist(self):
        self.click_servicePack_menu()  #点击服务套件
        self.click_groupManage_menu()  #点击群组管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName)) #等待群组列表第一条数据显示出来
        self.goUnderPage()            #拖动滚动条到网页底部
        self.click_pageTurnselect()   #点击下拉翻页选择显示条数
        self.click_selectPageofNmber() #选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize)) #等待显示翻页后的群组列表数据