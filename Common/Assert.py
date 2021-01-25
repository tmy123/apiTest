"""
封装Assert方法
"""
from Common import Log
from Common import Consts
import json


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()

    def assert_code(self,code,expected_code):
        """
        验证返回状态吗
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.log.error('statusCode error,expected_code is %s,statusCode is %s' % (expected_code,code))
            Consts.RESULT_LIST.append('fail')
            raise

    def assert_body(self,body,body_msg,expected_msg):
        """
        验证response body 中任意属性的值
        :param body:
        :param body_msg:
        :param expected_body:
        :return:
        """
        try:
            msg = body[body_msg]
            assert msg == expected_msg
            return True
        except:
            self.log.error('Response body msg != expected_msg,expected_msg is %s,body_msg is %s' % (expected_msg,body_msg))
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_in_text(self,body,expected_msg):
        """
        验证response body 中是否包含预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            text = json.dumps(body,ensure_ascii=False)
            assert expected_msg in text
            return True

        except:
            self.log.error('Response body is not contain expected_msg,expected_msg is %s' % expected_msg)
            Consts.RESULT_LIST.append('fail')

            raise

    def assert_text(self,body,expected_msg):
        """
        验证response body中是否等于预期字符串
        :param body:
        :param expected_msg:
        :return:
        """
        try:
            assert body == expected_msg
            return True
        except:
            self.log.error('Response body != expected_msg,expected_msg is %s,body is %s' % (expected_msg,body))
            Consts.RESULT_LIST.append('fail')

            raise


if __name__ == '__main__':
    a = Assertions()
    print(a.assert_code(000,200))