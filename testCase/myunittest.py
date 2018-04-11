import unittest

from selenium.webdriver.chrome import webdriver

from common.drive import Driver
from common.function import Excel
from page_obj.loginPage import Login
from readConfig import ReadConfig

config = ReadConfig()


class loginTest(unittest.TestCase):
    """继承unnittest,获取EXCEL表数据，或者插入数据"""

    url = config.getConfig("url")
    browser = config.getConfig("browser")
    def get_excel_data(self, dataname, row=2):
        data = Excel(dataname)
        return data.read_excel(row)

    def set_excel_data(self, dataname, datas=[], row=2):
        excel_data = Excel(dataname)
        excel_data.write_excel(datas, row)

    """登录页面"""
    def setUp(self):
        driver = Driver(self.browser).open_browser()
        #driver = webdriver.Chrome()
        self.login = Login(driver)
        self.login.open(self.url)
        self.AssertionError = []
    def tearDown(self):
        self.login.quit()
        self.assertEqual([], self.AssertionError)

