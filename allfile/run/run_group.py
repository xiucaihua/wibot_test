#ccoding:utf-8
import unittest
from allfile.scripts.jhtjjb_group_test import Bytjjh
from allfile.scripts.txcd_group_test import AtxcdGroup
from allfile.scripts.mergsheets_test import MergSheet
from allfile.scripts.test_data_styleGreep import StyleGreep

class Runn(unittest.TestCase):
    pass




if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(AtxcdGroup("test_1_getQDtxgjwl_Data"))
    suite.addTest(AtxcdGroup("test_2_getQDcgzs_Data"))
    suite.addTest(Bytjjh("test_3_getBytj_Data"))
    suite.addTest(Bytjjh("test_4_gethzjh_Data"))
    suite.addTest(Bytjjh("test_5_getJb_Data"))
    suite.addTest(Bytjjh("test_5_getJb_Data"))
    suite.addTest(MergSheet("test_6_mergSheet"))
    suite.addTest(StyleGreep("test_7_greepData"))
    suite.addTest(StyleGreep("test_8_setExcelStyle"))
    suite.addTest(StyleGreep("test_9_setcolsSize"))

    # 执行测试
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)