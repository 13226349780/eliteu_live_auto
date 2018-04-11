import os
from selenium import webdriver

from common.logger import Logging
from page_obj.base import Page

logger = Logging("Driver").getlog()
class Driver():
    """选择加载浏览器的驱动"""
    dir = os.path.dirname(os.path.abspath(''))  # 注意相对路径获取方法
    firefox_driver_path = dir+ '/driver/geckodriver'
    chrome_driver_path = dir + '/driver/chromedriver'
    #ie_driver_path = dir + '/driver/IEDriverServer.exe'
    def __init__(self,driver,time = 15):
        self.driver = driver
        self.time = time

    def open_browser(self,url):
        """打开浏览器"""
        if self.driver == "Firefox" or self.driver == "firefox":
            self.browser = webdriver.Firefox()
            self.browser.get(url)
            logger.info("打开火狐浏览器")
        if self.driver == "Chrome":
            #self.browser = webdriver.Chrome(self.chrome_driver_path)
            self.browser = webdriver.Chrome()
            self.browser.get(url)
            #telttopet(url)
            logger.info("打开谷歌浏览器")
        #if self.driver == "IE":
            #self.browser = webdriver.Ie(self.ie_driver_path)
            #logger.info("打开IE浏览器")
        self.browser.implicitly_wait(self.time)
        logger.info("隐式等待元素时间为：{}".format(self.time))
        return  self.browser

if __name__ == '__main__':
    dir = os.path.dirname(os.path.abspath(''))  # 注意相对路径获取方法
    print(dir,"dir")