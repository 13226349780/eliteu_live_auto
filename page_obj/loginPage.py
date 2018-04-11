from common.logger import Logging
from page_obj.base import Page

logger = Logging("Login").getlog()
class Login(Page):
    """登录模块"""
    def login_head_text(self):
        """登录模块的页头文本"""
        logger.info("获取登录模块的页眉页脚文本")
        list = []
        list.append(self.text("登录模块","logo文本"))
        list.append(self.text("登录模块","宣传语"))
        list.append(self.text("登录模块", "帮助"))
        list.append(self.text("登录模块", "隐私"))
        list.append(self.text("登录模块", "条款"))
        list.append(self.text("登录模块", "公司信息"))
        return list

    def login_location(self):
        self.get_location("登录模块","form")
        return  self.get_location("登录模块","form")

    def login_submit_text(self):
        """登录模块的登录文本"""
        list = []
        list.append(self.text("登录模块-登录", "账号密码登录"))
        list.append(self.text("登录模块-登录", "手机号码登录"))
        list.append(self.element_type_value("登录模块-登录", "账号输入框"))
        list.append(self.element_type_value("登录模块-登录", "密码输入框"))
        # self.click("登录模块-登录", "手机号码登录")
        # list.append(self.element_type_value("登录模块-登录", "手机号输入框"))
        # list.append(self.element_type_value("登录模块-登录", "验证码输入框"))
        # list.append(self.text("登录模块-登录", "获取验证码"))
        # list.append(self.text("登录模块-登录", "自动登录"))
        # list.append(self.text("登录模块-登录", "忘记密码"))
        # list.append(self.text("登录模块-登录", "登录"))
        # list.append(self.text("登录模块-登录", "其他登录方式"))
        # list.append(self.text("登录模块-登录", "注册账户"))
        return list

    def login_account(self,username,password):
        """账号密码登录操作"""
        logger.info("使用账号登录，账号为：{} 密码：{}".format(username,password))
        list = []
        self.click("登录模块-登录","账号密码登录")
        self.send_keys("登录模块-登录","账号输入框",username)
        self.send_keys("登录模块-登录", "密码输入框", password)
        self.click("登录模块-登录","登录")
        if self.isElementExist("登录模块-登录","账号错误"):
            list.append(self.text("登录模块-登录","账号错误"))
        if self.isElementExist("登录模块-登录","密码错误"):
            list.append(self.text("登录模块-登录","密码错误"))
        if self.isElementExist("登录模块-登录","账号密码验证"):
            list.append(self.text("登录模块-登录","账号密码验证"))
        if len(list) == 0 :
            list.append(self.get_title())
        return list

    def login_phone(self,username,code):
        """账号密码登录操作"""
        logger.info("使用账号登录，账号为：{} 密码：{}".format(username,code))
        list = []
        self.click("登录模块-登录","手机号码登录")
        self.send_keys("登录模块-登录","手机号输入框",username)
        self.send_keys("登录模块-登录", "验证码输入框",code)
        self.click("登录模块-登录","登录")
        if self.isElementExist("登录模块-登录","手机号错误"):
            list.append(self.text("登录模块-登录","手机号错误"))
        if self.isElementExist("登录模块-登录","验证码错误"):
            list.append(self.text("登录模块-登录","验证码错误"))
        if len(list) == 0 :
            list.append(self.get_title())
        return list

    def register_text(self):
        """ 登录模块-注册账号文本信息确认"""
        self.wait_time(1)
        self.click("登录模块-登录","注册账户")
        list = []
        list.append(self.text("登录模块-注册","注册标题"))
        list.append(self.element_type_value("登录模块-注册", "用户名输入框"))
        list.append(self.element_type_value("登录模块-注册", "密码输入框"))
        list.append(self.element_type_value("登录模块-注册", "确认密码"))
        list.append(self.text("登录模块-注册", "手机区号"))
        list.append(self.element_type_value("登录模块-注册", "手机号码"))
        list.append(self.element_type_value("登录模块-注册", "验证码输入框"))
        list.append(self.text("登录模块-注册", "获取验证码"))
        list.append(self.text("登录模块-注册", "注册"))
        list.append(self.text("登录模块-注册", "使用已有账户登录"))
        return list

    def register_click(self):
        self.click("登录模块-登录", "注册账户")

    def register(self,username,pwd,password,phone,code):
        """登录模块-注册账号"""
        list = []
        self.send_keys("登录模块-注册","用户名输入框",username)
        self.send_keys("登录模块-注册", "密码输入框", pwd)
        self.send_keys("登录模块-注册", "确认密码", password)
        self.send_keys("登录模块-注册", "手机号码", phone)
        self.send_keys("登录模块-注册", "验证码输入框", code)
        self.click("登录模块-注册", "注册")
        if self.isElementExist("登录模块-注册","用户名错误"):
            list.append(self.text("登录模块-注册","用户名错误"))
        if self.isElementExist("登录模块-注册","密码错误"):
            list.append(self.text("登录模块-注册","密码错误"))
        if self.isElementExist("登录模块-注册","确认密码错误"):
            list.append(self.text("登录模块-注册","确认密码错误"))
        if self.isElementExist("登录模块-注册","手机号码错误"):
            list.append(self.text("登录模块-注册","手机号码错误"))
        if self.isElementExist("登录模块-注册","验证码错误"):
            list.append(self.text("登录模块-注册","验证码错误"))
        if self.isElementExist("登录模块-注册","注册信息验证"):
            list.append(self.text("登录模块-注册","注册信息验证"))
        if len(list) == 0:
            list.append(self.get_url())
        return list


