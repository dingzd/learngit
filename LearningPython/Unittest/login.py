# -*- coding:utf-8 -*-
from selenium import webdriver
import unittest,time
import ddt


@ddt.ddt
class Login(unittest.TestCase):
    def setUp(self):
        self.option = webdriver.ChromeOptions()
        self.option.add_argument('disable-infobars')
        self.driver = webdriver.Chrome(chrome_options=self.option)

    @ddt.data(("18600000002","123456"))
    @ddt.unpack
    def test_login(self,phone,password):
        url = "https://www.htxksport.com"
        self.driver.get(url)
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)
        try:
            self.driver.find_element_by_link_text("登录").click()
            self.driver.find_element_by_xpath("//*[@id='__nuxt']/div[2]/div[2]/div[2]/div/form/div[3]/div/div[1]/input").send_keys(
            phone)
            self.driver.find_element_by_xpath("//*[@id='__nuxt']/div[2]/div[2]/div[2]/div/form/div[4]/div/div/div/input").send_keys(
            password)
            self.driver.find_element_by_xpath("//*[@id='__nuxt']/div[2]/div[2]/div[2]/div/form/div[5]/div/button").click()
            # self.assertTrue(expactdata in self.driver.page_source)
            self.assertTrue(self.driver.find_element_by_link_text("资讯"))
        except Exception as e:
            print(e)


    def tearDown(self):
        self.driver.close()

if __name__=='__main__':
    unittest.main()
