import unittest

from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.price_t_select import check
from readYaml import yl
"""
功能以及支持测试，比对目标地址
"""
logger = Logging("test_fun").getlog()

class test_f(unittest.TestCase,Page,check):
    browser = yl['t_wc']['browser']
    url = yl['t_wc']['url']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)
    def tearDown(self):
        logger.info('测试完成，现在退出')
        self.driver.quit()

    def test_fn(self):
        self.click("t_fun","fun")
        self.click("t_fun","free")
        url = self.driver.current_url
        t_url = yl["t_fun"]["url"]
        self.check_url(url,t_url,"free")
        self.driver.back()
        self.click("t_fun","use_now")
        url = self.driver.current_url
        t_url = yl["t_fun"]["price_url"]
        self.check_url(url,t_url,"price")
        self.driver.back()
    def test_support(self):
        self.click("t_fun","support")
        url = self.driver.current_url
        t_url = yl["t_fun"]["support_url"]
        self.check_url(url,t_url,"support")
        self.driver.back()

