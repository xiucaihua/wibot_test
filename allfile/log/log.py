#coding:utf-8
import logging
fromatter=('%(asctime)s - %(name)s -%(lineno)d %(levelname)s - %(message)s')
logging.basicConfig(filename='test.log',level=logging.INFO,format=fromatter)
consolog=logging.StreamHandler()
consolog.setFormatter(logging.Formatter(fromatter))
logging.getLogger().addHandler(consolog)  #输出到StreamHandler里面
#
# logging.info('info massage')
# logging.error('error massage')
# logging.warning('warning massage')
# logging.critical('critical massage')