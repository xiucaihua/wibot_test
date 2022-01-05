#coding:utf-8
from  selenium.webdriver.common.by import By
import xlrd,time
from xlutils import copy
from allfile.po.groupManage.groupManagePage import GroupManagePage
from allfile.po.BasePage import BasePage
from allfile.po.commonPage.commonPage import CommonPage

class CommmonFunction(BasePage):

    def writeData_wibot(self,writindex,openSheetName):
        groupName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 群组名称
        memberCount = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[6]/span")  # 群组总人数
        company = self.driver.find_element(By.XPATH, "//*[@id='root']/section/header/div/div[2]/div/span[3]")  # 公司名称
        print(company.text)

        # 1、使用xlrd打开Excel
        workbook = xlrd.open_workbook("D:\\每日在群人数统计.xls")
        # 2、使用xlutils模块的copy复制打开的文件，并保留原格式
        open_mb_file_cp = copy.copy(workbook)
        # 3、使用下标定位的方式定位到Excel工作簿里的工作表
        worksheet = open_mb_file_cp.get_sheet(openSheetName)

        # 写入公司名称
        worksheet.write(1, 0, company.text)

        #写入群组名称到excel
        for list1 in groupName:
            print("群组名称	：", list1.text)
            worksheet.write(groupName.index(list1) + 1, 1, list1.text)

        # 写入群组总数到excel
        for list2 in memberCount:
            print("群组总人数：", list2.text)
            worksheet.write(memberCount.index(list2) + 1, writindex, list2.text)
        open_mb_file_cp.save('D:\\每日在群人数统计.xls')

    def write_Date_index_wibot(self, writeSheetName, openSheetName):
        # 获取当前的时间以【12月21日】格式输出
        now_time = time.strftime("%y%m%d", time.localtime())
        struct_time = time.strptime(now_time, "%y%m%d")
        format_now_time = time.strftime("%m{m}%d{d}", struct_time).format(m='月', d='号')
        print("当前的日期为：", format_now_time)

        workbook = xlrd.open_workbook(r"D:\\每日在群人数统计.xls")
        workSheet = workbook.sheet_by_name(writeSheetName)

        firstRowDat = workSheet.row_values(0)
        print("第一行的数据为：", firstRowDat)

        for index, value in enumerate(firstRowDat):
            if format_now_time == value:
                print("调用写入到excel的方法")
                print("下标为：", index, value)
                self.writeData_wibot(index, openSheetName)  # 调用写入数据到指定日期的方法
                break
            else:
                continue

    def writeData_qdtest(self, writindex, openSheetName):
        groupName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 群组名称
        memberCount = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span")  # 群组总人数
        company = self.driver.find_element(By.XPATH, "//*[@id='root']/section/header/div/div[2]/div/span[3]")  # 公司名称
        print(company.text)

        # 1、使用xlrd打开Excel
        workbook = xlrd.open_workbook("D:\\每日在群人数统计.xls")
        # 2、使用xlutils模块的copy复制打开的文件，并保留原格式
        open_mb_file_cp = copy.copy(workbook)
        # 3、使用下标定位的方式定位到Excel工作簿里的工作表
        worksheet = open_mb_file_cp.get_sheet(openSheetName)

        # 写入公司名称
        worksheet.write(1, 0, company.text)

        # 写入群组名称到excel
        for list1 in groupName:
            print("群组名称	：", list1.text)
            worksheet.write(groupName.index(list1) + 1, 1, list1.text)

        # 写入群组总数到excel
        for list2 in memberCount:
            print("群组总人数：", list2.text)
            worksheet.write(memberCount.index(list2) + 1, writindex, list2.text)
        open_mb_file_cp.save('D:\\每日在群人数统计.xls')

    def write_Date_index_qdtest(self,writeSheetName,openSheetName):
        # 获取当前的时间以【12月21日】格式输出
        now_time = time.strftime("%y%m%d", time.localtime())
        struct_time = time.strptime(now_time, "%y%m%d")
        format_now_time = time.strftime("%m{m}%d{d}", struct_time).format(m='月', d='号')
        print("当前的日期为：", format_now_time)

        workbook = xlrd.open_workbook(r"D:\\每日在群人数统计.xls")
        workSheet = workbook.sheet_by_name(writeSheetName)

        firstRowDat = workSheet.row_values(0)
        print("第一行的数据为：",firstRowDat)


        for index, value in enumerate(firstRowDat):
            if format_now_time == value:
                print("调用写入到excel的方法")
                print("下标为：", index, value)
                print("OK!")
                print(index)
                self.writeData_qdtest(index,openSheetName)  # 调用写入数据到指定日期的方法
                break
            else:
                continue

    def writeData_wibot_assistant2(self, writindex,openSheetName):
        zhuliName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")         #助理名称
        loginActive = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[8]/div/span")  # 助理在线情况
        company = self.driver.find_element(By.XPATH, "//*[@id='root']/section/header/div/div[2]/div/span[3]")  # 公司名称
        print(company.text)

        # 1、使用xlrd打开Excel
        workbook = xlrd.open_workbook("D:\\每日助理在线情况统计.xls")
        # 2、使用xlutils模块的copy复制打开的文件，并保留原格式
        open_mb_file_cp = copy.copy(workbook)
        # 3、使用下标定位的方式定位到Excel工作簿里的工作表
        worksheet = open_mb_file_cp.get_sheet(openSheetName)

        # 写入公司名称
        worksheet.write(1, 0, company.text)

        #写入助理名称到excel
        for list1 in zhuliName:
            print("助理名称	：", list1.text)
            worksheet.write(zhuliName.index(list1) + 1, 1, list1.text)

        # 写入群组总数到excel
        for list2 in loginActive:
            print("助理登录状态：", list2.text)
            worksheet.write(loginActive.index(list2) + 1, writindex, list2.text)
        open_mb_file_cp.save('D:\\每日助理在线情况统计.xls')

    def writeqdtest_assistant(self, writindex,openSheetName):
        zhuliName = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")  # 助理名称
        loginActive = self.driver.find_elements(By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/div/span")  # 助理在线情况
        company = self.driver.find_element(By.XPATH, "//*[@id='root']/section/header/div/div[2]/div/span[3]")  # 公司名称
        print(company.text)
        # 1、使用xlrd打开Excel
        workbook = xlrd.open_workbook("D:\\每日助理在线情况统计.xls")
        # 2、使用xlutils模块的copy复制打开的文件，并保留原格式
        open_mb_file_cp = copy.copy(workbook)
        # 3、使用下标定位的方式定位到Excel工作簿里的工作表
        worksheet = open_mb_file_cp.get_sheet(openSheetName)

        # 写入公司名称
        worksheet.write(1, 0, company.text)

        #写入助理名称到excel
        for list1 in zhuliName:
            print("助理名称	：", list1.text)
            worksheet.write(zhuliName.index(list1) + 1, 1, list1.text)

        # 写入群组总数到excel
        for list2 in loginActive:
            print("助理登录状态：", list2.text)
            worksheet.write(loginActive.index(list2) + 1, writindex, list2.text)
        open_mb_file_cp.save('D:\\每日助理在线情况统计.xls')

    #qdtest，根据日期，将助理状态写入到指定的excel中
    def writeDate_qdtest_assistant(self,writeSheetName,openSheetName):
        # 获取当前的时间以【12月21日】格式输出
        now_time = time.strftime("%y%m%d", time.localtime())
        struct_time = time.strptime(now_time, "%y%m%d")
        format_now_time = time.strftime("%m{m}%d{d}", struct_time).format(m='月', d='号')
        print("当前的日期为：", format_now_time)

        workbook = xlrd.open_workbook(r"D:\\每日助理在线情况统计.xls")
        workSheet = workbook.sheet_by_name(writeSheetName)

        firstRowDat = workSheet.row_values(0)
        print("第一行的数据为：",firstRowDat)


        for index, value in enumerate(firstRowDat):
            if format_now_time == value:
                print("调用写入到excel的方法")
                print("下标为：", index, value)
                print("OK!")
                print(index)
                self.writeqdtest_assistant(index,openSheetName)  # 调用写入数据到指定日期的方法
                break
            else:
                continue


    #wibot，根据日期，将助理状态写入到指定的excel中
    def writeDate_wibot_assistant(self,writeSheetName,openSheetName):
        # 获取当前的时间以【12月21日】格式输出
        now_time = time.strftime("%y%m%d", time.localtime())
        struct_time = time.strptime(now_time, "%y%m%d")
        format_now_time = time.strftime("%m{m}%d{d}", struct_time).format(m='月', d='号')
        print("当前的日期为：", format_now_time)

        workbook = xlrd.open_workbook(r"D:\\每日助理在线情况统计.xls")
        workSheet = workbook.sheet_by_name(writeSheetName)

        firstRowDat = workSheet.row_values(0)
        print("第一行的数据为：",firstRowDat)

        for index, value in enumerate(firstRowDat):
            if format_now_time == value:
                print("调用写入到excel的方法")
                print("下标为：", index, value)
                print("OK!")
                print(index)
                self.writeData_wibot_assistant2(index,openSheetName)  # 调用写入数据到指定日期的方法
                break
            else:
                continue