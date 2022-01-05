#coding:utf-8
from BaseInfoConfig import BasePathConfig
from time import sleep,time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait


class ListData():


    if __name__ == '__main__':
        driver = webdriver.Chrome(BasePathConfig.ChomedriverPath)
        driver.get("https://testnew.wisight.cn/login")
        driver.maximize_window()
        driver.implicitly_wait(5)
        driver.find_element_by_id("account").send_keys("admin@long.com")
        driver.find_element_by_id("password").send_keys("Password123")
        driver.find_element_by_xpath("*//button[@type='submit'][span]").click()
        driver.find_element_by_xpath("*//div[@class='ant-row']/div/ul/li[2]").click()  #企业工作台
        print(driver.find_element_by_xpath("*//div[@class='ant-row']/div/ul/li[2]").text)
        driver.find_elements_by_xpath("*//div[@class='ant-tree-list-holder-inner'")
        #complanNmae=driver.find_element_by_xpath("*//div[@class='ant-tree-treenode ant-tree-treenode-switcher-open ant-tree-treenode-selected']/span[3]") #选中企业名称[演示部]
        #complanNmae.click()
        #print("选中的企业名称为：",complanNmae.text)
        # element=WebDriverWait(driver,10).until(EC.visibility_of_element_located(By.XPATH,"*//div[@class='ant-row']/div[2]/button"))
        # element.click()
        # print(element.text)
        # driver.find_element_by_xpath("*//div[@class='ant-row']/div[2]/button").click()      #新增按钮
        # driver.find_element_by_xpath("*//input[@id='name']").send_keys(u"测试部门113")        #输入部门名称
        # driver.find_element_by_xpath("*//div[@class='ant-modal-footer']/button[2]").click()   #新增提交按钮