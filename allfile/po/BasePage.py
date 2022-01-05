# coding:utf-8
from selenium.webdriver.remote.webdriver import WebDriver
from time import sleep,time
import os
from  selenium.webdriver.support.select import Select
from BaseInfoConfig import BaseInfoCofig
from BaseInfoConfig import BasePathConfig
from BaseInfoConfig import LogMessage
from selenium import webdriver
from  selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import  WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement


from libs.ShareModules import InsertLog
log=InsertLog()

class BasePage():
    u"""所有页面对象的基类"""

    def __init__(self, driver:WebDriver=''):
        b = driver
        if b == '':
            self.driver = self.create_browser()
            log.info("创建浏览器对象成功!")
        else:
            self.driver = b
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    #创建浏览器
    def create_browser(self, b='g'):
        if b == 'g':
            d = webdriver.Chrome(BasePathConfig.ChomedriverPath)
            log.info("创建谷歌浏览器对象成功!")
        elif b == 'f':
            d = webdriver.Firefox()
            log.info("创建火狐浏览器对象成功!")
        return d

    #打开访问地址
    def open_url(self, url):
        try:
            self.driver.get(url)
            log.info("打开"+url+LogMessage.Pass)
        except BaseException as msg:
            print (msg)


    #关闭浏览器
    def close_broser(self):
        try:
            if self.driver!=None:
                log.info("关闭浏览器对象成功！")
                self.driver.quit()
        except BaseException as msg:
            print (msg)

    #退出diver驱动操作
    def quitDriver(self):
        self.driver.quit()


    """
    功能描述：截图功能
    创建者：修才华
    创建时间：2021/11/06
    """
    def get_screenshot_as_files(self, imageNmae, imagePath=BasePathConfig.imagePath):
        try:
            self.driver.get_screenshot_as_file(imagePath+imageNmae)
            log.info("截图方法调用---成功！")
        except BaseException as msg:
            log.error("截图方法调用--失败！")
            print (msg)

     #返回操作
    def goBack(self):
        self.driver.back()
        log.info("返回成功！")

    #刷新操作
    def Refresh(self):
        self.driver.refresh()
        log.info("刷新操作成功！")

    # 前进操作
    def forWard(self):
        self.driver.forward()
        log.info("前进操作成功！")

    #隐式等待
    def new_implicitly_wait(self,time_to_wait):
        self.driver.implicitly_wait(time_to_wait)

    #sleep等待
    def new_Sleep(self,time):
        try:
            sleep(time)
        except Exception as msg:
            print (msg)

    # 获取当前的URL
    def ger_current_url(self):
        return self.driver.current_url
        #log.info("获取到当前"+dr.current_url+LogMessage.Pass)

    #滚动条到底部
    def goUnderPage(self):
        js = "window.scrollTo(0,document.body.scrollHeight)"
        self.driver.execute_script(js)
        log.info("滚动条拖动到底部！")

    # 执行js拖拽，拖拽到顶部
    def goTopPage(self):
        js = "window.scrollTo(0,0)"
        self.driver.execute_script(js)
        log.info("滚动条拖动到顶部！")


# 一直等待某个元素可见，页面出现马上执行下一步操作，如果在规定时间内没有出现，也会执行下一步操作，比如设置30秒，10秒该元素就出现，也会执行下一步
def is_visible(self,byTye,locatorValue,timeout,poll_frequency=0.5):
    try:
        element = WebDriverWait(self.driver,timeout).until(EC.visibility_of_element_located((byTye, locatorValue)))
        element:WebElement
        return element          #找到元素返回元素对象
    except Exception as e:
        print(e)
        raise Exception("没有找到指定的元素！")