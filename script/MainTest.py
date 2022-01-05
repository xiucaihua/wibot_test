import unittest
import os
from script import *
import os,time,HTMLTestRunner
import unittest
from script.Login_Test import testloginCase
from libs.ShareModules import SendEmail,GetNewReport


class MainTest():
    """执行测试类里面指定case"""
if __name__ == '__main__':
        # 第三种方式执行
    case_path = "./sripts"
    runner = unittest.TextTestRunner(verbosity=2)
    discover = unittest.defaultTestLoader.discover(case_path, pattern="*_Test.py", top_level_dir=None)
    now = time.strftime("%Y-%m-%M-%H_%M_%S", time.localtime(time.time()))
    fp = open("D:\\FramWork\\report\\" + now + ".html", "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='登录数据驱动,创建部门流程测试 ', tester="修才华",description="登录数据驱动,创建部门流程测试")
    runner.run(discover)