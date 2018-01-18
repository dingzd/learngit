# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest,time
import ddt


@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(("18600000002","123456"))
    @ddt.unpack
    def test_login(self,phone,password):
        url = "https://www.htxksport.com"
        self.driver.get(url)
        time.sleep(3)
        self.driver.maximize_window()

        self.driver.implicitly_wait(5)

        self.driver.find_element_by_link_text("登录").click()
        self.driver.find_element_by_id("el-input-group--prepend").send_keys(phone)


    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
