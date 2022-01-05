#coding:utf-8

import time
from selenium import webdriver
from BaseInfoConfig import BasePathConfig
from selenium.webdriver.common.by import By
import xlwt

driver = webdriver.Chrome(BasePathConfig.ChomedriverPath)
driver.get("https://qdtest.wisight.cn/login")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, 'account').clear()
driver.find_element(By.ID, 'account').send_keys('admin@QDtxgjwl.com')
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg auth-form-button']").click()
time.sleep(5)

#点击服务套件
element=driver.find_element(By.XPATH,"//*[@id='root']/section/header/div/div[1]/ul/li[2]/span")
element.click()

#点击助理管理
element=driver.find_element(By.XPATH,"//*[@id='root']/section/section/aside/div/ul/li[4]/span/span")
print("助理管理的元素为：",element.text)
element.click()

#获取助理名称
assistantName=driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")
loginStatus=driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/div/span")



workbook = xlwt.Workbook()
worksheet = workbook.add_sheet(r'机器人状态')

def writeData():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(r'助理状态',)

    for list1 in assistantName:
        print("助理名称：", list1.text)
        worksheet.write(assistantName.index(list1), 0, list1.text)
        workbook.save('D:\\群组在线人数统计.xls')

    for list2 in loginStatus:
        print("助理状态：", list2.text)
        worksheet.write(loginStatus.index(list2), 1, list2.text)
        workbook.save('D:\\群组在线人数统计.xls')



if __name__ == '__main__':
    writeData()