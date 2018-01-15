# -*- coding:utf-8 -*-
__auth__ = 'dingxd'
import unittest
from ddt import ddt,unpack,data
import requests
import sys

@ddt
class Articles(unittest.TestCase):
    def setUp(self):
        self.base_url = "http://m.htxk.com/api/v1/article/article"

    def tearDown(self):
        print(self.result)

    # @data(({'articleId':'435'}),({'articleId':'438'}))
    # @unpack
    def test_article_article(self):
        u"""获取资讯，资讯ID不为空"""
        r = requests.get(self.base_url,params={'articleId':'435'})
        self.result = r.json()
        self.assertEqual(self.result['data']['userId'],'hhly92279')


if __name__=='__main_':
    unittest.main()



