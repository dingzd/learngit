# -*- coding:utf-8 -*-
import unittest
import time
import ddt
from selenium import webdriver

@ddt.ddt
class BaiduLogin(unittest.TestCase):
    def setUp(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=self.option)


    @ddt.data(("tyindon", "007zadxd8095@"))
    @ddt.unpack
    def test_login(self, userName, passWord):
        self.url = "https://www.baidu.com"
        try:
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)
            self.driver.find_element_by_xpath("//*[@id='u1']/a[7]").click()
            time.sleep(2)
            self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__footerULoginBtn']").click()
            self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__userName']").send_keys(userName)
            self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__password']").send_keys(passWord)
            #手动输入验证码
            time.sleep(20)
            self.driver.find_element_by_xpath("//*[@id='TANGRAM__PSP_10__submit']").click()
            self.assertEqual(self.driver.find_element_by_xpath("//*[@id='s_username_top']/span").text,"tyindon",u"登录失败")
        except Exception as e:
            print(e)
    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()







