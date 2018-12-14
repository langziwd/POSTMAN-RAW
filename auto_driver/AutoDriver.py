import json
import unittest
import requests


class AutoDriver(object):
    # 定义属性
    def __init__(self):
        self.s = requests.session()
        self.base_url = 'http://192.168.3.53'

    # post
    def post(self, url, headers, data):
        r = self.s.post(url=self.base_url + url, headers=headers, json=data, verify=False)
        print('状态码：', r.status_code,
              '\n请求参数：', data,
              '\n响应字段：', dict(r.json()).keys(),
              '\n响应全文：', r.json(),
              '\ncookies：', r.cookies)
        return r

    # get
    def get(self, url, headers, data):
        r = self.s.get(url=self.base_url + url, headers=headers, params=data, verify=False)

        print('状态码：', r.status_code,
              '\n请求参数：', data,
              '\n响应字段：', dict(r.json()).keys(),
              '\n响应全文：', r.json())
        if '<RequestsCookieJar[]>' in r.cookies:
            cookies = 'no cookies'
            print('\ncookies：', cookies)
        else:
            print('\ncookies：', r.cookies)
        return r

    # quit
    def quit(self):
        self.s.close()

    # 读取CSV文件数据驱动
    def redcsv(self, path, r):
        file = open(path, r, encoding='utf8')
        data = file.readline()
        file.close()
        return data

    def get_row(self, row_path):
        # 从row中解析URL,DATA,HEADERS
        file = open(row_path, 'r')
        data = file.read()

        end1 = data.index('\n')
        url = data[:end1]
        url = url.split(' ')
        url = url[1]

        list_data = data.split('\n')
        data = list_data[-1]

        headers = list_data[1:-2]
        i = 0
        dict3 = {}
        for n in headers:
            dict1 = {headers[i].split(':')[0]: headers[i].split(':')[1]}
            dict3.update(dict1)
            i += 1
        headers = dict3
        file.close()

        dict_row = {'url':url,
                    'data':data,
                    'headers':headers}

        return dict_row
