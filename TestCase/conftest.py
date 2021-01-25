import sys
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录
sys.path.append(BASE_DIR)

# print(os.path.abspath(__file__)) #这才是当前程序绝对路径
# print(os.path.dirname(os.path.abspath(__file__))) #当前程序上一级目录，其中dirname返回目录名，不要文件名
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))#当前程序上上一级目录

import allure
import pytest
from Conf.Config import Config
from Common import Consts


@pytest.fixture()
def action():
    #定义环境
    env = Consts.API_ENVIRONMENT_DEBUG
    # 定义报告中的environment
    conf = Config()
    host = conf.host_debug
    tester = conf.tester_debug
    allure.environment(environment = env)
    allure.environment(hostname = host)
    allure.environment(tester= tester)

    return env


