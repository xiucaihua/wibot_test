#coding:utf-8

import unittest
from script.testall import TestAll
from script.testall2 import TestAll2
class RunAll(unittest.TestCase):
    pass


if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(TestAll('test_getQDtxgjwl_Data'))
    suite.addTest(TestAll('test_getQDcgzs_Data'))
    suite.addTest(TestAll2('test_getBytj_Data'))
    suite.addTest(TestAll2('test_gethzjh_Data'))