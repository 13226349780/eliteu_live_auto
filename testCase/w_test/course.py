import unittest
from time import sleep

from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.price_t_select import check
from readYaml import yl
"""
课程选项测试
登录框测试
nav内容测试（对比内容）
轮播图测试（对比内容，以及切换测试）
"""
logger = Logging("test_course").getlog()
class test_course(unittest.TestCase,Page,check):
    browser = yl['t_wc']['browser']
    url = yl['t_wc']['url']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)

    def tearDown(self):
        logger.info("测试完成，现在退出")
        self.driver.quit()
    def test_course_cli(self):
        self.click("test_course","course_cli")
        #self.driver.close()
        sleep(3)
        #获取当前网页句柄
        self.driver.switch_to.window(self.driver.window_handles[-1])
       #self.driver.switch_to_window(self.driver.window_handles[-1])
        self.click("test_course","course_login")
        self.click("test_course","login_cancel")
        #获取一组元素
        li_el = self.driver.find_elements_by_css_selector('html body nav.navbar.navbar-default.navbar-fixed-top div.container div#bs-example-navbar-collapse-1.collapse.navbar-collapse ul.nav.navbar-nav.bor-left li a')
        li_tit = []
        #将元素.textapp到list中
        for v in li_el:
           a =  v.text
           li_tit.append(a)
        print(".text数据：",li_tit)
        #去掉空
        while '' in li_tit:
            li_tit.remove('')
        print("去掉空元素：",li_tit)
        self.check_string(li_tit,yl['t_course']['li_tit'])

        #check s1
        self.click("test_course","s1")
        dinger = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[1]/div/div[2]/h1')
        self.check_string(dinger.text,yl['t_course']['dinger'])

        sleep(2)

        #check s2
        self.click("test_course", "s2")
        compete = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[2]/div/div[2]/h1')
        self.check_string(compete.text, yl['t_course']['compete'])
        sleep(2)

        # check s3
        self.click("test_course", "s3")
        s_3 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[3]/div/div[2]/h1')
        self.check_string(s_3.text, yl['t_course']['s3'])
        sleep(2)

        # check s4
        self.click("test_course", "s4")
        s_4 = self.driver.find_element_by_xpath('/html/body/div[3]/div[1]/div[4]/div/div[2]/h1')
        self.check_string(s_4.text, yl['t_course']['s4'])
        sleep(2)




