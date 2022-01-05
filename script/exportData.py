#coding:utf8
from selenium import webdriver
import time,os
from BaseInfoConfig import BasePathConfig
from selenium.webdriver.common.by import By
import xlwt
import random

driver = webdriver.Chrome(BasePathConfig.ChomedriverPath)
driver.get("https://qdtest.wisight.cn/login")
driver.implicitly_wait(10)
driver.maximize_window()



driver.find_element(By.ID, 'account').clear()
driver.find_element(By.ID, 'account').send_keys('admin@QDtxgjwl.com')
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg auth-form-button']").click()

element=driver.find_element(By.XPATH,"//*[@id='root']/section/header/div/div[1]/ul/li[2]/span")
element.click()
elemnt1=driver.find_element(By.XPATH,"//*[@id='root']/section/section/aside/div/ul/li[2]/span/span")
elemnt1.click()

groupName=  driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")
memberCount=driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span")
company=driver.find_element(By.XPATH,"//*[@id='root']/section/header/div/div[2]/div/span[3]")
print(company.text)


def writeData():
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(r'12月份腾信国际物流')

    # rows=31
    # for i in rows:
    #     worksheet.write(0, i, '12月'+i+'号')

    # 改变行高或者列宽  xlwt中是行和列都是从0开始计算的
    first_col = worksheet.col(0)    #第一列
    two_col = worksheet.col(1)      #第二列
    three_col = worksheet.col(2)    #第三列
    # sec_col = worksheet.col(0)
    first_col.width = 320 * 20       #第一列的宽，高
    two_col.width =   320 * 20       #第二列的宽，高
    three_col.width = 100 * 20       #第三列的宽，高

    #写入公司名称
    worksheet.write(1, 0,company.text)

    #写入群组名称到excel
    for list1 in groupName:
        print("群组名称	：", list1.text)
        worksheet.write(groupName.index(list1)+1, 1, list1.text)
        #workbook.save('D:\\群组在线人数统计1.xls')

    #写入群组总数到excel
    for list2 in memberCount:
        print("群组总人数：", list2.text)
        worksheet.write(memberCount.index(list2)+1, 2, list2.text)
        #workbook.save('D:\\群组在线人数统计1.xls')
    workbook.save('D:\\群组在线人数统计1.xls')

# if __name__ == '__main__':
#     writeData()