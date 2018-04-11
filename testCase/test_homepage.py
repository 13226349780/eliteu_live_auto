import unittest
from time import sleep

from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.price_t_select import check
from readYaml import yl
"""
测试切换英文按钮是否起作用，

"""
logger = Logging("test_homeoage").getlog()
class test_use(unittest.TestCase,Page,check):
    browser = yl['t_wc']['browser']
    url = yl['t_wc']['url']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)

    def tearDown(self):
        logger.info("测试完成，现在退出")
        self.driver.quit()
    def test_navinfo(self):
        self.click("test_homepage","chinese")
        self.click("test_homepage","english")
        #确认中英文按钮起作用
        e_list = self.driver.find_elements_by_css_selector('html body header.container-fluid.nav-color div.container nav.navbar.navbar-default.no-margin.nav-header div.container-fluid div#bs-example-navbar-collapse-1.collapse.navbar-collapse ul.nav.navbar-nav.navbar-left.nav-ml.nav-menu-list li.function_nav a')

        li_e = []
        # 将元素.textapp到list中
        for v in e_list:
            a = v.text
            li_e.append(a)
        # 去掉空
        while '' in li_e:
            li_e.remove('')
        self.check_string(li_e[0],yl['t_homepage']['english'])


