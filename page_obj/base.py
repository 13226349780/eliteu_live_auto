import time

import os
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

from testFile.config import config_element
from common.logger import Logging

logger = Logging("Page").getlog()
class Page():
    #初始化
    def __init__(self,driver):
        self.driver = driver

    #单个元素定位
    def find_element(self,page,element):
        try:
            el = config_element[page][element]
            type = el[0]
            value = el[1]
            if type == "ID" or type == "id" or type == "Id":
                try:
                    find_element = self.driver.find_element_by_id(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素ID为：{}@".format(value))
                    raise e
            elif type == "NAME" or type == "name" or type == "Name":
                try:
                    find_element = self.driver.find_element_by_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素NAME为：{}的元素@".format(value))
                    raise e
            elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
                try:
                    find_element = self.driver.find_element_by_class_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素CLASSNAME为：{}的元素@".format(value))
                    raise e
            elif type == "TAGNAME" or type == "tagname" or type == "TagName":
                try:
                    find_element = self.driver.find_element_by_tag_name(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素TAGNAME为：{}的元素@".format(value))
                    raise e
            elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
                try:
                    find_element = self.driver.find_element_by_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素LINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
                try:
                    find_element = self.driver.find_element_by_partial_link_text(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素PARTIALLINKTEXT为：{}的元素@".format(value))
                    raise e
            elif type == "XPATH" or type == "xpath" or type == "XPath":
                try:
                    find_element = self.driver.find_element_by_xpath(value)
                    return find_element
                except NoSuchElementException as e:
                    logger.error("@未发现元素XPATH为：{}的元素@".format(value))
                    raise e
            elif type == "CSS" or type == "css" or type == "Css":
                try:
                    find_element = self.driver.find_element_by_css_selector(value)
                    return find_element
                except Exception as e:
                    logger.error("@未发现元素CSS为：{}的元素@".format(value))
                    logger.error(e)
                    raise e
            else:
                error = "@{}模块下{}元素类型参数错误！@".format(page, element)
                logger.error(error)

        except KeyError as e:
            logger.error("@加载{}模块{}元素不匹配@".format(page, element))
            logger.error(e)
            raise e


    def find(self,element):

        type = element[0]
        value = element[1]
        find_element = ""
        if type == "ID" or type == "id" or type == "Id":
            try:
                find_element = self.driver.find_element_by_id(value)
            except NoSuchElementException as e:
                logger.error("未发现元素ID为：{}".format(value))
        elif type == "NAME" or type == "name" or type == "Name":
            try:
                find_element = self.driver.find_element_by_name(value)
                logger.info("加载NAME为：{}的元素".format(value))
            except NoSuchElementException as e:
                logger.error("未发现元素NAME为：{}的元素".format(value))
        elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
            try:
                find_element = self.driver.find_element_by_class_name(value)
            except NoSuchElementException as e:
                logger.error("未发现元素CLASSNAME为：{}的元素".format(value))
        elif type == "TAGNAME" or type == "tagname" or type == "TagName":
            try:
                find_element = self.driver.find_element_by_tag_name(value)
            except NoSuchElementException as e:
                logger.error("未发现元素TAGNAME为：{}的元素".format(value))
        elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
            try:
                find_element = self.driver.find_element_by_link_text(value)
            except NoSuchElementException as e:
                logger.error("未发现元素LINKTEXT为：{}的元素".format(value))
        elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
            try:
                find_element = self.driver.find_element_by_partial_link_text(value)
            except NoSuchElementException as e:
                logger.error("未发现元素PARTIALLINKTEXT为：{}的元素".format(value))
        elif type == "XPATH" or type == "xpath" or type == "XPath":
            try:
                find_element = self.driver.find_element_by_xpath(value)
            except NoSuchElementException as e:
                logger.error("未发现元素XPATH为：{}的元素".format(value))
        elif type == "CSS" or type == "css" or type == "Css":
            try:
                find_element = self.driver.find_element_by_css_selector(value)
            except NoSuchElementException as e:
                logger.error("未发现元素CSS为：{}的元素".format(value))
        else:
            error = "{}类型下{}元素类型参数错误！".format(type,value)
            logger.error(error)
        return find_element

    def title(self):
        self.wait_time(0.5)
        title = self.driver.title
        logger.info("获取页面的title : %s"  %title)
        return  title

    def finds(self,elements):
        type = elements[0]
        value = elements[1]
        if type =="css" or type =="Css" or type =="CSS":
            elements  = self.driver.find_elements_by_css_selector(value)
        else:print("暂时不支持其他元素定位")
        return elements
    #css多元素定位
    # def find_elements(self,page,elements):
    #     el = element_config[page][elements]
    #     print("el",el)
    #     type = el[0]
    #     value = el[1]
    #     if type =="css" or type =="Css" or type =="CSS":
    #         elements  = self.driver.find_elements_by_css_selector(value)
    #     else:print("暂时不支持其他元素定位")
    #     return elements

    #点击事件
    def click(self,page,element):
        logger.info("点击{}下的{}按钮".format(page, element))
        el = self.find_element(page,element)
        el.click()
        self.wait_time(1)

    #获取元素文本信息
    def text(self,page,element):
        text = self.find_element(page, element).text
        logger.info("获取{}下的{}文本信息：{}".format(page, element,text))
        self.wait_time(0.5)
        return text

    def get_url(self):
        """获取当前页面的URL"""
        return self.driver.current_url

    def get_title(self):
        """获取当前页面的URL"""
        return self.driver.title

    #清空输入框，然后输入VALUE
    def send_keys(self,page,element,value):
        self.wait_time(0.8)
        self.find_element(page,element).clear()
        self.find_element(page,element).send_keys(value)


    # 下拉选择框
    def select(self, page, element, index):
        Select(self.find_element(page, element)).select_by_index(index)


    #内嵌框架进行切换
    def iframe(self,page,element):
        self.wait_time(1)
        self.driver.switch_to.frame(self.find_element(page,element))

    #鼠标事件
    def action(self):
        self.wait_time(1)
        action = ActionChains(self.driver)
        return action

    #鼠标悬停
    def move(self,page,element):
        try:
            el = self.find_element(page, element)
            self.wait_time(0.5)
            self.action().move_to_element(el).perform()
        except Exception as e:
            logger.error("鼠标没有能正常悬停在 {} 的 {} 上".format(page, element))
            logger.error(e)
        self.wait_time(0.5)

    # 根据元素属性获取元素值
    def element_type_value(self, page, element, name="placeholder"):
        attribute = self.find_element(page, element).get_attribute(name)
        self.wait_time(0.5)
        return  attribute



    """对浏览器的一些操作--------------------------------------"""

    def open(self,url):
        """打开网页"""
        self.driver.get(url)
        logger.info("浏览器中输入域名：%s" %url)


    def close(self):
        """关闭当前网页"""
        self.driver.close()
        logger.info("关闭当前页面")


    def quit(self):
        """关闭浏览器"""
        self.driver.quit()
        logger.info("关闭浏览器")


    def wait_time(self, wait_time):
        """强制等待元素加载时间"""
        time.sleep(wait_time)


    def window(self, page='new_page'):
        """窗口定位切换"""
        # 获取全部打开网页的句柄
        handles = self.driver.window_handles
        lens = len(handles)
        if page == "new_page":
            if lens != 1:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[-1])
            else:
                self.wait_time(0.5)
                self.driver.switch_to.window(handles[0])
        elif page == "superior_page":
            self.wait_time(0.5)
            self.driver.switch_to.window(handles[-2])
        else:
           logger.error("@切换窗口参数错误@")
        self.wait_time(1)

    #页面 后退：-1 ，刷新当前页：0 ，前进：1
    def browser_page_handle(self,type ="-1"):
        if type == "-1":
            self.wait_time(0.5)
            self.driver.back()
        elif type == "0":
            self.wait_time(0.5)
            self.driver.refresh()
        elif  type == "1":
            self.wait_time(0.5)
            self.driver.forward()
        else:
            logger.error("页面前进后退，操作参数错误！")
        self.wait_time(1)
    #调节浏览器窗口大小
    def window_sizi(self,width =400,height=400):
        self.wait_time(0.5)
        self.driver.set_window_size(width,height)
        self.wait_time(0.5)

    def window_max(self):
        self.driver.maximize_window()

    # javascript
    def javascript(self, js):
        try:
            self.driver.execute_script(js)
        except Exception as e:
            logger.error("@JS加载错误:%s@" %e)


    # 调节浏览器滚动条
    def page_location(self,down = 0,right = 0):
        if str.isnumeric(down) and str.isnumeric(right):
            size = "window.scrollTo({},{})".format(down, right)
        else:
            logger.error("@加载浏览器的滚动条位置参数{}{}不是数字！@".format(down, right))
        self.javascript(size)
        self.wait_time(1)

    def get_windows_img(self,Fail=""):
        """
        在这里我们把file_path这个参数写死，直接保存到我们项目根目录的一个文件夹.\Screenshots下
        """
        file_path = os.path.dirname(os.path.abspath('.')) + '/report/image/'
        rq = time.strftime('%m%d%H%M', time.localtime(time.time()))
        screen_name = file_path + rq +Fail+ '.png'
        try:
            self.wait_time(1)
            self.driver.get_screenshot_as_file(screen_name)
            logger.info("页面截图保存在 :/report/image/")
        except NameError as e:
            logger.error("@页面截图保存发生错误! %s@" % e)

    def get_location(self,page,element):
        list = []
        el = self.find_element(page,element)
        location  = el.location
        list.append(location)
        size = el.size
        list.append(size)
        return list

    def get_relative_location(self,elementA,elementB):

        locationA = self.get_location(*elementA)
        xA = locationA[0]["x"]
        yA = locationA[0]["y"]
        heightA = locationA[1]["height"]
        widthA = locationA[1]["width"]
        locationB = self.get_location(*elementB)
        xB = locationB[0]["x"]
        yB = locationB[0]["y"]
        heightB = locationB[1]["height"]
        widthB = locationB[1]["width"]
        list=  []
        zuo = xB - xA
        shang = yB  - yA
        you = (widthB+xB)-(widthA+xA)
        xia = (heightA+yA)- (heightB+yB)
        list.append(zuo)
        list.append(shang)
        list.append(you)
        list.append(xia)
        return list
    """对元素的判断返回  True,False--------------------------------------"""
    def is_displayed(self, page, element):
        """判断元素是否可见"""
        dis = self.find_element(page, element).is_displayed()
        logger.info("{}模块下的{}元素可见性为：{}".format(page, element,dis))
        return dis

    def isElementExist(self, page, element,time=2):
        """判断元素是否存在"""
        try:
            el = config_element[page][element]
            type = el[0]
            value = el[1]
            if type == "ID" or type == "id" or type == "Id":
                    find_element = self.driver.find_element_by_id(value)
            elif type == "NAME" or type == "name" or type == "Name":
                    find_element = self.driver.find_element_by_name(value)
            elif type == "CLASSNAME" or type == "classname" or type == "ClassName":
                    find_element = self.driver.find_element_by_class_name(value)
            elif type == "TAGNAME" or type == "tagname" or type == "TagName":
                    find_element = self.driver.find_element_by_tag_name(value)
            elif type == "LINKTEXT" or type == "linktext" or type == "LinkText":
                    find_element = self.driver.find_element_by_link_text(value)
            elif type == "PARTIALLINKTEXT" or type == "partiallinktext" or type == "PartialLinkText":
                    find_element = self.driver.find_element_by_partial_link_text(value)
            elif type == "XPATH" or type == "xpath" or type == "XPath":
                    find_element = self.driver.find_element_by_xpath(value)
            elif type == "CSS" or type == "css" or type == "Css":
                    find_element = self.driver.find_element_by_css_selector(value)
            return True
        except:
            self.driver.implicitly_wait(time+10)
            logger.error("{}模块下的{}元素不存在".format(page, element))
            return False

    def isEnabled(self, page, element):
        """判断元素是否为灰化状态"""
        enabled = self.find_element(page, element).is_enabled()
        logger.info("{}模块下的{}元素灰化状态：{}".format(page, element,enabled))
        return enabled

    def is_select(self,page,element):
        """点选框是否为选中状态"""
        select = self.find_element(page,element).is_selected()
        logger.info("{}模块下的{}元素是否为点选状态：{}".format(page, element, select))
        return select
