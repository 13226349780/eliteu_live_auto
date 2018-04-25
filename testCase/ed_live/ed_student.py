import unittest
from time import sleep


from common.drive import Driver, logger
from common.login import tes_login

from page_obj.base import Page
from readYaml import yl


class test_student(unittest.TestCase, Page, tes_login):
    brower = yl['t_ed_student']['browser']
    url = yl['t_ed_student']['url']

    def setUp(self):
        #self.driver = Driver(self.brower).open_browser(self.url)
        #self.test_login()
        self.t_login(self.brower, self.url)



    def tearDown(self):
        logger.info("测试完成，现在退出")
        self.driver.quit()

    def test_add(self):
        """
        sleep(2)
        a_url = yl['t_ed_student']['a_url']
        self.driver = Driver(self.brower).open_browser(a_url)
        sleep(6)
        """
