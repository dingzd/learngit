#!usr/bin/env python
#-*-coding:utf-8-*-
__author__ = 'dingzd'

from selenium import webdriver
import unittest,time
import logging,traceback
import ddt
from selenium.common.exceptions import NoSuchElementException

# 初始化日志对象
logging.basicConfig(
    #日志级别
    level=logging.INFO,
    #日志格式
    #时间、代码所在文件名、代码行号、日志级别名字、日志信息
    format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)s %(message)s',
    #打印日志的时间
    datefmt='%Y-%m-%d %Y %H:%M:%S',
    #日志文件存放的目录及日志文件名
    filename='report.log',
    #打开日志文件的方式
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data((u"神奇动物在哪里",u"叶茨"),
              (u"疯狂动物城",u"古德温"),
              (u"大话西游之月光宝盒",u"周星驰")
              )
    @ddt.unpack
    def test_dataDriverByObj(self,testdata,expectdata):
        url = "https://www.baidu.com"
        self.driver.get(url)
        self.driver.implicitly_wait(5)#设置隐式等待时间为5S
        try:
            self.driver.find_element_by_id("kw").send_keys(testdata)
            self.driver.find_element_by_id("su").click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException:
            logging.error(u"查找的页面元素不存在，异常堆栈信息：" + str(traceback.format_exc()))
        except AssertionError:
            logging.error(u"搜索 %s， 期望 %s， 失败" %(testdata,expectdata))
        else:
            logging.info(u"搜索 %s， 期望 %s， 通过" %(testdata,expectdata))

    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()