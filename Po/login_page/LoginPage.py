# coding:utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Po.BasePage import BasePage
from BaseInfoConfig import LogMessage
from time import sleep
from libs.ShareModules import InsertLog
log=InsertLog()

class LoginPage(BasePage):

    # 元素层
    ipt_username_loc = (By.ID, "account")                                                                               # 登录用户名
    ipt_password_loc = (By.ID, "password")                                                                              # 登录密码
    login_button_loc = (By.XPATH, "*//button[@type='submit'][span]")                                                    # 登录按钮
    txt_account_error_msg_loc=(By.XPATH,"*//div[@class='ant-message-custom-content ant-message-error']/span[2]")        #"用户名或密码不正确"
    txt_success_msg_loc = (By.XPATH,"*//span[@class='ant-menu-title-content']/a[text()='系统工作台']")                   # 登录成功，显示系统工作台


    # 输入用户名
    def set_username(self, username):
        try:
            self.dr.find_element(*self.ipt_username_loc).send_keys(username)
            log.info(u"输入用户名：" + username + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement +username + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入用户名.png")
            print(msg)



    # 输入密码
    def set_password(self, password):
        try:
            self.dr.find_element(*self.ipt_password_loc).send_keys(password)
            log.info(u"输入密码：" + password + LogMessage.Pass)
        except BaseException as msg:
            log.error(LogMessage.findElement + password + LogMessage.Fail)
            self.get_screenshot_as_files(u"输入密码.png")
            print (msg)


    # 点击登录按钮
    def click_login_button(self):
        try:
            self.dr.find_element(*self.login_button_loc).click()
            log.info(u"点击登录按钮成功！")
        except BaseException as msg:
            log.error("点击登录按钮失败！")
            self.get_screenshot_as_files(u"点击登录按钮.png")
            print (msg)


    # 密码或者错误
    def get_account_password_error_msg(self):
        #WebDriverWait(self.dr, 10, 0.5).until(EC.text_to_be_present_in_element(self.get_success_msg(), u"用户名或密码不正确"))
        r = self.dr.find_element(*self.txt_account_error_msg_loc).text
        return r


    # 登录成功
    def get_success_msg(self):
        r = self.dr.find_element(*self.txt_success_msg_loc).text
        return r

     # 登录流程
    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_login_button()
        sleep(1)
        return self.dr