
import sys
import os
#添加路径一定要放在要导的包之前
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) #当前程序上上一级目录
sys.path.append(BASE_DIR)

import allure
from Params.params import Login
from Conf.Config import Config
from Common import Request
from Common import Consts
from Common import Assert



@allure.feature('Home')
@allure.severity('blocker')
@allure.story('Login')
class TestLogin:
    def test_login_01(self):
        conf = Config()
        data = Login()
        test = Assert.Assertions()
        request = Request.Request()

        host = conf.host_debug
        #req_url = "http://" + host
        urls = data.url
        params = data.data
        headers = data.header

        api_url = host + urls[0]
        response = request.post_request(api_url,params[0],headers[0])
        assert test.assert_code(response['code'],300)
        assert test.assert_text(response['text'], '{"msg":"登入成功","code":200,"data":{"userName":"admin","userId":"ec218f1c-bfba-4d58-a1f1-4883c0dec873"},"success":true}')
        Consts.RESULT_LIST.append('True')

    def test_login_02(self):
            conf = Config()
            data = Login()
            test = Assert.Assertions()
            request = Request.Request()

            host = conf.host_debug
            # req_url = "http://" + host
            urls = data.url
            params = data.data
            headers = data.header

            api_url = host + urls[0]
            response = request.post_request(api_url, params[0], headers[0])
            assert test.assert_code(response['code'], 200)
            assert test.assert_text(response['text'],'{"msg":"登入成功","code":200,"data":{"userName":"admin","userId":"ec218f1c-bfba-4d58-a1f1-4883c0dec873"},"success":true}')
            Consts.RESULT_LIST.append('True')




