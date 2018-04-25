import unittest

from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.price_t_select import check
from readYaml import yl
"""
比对目标地址，（按钮是否起作用）
"""
logger = Logging("test_use").getlog()
class test_use(unittest.TestCase,Page,check):
    browser = yl['t_wc']['browser']
    url = yl['t_wc']['url']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)

    def tearDown(self):
        logger.info("测试完成，现在退出")
        self.driver.quit()
    def test_1_use(self):
        #检查url是否正确
        self.click("t_use", "t_cli")

        self.click("t_use", "quick")
        url = self.driver.current_url
        t_url = yl["t_use"]["quick"]
        self.check_url(url, t_url, "quick")
        self.driver.back()

        self.click("t_use", "Xadmin")
        url = self.driver.current_url
        t_url = yl["t_use"]["Xadmin"]
        self.check_url(url, t_url, "Xadmin")
        self.driver.back()

        self.click("t_use", "CMS")
        url = self.driver.current_url
        t_url = yl["t_use"]["CMS"]
        self.check_url(url, t_url, "CMS")
        self.driver.back()

        self.click("t_use", "LMS")
        url = self.driver.current_url
        t_url = yl["t_use"]["LMS"]
        self.check_url(url, t_url, "LMS")
        self.driver.back()





