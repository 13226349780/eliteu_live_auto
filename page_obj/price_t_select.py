from common import logger
from readYaml import yl
from testFile.config import config_element

from common.logger import Logging
logger = Logging("price_test").getlog()
class check():
    def __init__(self,driver,Page):
        self.driver = driver
    #check element
    def check_element(self,ft,af):

        self.click(ft[0],ft[1])
        css_click = config_element[af[0]][af[1]]
        # print(css_50[1])
        # 获取元素属性
        # ic_50 = self.driver.find_element_by_css_selector(css_50[1]).get_attribute("id")
        # 尝试重新点击50选项
        try:
            self.driver.find_element_by_css_selector(css_click[1]).click()
            logger.info("选择%s成功"%af[1])
            #print(11111111111111111111111111111111111)
        except:
            logger.info("选择%s失败"%af[1])

    def check_url(self,now_url,target_url,fun):
        now_url = now_url.split('/')
        target_url = target_url.split('/')

        try:
            assert now_url[-2] == target_url[-2]
            logger.info('%s btn is good'%fun)
        except:
            logger.info('%s fun is error'%fun)
    def check_string(self,now_string,real_string):
        try:
            assert now_string ==real_string
            logger.info('%s info is good'%now_string)
        except:
            logger.info('%s info is error'%now_string)


