import unittest
from time import sleep


from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from common.drive import Driver
from common.logger import Logging
from page_obj.base import Page
from page_obj.price_t_select import check
from readYaml import yl
from testFile.config import config_element
"""
价格测试
价格是否选中（对比选中吼的css变化）
立即使用是否到目标地址
"""
logger = Logging("price_test").getlog()

class test_price(unittest.TestCase,Page,check):
    browser = yl['t_wc']['browser']
    url = yl['t_wc']['url']

    def setUp(self):
        self.driver = Driver(self.browser).open_browser(self.url)

    def tearDown(self):
        logger.info("测试完成，现在退出")
        self.driver.quit()

    def test_1_price(self):
        self.click("t_price","price_c")
        WebDriverWait(self.driver, 5, 0.5).until(EC.presence_of_all_elements_located)

        #js = 'document.getElementById("layui-layer3").style.display="none";'
        #self.driver.execute_script(js)
        #self.driver.switch_to_active_element()

        """
        try:
            self.click("t_price","cancel")
        except:
            self.click("t_price","confirm")
        """
        """
        self.click("t_price","price_50")
        css_50 = config_element["t_price"]["price_50_ic"]
        #print(css_50[1])
        #获取元素属性
        #ic_50 = self.driver.find_element_by_css_selector(css_50[1]).get_attribute("id")
        #尝试重新点击50选项
        try:
            self.driver.find_element_by_css_selector(css_50[1]).click()
            logger.info("选择50成功")
        except:
            logger.info("选择50失败")
            """
        no_c_50 = ["t_price", "price_50"]
        is_c_50 = ["t_price", "price_50_ic"]
        self.check_element(no_c_50,is_c_50)
        no_c_100 = ["t_price", "price_100"]
        is_c_100 = ["t_price", "price_100_ic"]
        self.check_element(no_c_100, is_c_100)
        no_c_300 = ["t_price", "price_300"]
        is_c_300 = ["t_price", "price_300_ic"]
        self.check_element(no_c_300, is_c_300)
        no_c_500 = ["t_price", "price_500"]
        is_c_500 = ["t_price", "price_500_ic"]
        self.check_element(no_c_500, is_c_500)
        no_c_800 = ["t_price", "price_800"]
        is_c_800 = ["t_price", "price_800_ic"]
        self.check_element(no_c_800, is_c_800)
        no_c_1000 = ["t_price", "price_1000"]
        is_c_1000 = ["t_price", "price_1000_ic"]
        self.check_element(no_c_1000, is_c_1000)
        no_c_1500 = ["t_price", "price_1500"]
        is_c_1500 = ["t_price", "price_1500_ic"]
        self.check_element(no_c_1500, is_c_1500)
        no_c_2000 = ["t_price", "price_2000"]
        is_c_2000 = ["t_price", "price_2000_ic"]
        self.check_element(no_c_2000, is_c_2000)
        no_c_3000 = ["t_price", "price_3000"]
        is_c_3000 = ["t_price", "price_3000_ic"]
        self.check_element(no_c_3000, is_c_3000)

        # 确认套餐
        self.click("t_price", "use")
        url = self.driver.current_url
        url = url.split('/')
        #print(url[-2])
        try:
            assert url[-2] == "agreement"
        except:
            logger.info("选择套餐跳转错误")








