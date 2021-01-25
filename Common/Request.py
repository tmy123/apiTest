"""
封装request
"""

import requests


class Request:
    def __init__(self):
        pass


    def get_request(self,url,data,header):
        """
        Get请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '{}{}'.format('http://',url)
            # print(url)
        try:
            if data is None:
                response = requests.get(url=url,headers=header)
            else:
                response = requests.get(url=url, params = data,headers=header)

        except requests.RequestException as e:
            print('{}{}'.format('RequestException url: ',url))
            print(e)
            return ()
        except Exception as e:
            print('{}{}'.format('Exception url: ',url))
            print(e)
            return ()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            print(e)
            response_dicts['body'] = ''
        response_dicts['text'] = response.text
        return response_dicts

    def post_request(self,url,data,header):
        """
        POST请求
        :param url:
        :param data:
        :param header:
        :return:
        """
        if not url.startswith('http://'):
            url = '{}{}'.format('http://', url)
            print(url)
        try:
            if data is None:
                response = requests.post(url=url,headers=header)
            else:
                response = requests.post(url=url,json=data,headers=header)

        except requests.RequestException as e:
            print('{}{}'.format('RequestException url: ', url))
            print(e)
            return ()
        except Exception as e:
            print('{}{}'.format('Exception url: ', url))
            print(e)
            return()

        response_dicts = dict()
        response_dicts['code'] = response.status_code
        try:
            response_dicts['body'] = response.json()
        except Exception as e:
            response_dicts['body'] = ''
        response_dicts['text'] = response.text

        return response_dicts


if __name__ == '__main__':
    R = Request()
    R.post_request('39.105.34.24:8888/apis/login',{'userName':'admin','password':123456},'')
