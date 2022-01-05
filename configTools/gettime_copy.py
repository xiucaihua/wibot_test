#coding:utf-8
import xlwt,xlrd,time,datetime
from selenium import webdriver
from BaseInfoConfig import BasePathConfig
from selenium.webdriver.common.by import By
from xlutils.copy import copy
from xlutils import copy



driver = webdriver.Chrome(BasePathConfig.ChomedriverPath)
driver.get("https://qdtest.wisight.cn/login")
driver.implicitly_wait(10)
driver.maximize_window()

driver.find_element(By.ID, 'account').clear()
driver.find_element(By.ID, 'account').send_keys('admin@QDtxgjwl.com')
driver.find_element(By.ID, 'password').clear()
driver.find_element(By.ID, 'password').send_keys('Password123')
driver.find_element(By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-lg auth-form-button']").click()

driver.find_element(By.XPATH,"//*[@id='root']/section/header/div/div[1]/ul/li[2]/span").click()
driver.find_element(By.XPATH,"//*[@id='root']/section/section/aside/div/ul/li[2]/span/span").click()

groupName=  driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")
memberCount=driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span")
company=driver.find_element(By.XPATH,"//*[@id='root']/section/header/div/div[2]/div/span[3]")
print(company.text)


def writeData(writindex):
    # 1、使用xlrd打开Excel
    workbook = xlrd.open_workbook("D://群组在线人数统计1.xls")
    # 2、使用xlutils模块的copy复制打开的文件，并保留原格式
    open_mb_file_cp = copy.copy(workbook)
    # 3、使用下标定位的方式定位到Excel工作簿里的工作表
    worksheet = open_mb_file_cp.get_sheet(r"12月份腾信国际物流")


    # 改变行高或者列宽  xlwt中是行和列都是从0开始计算的
    first_col = worksheet.col  #第一列
    two_col = worksheet.col(1)      #第二列
    three_col = worksheet.col(2)    #第三列
    # sec_col = worksheet.col(0)
    #first_col.width= 320 * 20       #第一列的宽，高
    #two_col.width =   320 * 20       #第二列的宽，高
    #three_col.width = 100 * 20       #第三列的宽，高

    #写入公司名称
   # worksheet.write(1, 0,company.text)
   # worksheet.write(1, 0, company.text)
    worksheet.write(1, 0, company.text)
    #worksheet.write(0, 0, '新数据写入')
    #写入群组名称到excel
    for list1 in groupName:
        print("群组名称	：", list1.text)
        worksheet.write(groupName.index(list1)+1, 1, list1.text)


    #写入群组总数到excel
    for list2 in memberCount:
        print("群组总人数：", list2.text)
        worksheet.write(memberCount.index(list2)+1, writindex, list2.text)
    open_mb_file_cp.save('D://群组在线人数统计1.xls')



def write_Date_index():
    # 获取当前的时间以【12月21日】格式输出
    now_time = time.strftime("%y%m%d", time.localtime())
    struct_time = time.strptime(now_time, "%y%m%d")
    format_now_time = time.strftime("%m{m}%d{d}", struct_time).format(m='月', d='号')
    print("当前的日期为：", format_now_time)

    workbook = xlrd.open_workbook(r"D:\\群组在线人数统计1.xls")
    workSheet = workbook.sheet_by_name("12月份腾信国际物流")

    firstRowDat=workSheet.row_values(0)
    print(firstRowDat)
    print(firstRowDat)


    for index, value in enumerate(firstRowDat):
        if format_now_time == value:
            print("调用写入到excel的方法")
            print("下标为：", index, value)
            print("OK!")
            print(index)
            writeData(index) #调用写入数据到指定日期的方法
            break
        else:
            print("当前日期和表格中的日期不匹配！")

if __name__ == '__main__':
    write_Date_index()