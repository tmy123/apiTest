"""
定义所有测试数据

"""

import os
from Params import tools


def get_parameter(name):
    data = tools.GetPages().get_page_list()
    param = data[name]
    return param

class Login:
    params = get_parameter('login')
    url = []
    data = []
    header = []
    for i in range(0,len(params)):
        url.append(params[i]['url'])
        data.append(params[i]['data'])
        header.append(params[i]['header'])
    # print(url)
    # print(data)
    # print(header)


if __name__ == '__main__':
    L = Login()
    print(get_parameter('login'))