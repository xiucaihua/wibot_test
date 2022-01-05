#coding:utf-8
from allfile.po.commonPage.commonPage import CommonPage
from allfile.po.BasePage import BasePage
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from libs.ShareModules import InsertLog
log=InsertLog()



class LoginPage(BasePage):
    # 元素层
    ipt_username_loc = (By.ID, 'account')  # 登录用户名
    ipt_password_loc = (By.ID, 'password')  # 登录密码
    login_button_loc = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg auth-form-button']")  # 登录按钮
    servicePack_menu = (By.XPATH, "//*[@id='root']/section/header/div/div[1]/ul/li[2]/span")        # 服务套件
    groupManage_menu = (By.XPATH, "//*[@id='root']/section/section/aside/div/ul/li[2]/span/span")    # qdtest群组管理
    wibot_groupManage_menu=(By.XPATH,"//*[@id='root']/section/section/aside/div/ul/li[2]/span/span")  # wibot群组管理
    wibot_assistantMange=(By.XPATH,'//*[@id="root"]/section/section/aside/div/ul/li[7]/span/span')    #wibot助理管理
    qdtest_assistantMange=(By.XPATH,"//*[@id='root']/section/section/aside/div/ul/li[4]/span/span")    #qdtest助理管理
    assistantName =(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 助理名称
    assistantActive = (By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/div/span")  # 助理在线情况
    pageTurnselect = (By.XPATH, "//span[@class='ant-select-selection-item']")                         # 翻页下拉
    selectPageofNmber = (By.XPATH, "//div[@class='ant-select-item ant-select-item-option'][2]")       # 每页显示50条
    firstGroupName = (By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr[2]/td[2]/span")  # 群组列表第一条数据
    afterTurnPageSize = (By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 翻页显示后的所有群组数据

    """
    输入用户名
    :param userName 用户名
    """
    def set_username(self, userName):
        try:
            self.driver.find_element(*self.ipt_username_loc).clear()
            self.driver.find_element(*self.ipt_username_loc).send_keys(userName)
            log.info(u"输入用户名：" + userName + "成功")
        except BaseException as msg:
            self.get_screenshot_as_files(u"输入用户名.png")

    """
    输入密码
    :param passWord: 密码
    """
    def set_passWord(self,passWord):
        try:
            self.driver.find_element(*self.ipt_password_loc).clear()
            log.info(u"清除密码：" + passWord + "成功")
            self.driver.find_element(*self.ipt_password_loc).send_keys(passWord)
            log.info(u"输入用密码：" + passWord + "成功")
        except BaseException as msg:
            self.get_screenshot_as_files(u"输入密码.png")

    #点击登录按钮
    def click_loginButton(self):
        try:
            self.driver.find_element(*self.login_button_loc).click()
            log.info(u"点击登录按钮成功")
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击登录按钮.png")


    """
    企点，腾信物流，群在线登录方法
    :param userName：用户名
    :param passWord  密码
    """
    def qd_tx_login(self, userName, passWord):
        self.set_username(userName)   #输入用户名
        self.set_passWord(passWord)  #输入密码
        self.click_loginButton()    #点击登录按钮
        self.click_servicePack_menu()  # 点击服务套件
        self.click_groupManage_menu()  # 点击群组管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName))  # 等待群组列表第一条数据显示出来
        self.goUnderPage()  # 拖动滚动条到网页底部
        self.click_pageTurnselect()  # 点击下拉翻页选择显示条数
        self.click_selectPageofNmber()  # 选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize))  # 等待显示翻页后的群组列表数据
        self.new_Sleep(5)
        return self.driver



    """
    建行，天津，江北，群在线登录方法
    :param userName：用户名
    :param passWord  密码
    """
    def jh_tj_jb_login(self, userName, passWord):
        self.set_username(userName)   #输入用户名
        self.set_passWord(passWord)  #输入密码
        self.click_loginButton()    #点击登录按钮
        self.click_servicePack_menu()  # 点击服务套件
        self.click_wibot_groupManage_menu()  # 点击群组管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName))  # 等待群组列表第一条数据显示出来
        self.goUnderPage()  # 拖动滚动条到网页底部
        self.click_pageTurnselect()  # 点击下拉翻页选择显示条数
        self.click_selectPageofNmber()  # 选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize))  # 等待显示翻页后的群组列表数据
        self.new_Sleep(3)
        return self.driver

    """
    企点，腾信物流，助理状态获取方法
    :param userName：用户名
    :param passWord  密码
    """
    def qdtx_assistant_active_login(self, userName, passWord):
        self.set_username(userName)   #输入用户名
        self.set_passWord(passWord)  #输入密码
        self.click_loginButton()    #点击登录按钮
        self.click_servicePack_menu()  # 点击服务套件
        self.click_qdtest_assistantMange()  # 点击助理管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName))  # 等待群组列表第一条数据显示出来
        self.goUnderPage()  # 拖动滚动条到网页底部
        self.click_pageTurnselect()  # 点击下拉翻页选择显示条数
        self.click_selectPageofNmber()  # 选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize))  # 等待显示翻页后的群组列表数据
        self.new_Sleep(5)
        return self.driver

    """
    建行，江北，重庆合川，恒丰重庆江北支行，助理状态获取方法
    :param userName：用户名
    :param passWord  密码
    """
    def wibot_assistant_active_login(self, userName, passWord):
        self.set_username(userName)   #输入用户名
        self.set_passWord(passWord)  #输入密码
        self.click_loginButton()    #点击登录按钮
        self.click_servicePack_menu()  # 点击服务套件
        self.click_wibot_assistantMange()  # 点击助理管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName))  # 等待群组列表第一条数据显示出来
        self.goUnderPage()  # 拖动滚动条到网页底部
        self.click_pageTurnselect()  # 点击下拉翻页选择显示条数
        self.click_selectPageofNmber()  # 选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize))  # 等待显示翻页后的群组列表数据
        self.new_Sleep(5)
        return self.driver

    # 用户登录方法
    def login(self, suer, pwd):
        self.set_username(suer)  # 输入用户名
        self.set_passWord(pwd)  # 输入密码
        self.click_loginButton()  # 点击登录按钮
        return self.driver

    # 点击服务套件菜单
    def click_servicePack_menu(self):
        try:
            self.driver.find_element(*self.servicePack_menu).click()
            log.info(u'点击服务套件成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击服务套件.png")

    # 点击wibot助理管理
    def click_wibot_assistantMange(self):
        try:
            self.driver.find_element(*self.wibot_assistantMange).click()
            log.info(u'点击wibot助理管理成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击wibot助理管理.png")

    # 点击qdtest助理管理
    def click_qdtest_assistantMange(self):
        try:
            self.driver.find_element(*self.qdtest_assistantMange).click()
            log.info(u'点击qdtest助理管理成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击qdtest助理管理.png")

    # 点击qdtest群组管理菜单
    def click_groupManage_menu(self):
        try:
            self.driver.find_element(*self.groupManage_menu).click()
            log.info(u'点击群组管理成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击群组管理.png")

    # 点击wibot群组管理菜单
    def click_wibot_groupManage_menu(self):
        try:
            self.driver.find_element(*self.wibot_groupManage_menu).click()
            log.info(u'点击群组管理成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击群组管理.png")

    # 点击翻页显示下拉框
    def click_pageTurnselect(self):
        try:
            self.driver.find_element(*self.pageTurnselect).click()
            log.info(u'点击下拉选择翻页成功')
        except BaseException as msg:
            self.get_screenshot_as_files(u"点击翻页显示下拉框.png")

    # 选择翻页条数，每页50条
    def click_selectPageofNmber(self):
        try:
            self.driver.find_element(*self.selectPageofNmber).click()
            global groupName
            groupName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 群组名称
            log.info(u'成功选择每页显示50条数据！')
        except BaseException as msg:
            self.get_screenshot_as_files(u"选择每页显示50条.png")

    # 显示群组管理列表页面数据
    def groupNameLlist(self):
        self.click_servicePack_menu()  # 点击服务套件
        self.click_groupManage_menu()  # 点击群组管理
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.firstGroupName))  # 等待群组列表第一条数据显示出来
        self.goUnderPage()  # 拖动滚动条到网页底部
        self.click_pageTurnselect()  # 点击下拉翻页选择显示条数
        self.click_selectPageofNmber()  # 选择每页具体的显示数目
        WebDriverWait(self.driver, 5).until(lambda x: x.find_element(*self.afterTurnPageSize))  # 等待显示翻页后的群组列表数据