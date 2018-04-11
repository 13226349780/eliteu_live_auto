import unittest

from selenium.webdriver.support import expected_conditions as EC


from selenium.webdriver.support.wait import WebDriverWait

from common.drive import Driver
from common.function import Excel, Random
from common.logger import Logging
from page_obj.base import Page


from readYaml import yl
"""
登录测试


"""

logger = Logging("wel_LoginTest").getlog()
class test_click(unittest.TestCase,Page,Random):
    url = yl['t_wc']['url']
    browser = yl['t_wc']['browser']
    real_title = yl['t_wc']['real_title']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)
        #self.open(self.url)
    def tearDown(self):
        logger.info('测试完成，现在退出')
        self.driver.quit()
    def test_1_click(self):
        logger.info('点击一下click click')
        self.click("w_login","宣传登陆")
        WebDriverWait(self.driver,5,0.5).until(EC.presence_of_all_elements_located)
        # 空空如也
        self.click("w_login", "confirm")
        null = self.driver.find_element_by_class_name('mistack').text
        try:
            assert null == yl['t_wc']['null']
        except:
            logger.info("不输入密码和账号时提示错误")

        #只输入密码
        #pw = self.get_random_number([1,10])
        pw = yl['t_wc']['password']
        self.send_keys("w_login", "pw_input", pw)
        self.click("w_login", "confirm")
        #pw_h = self.find_element("w_login","hint_np")
        pw_h = self.driver.find_element_by_class_name('mistack').text
        #url_now = self.driver.current_url
        try:
            assert pw_h == yl['t_wc']['nn_tips']
        except:
            logger.info("只输入密码是提示错误")
        #print(pw_h)

        #只输入账号
        c_pw=self.find_element("w_login","pw_input").clear()
        ua = yl['t_wc']['username']
        self.send_keys("w_login","un_input",ua)
        self.click("w_login", "confirm")
        un_h = self.driver.find_element_by_class_name('mistack').text
        #print(un_h)
        try:
            assert un_h == yl['t_wc']['np_tips']
        except:
            logger.info("只输入账号时提示错误")
        #正常登录
        self.send_keys("w_login","un_input",ua)
        self.send_keys("w_login","pw_input",pw)
        self.click("w_login","confirm")
        title = self.driver.title
        url_now = self.driver.current_url
        print(url_now)
        #print(title)
        logger.info('title is : %s' %title)
        assert url_now == yl['t_wc']['n_url']


















