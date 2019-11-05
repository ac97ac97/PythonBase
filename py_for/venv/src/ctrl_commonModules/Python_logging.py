# logging
import logging

# logging.basicConfig(level=logging.DEBUG)
# logging.debug('这是debug信息')
# logging.info('这是info信息')
# logging.warning('这是warning信息')
# logging.error('这是error信息')
# logging.critical('这是critical信息')


# logging.basicConfig(level=logging.DEBUG)
# logger = logging.getLogger(__name__)
# logger.debug('这是debug信息')
# logger.info('这是info信息')
# logger.warning('这是warning信息')
# logger.error('这是error信息')
# logger.critical('这是critical信息')

# 日志格式信息化
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(threadName)s -'
#                            '%(name)s - %(funcName)s - %(levelName)s - %(message)s')
# logger = logging.getLogger(__name__)
#
# logger.debug('这是debug信息')
# logger.info('这是info信息')
# logger.warning('这是warning信息')
# logger.error('这是error信息')
# logger.critical('这是critical信息')
#
#
# def funlog():
#     logger.info("进入funlog函数")
#
#
# logger.info("调用funlog函数")
# funlog()

#日志重定位
# logging.basicConfig(level=logging.INFO,
#                     format='%(asctime)s - %(threadName)s - '
#                            '%(name)s - %(funcName)s - %(levelName)s - %(message)s',
#                     filename='test.log')
# logger = logging.getLogger(__name__)
#
# logger.debug('这是debug信息')
# logger.info('这是info信息')
# logger.warning('这是warning信息')
# logger.error('这是error信息')
# logger.critical('这是critical信息')
#
#
# def funlog():
#     logger.info("进入funlog函数")

# logger.info("调用funlog函数")
# funlog()


#使用配置文件
import logging.config
logging.config.fileConfig("logger.conf")
logger= logging.getLogger('logger1')
logger.debug('这是debug信息')
logger.info('这是info信息')
logger.warning('这是warning信息')
logger.error('这是error信息')
logger.critical('这是critical信息')

def funlog():
    logger.info("进入funlog函数")

logger.info("调用funlog函数")
funlog()