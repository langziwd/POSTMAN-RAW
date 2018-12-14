import unittest
from auto_driver.AutoDriver import AutoDriver


class AppLogin(unittest.TestCase):
    def setUp(self):
        self.s = AutoDriver()

    def tearDown(self):
        self.s.quit()

    def testpost(self):
        # 从row中解析URL,DATA,HEADERS
        # file = open('..//data/row.csv', 'r', encoding='utf8')
        # data = file.read()

        # end1 = data.index('\n')
        # url = data[:end1]
        # url = url.split(' ')
        # url = url[1]

        # list_data = data.split('\n')
        # data = eval(list_data[-1])

        # headers = list_data[1:-2]
        # i = 0
        # dict3 = {}
        # for n in headers:
        #     dict1 = {headers[i].split(':')[0]: headers[i].split(':')[1][1:]}
        #     dict3.update(dict1)
        #     i += 1
        # headers = dict3
        # file.close()
        dict_row = self.s.get_row('..//data/row.csv')
        url = dict_row['url']
        headers = dict_row['headers']
        data = dict_row['data']


        # 发起请求
        r = self.s.post(url, headers, data)

        # # 断言
        expected = 0
        actual = r.json()['status']  # 获取响应的字段
        self.assertEqual(expected, actual, msg='失败原因：%s != %s' % (expected, actual))

    def testget(self):
        dict_row = self.s.get_row('..//data/getrow.csv')
        url = dict_row['url']
        headers = dict_row['headers']
        data = dict_row['data']

        r = self.s.get(url,headers,data)

