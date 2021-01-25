"""
封装log方法
"""

import logging
import os
import time

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning':logging.WARNING,
    'error': logging.ERROR,
    'critical':logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'

def create_file(filename):
    path = filename[0:filename.rfind('/')]  #从倒数第1个/往前取值（右向左）
    #print(path)
    if not os.path.isdir(path):  # 无文件夹时创建
        os.makedirs(path)
    if not os.path.isfile(filename):  # 无文件时创建
        fd = open(filename,mode='w',encoding='utf8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)

def remove_handler(levels):
    if levels == 'error':
        logger.addHandler(MyLog.err_handler)
    logger.addHandler(MyLog.handler)

def get_current_time():
    return time.strftime(MyLog.data,time.localtime(time.time()))


class MyLog:
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = path + '/Log/log.log'
    err_file = path + '/Log/err.log'
    logger.setLevel(LEVELS.get(level,logging.NOTSET))  #若LEVELS字典里不存在level键的值，则返回默认值logging.NOTSET
    create_file(log_file)
    create_file(err_file)
    data = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file,encoding='utf8')
    err_handler = logging.FileHandler(err_file,encoding='utf8')

    @staticmethod
    def debug(log_msg):
        set_handler('debug')
        logger.debug('[DEBUG '+ get_current_time()+']' + log_msg)
        remove_handler('debug')

    @staticmethod
    def info(log_msg):
        set_handler('info')
        logger.info('[INFO ' + get_current_time()+']' + log_msg)
        remove_handler('info')

    @staticmethod
    def warning(log_msg):
        set_handler('warning')
        logger.warning('[WARNING ' + get_current_time() + ']' + log_msg)
        remove_handler('warning')

    @staticmethod
    def error(log_msg):
        set_handler('error')
        logger.error('[ERROR ' + get_current_time() + ']' +log_msg)
        remove_handler('error')

    @staticmethod
    def critical(log_msg):
        set_handler('critical')
        logger.critical('[CRITICAL ' + get_current_time() + ']' + log_msg)
        remove_handler('critical')


if __name__ == '__main__':
    # MyLog.debug('this is debug message')
    # MyLog.info('this is info message')
    # MyLog.warning('this is warning message')
    MyLog.error('this is error message')
    # MyLog.critical('this is citical message')