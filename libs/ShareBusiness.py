#coding:utf-8
from Po.login_page.LoginPage import LoginPage
from time import sleep

# -------------------------------------------------------------------------------
# 函数/过程名称：login_B
# 函数/过程的目的：登录业务函数
# 假设：无
# 影响：无
# 输入：无
# 返回值：无
# 创建者：修才华
# 创建时间：2021/11/10
# 修改者：
# 修改原因：
# 修改时间:
# -------------------------------------------------------------------------------

def login_B(username,password):
    obj = LoginPage()
    obj.open_url()
    obj.set_username(username)
    obj.set_password(password)
    obj.click_login_button()
    sleep(1)
    return obj.dr