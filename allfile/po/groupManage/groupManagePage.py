#coding:utf-8
from allfile.po.BasePage import BasePage
from selenium.webdriver.common.by import By

class GroupManagePage(BasePage):

    groupName = (By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[2]/span")    # 群组名称
    memberCount = (By.XPATH,"//*[@id='root']/section/section/main/div[2]/div[2]/div/div/div/div/div/div/div/table/tbody/tr/td[7]/span")  # 群组总人数
    company =(By.XPATH, "//*[@id='root']/section/header/div/div[2]/div/span[3]")                                                         # 公司名称


    """
    获取到全部的群名称
    :return groupName 群名称
    """
    def get_groupName(self):
        groupName= self.driver.find_elements(*self.groupName)
        return groupName

    """
    获取到全部的在群人数
    :return memberCount 群在群人数
    """
    def get_memberCount(self):
         memberCount=self.driver.find_elements(*self.memberCount)
         return memberCount

    """
      获取到公司名称
      :return company 公司名称
      """
    def get_company(self):
        return self.driver.find_element(*self.company)
        #return company