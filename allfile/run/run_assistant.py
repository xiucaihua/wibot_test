#ccoding:utf-8
import unittest

from allfile.scripts.mergsheets_test import MergSheet
from allfile.scripts.test_data_styleGreep import StyleGreep
from allfile.scripts.jhtjjbhf_assistant_test import BJJHCQ_assistant
from allfile.scripts.txcd_assistant_test import ATxCd_assistant

class RunAssistant(unittest.TestCase):
    pass

if __name__ == "__main__":
    # 构造测试套件
    suite = unittest.TestSuite()
    suite.addTest(ATxCd_assistant("test_1_txwl_login"))
    suite.addTest(ATxCd_assistant("test_2_cdzs_login"))
    suite.addTest(BJJHCQ_assistant("test_3_jh_login"))
    suite.addTest(BJJHCQ_assistant("test_4_bytj_login"))
    suite.addTest(BJJHCQ_assistant("test_5_cqhc_login"))
    suite.addTest(BJJHCQ_assistant("test_6_cqhf_login"))
    suite.addTest(MergSheet("test_mergAssistantSheet"))
    suite.addTest(StyleGreep("test_zassistant_setExcelStyle"))
    suite.addTest(StyleGreep("test_zassistant_setcolsSize"))

    # 执行测试
    runner = unittest.TextTestRunner()
    runner.run(suite)
