#coding:utf-8
import logging

# logging.basicConfig(level=logging.INFO,format='%(asctime)s,%(levelname)s,%(message)s,%(lineno)d')
# sh = logging.FileHandler(filename='../log/test.log',encoding='utf-8')
# logger = logging.getLogger()
# logger.addHandler(sh)

import logging
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
handler = logging.FileHandler("test.log",encoding='utf-8')
console = logging.StreamHandler()
handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
console.setFormatter(formatter)
logger.addHandler(console)
logger.addHandler(handler)


