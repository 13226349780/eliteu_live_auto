import unittest as unittest

from common.drive import Driver
from page_obj.base import Page
from readYaml import yl


class tes_login():
    #browser = yl['t_ed_student']['browser']
    #url = yl['t_ed_student']['url']
    def t_login(self,url,browser):
        self.driver = Driver(self.brower).open_browser(self.url)
        self.click("test_login", "username")

        username = yl['t_ed_student']['username']
        #print(username)
        self.send_keys("test_login", "username", username)
        password = yl['t_ed_student']['pwd']
        self.send_keys("test_login", "password", password)
        self.click("test_login", "confirm")

