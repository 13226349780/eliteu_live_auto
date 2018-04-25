from common.function import Excel
from testFile.config import Page_Text
from common.logger import Logging
from testCase.w_test.myunittest import loginTest

logger = Logging("LoginTest").getlog()
datas = Excel("users").read_excel(2)
# @paramunittest.parametrized(*datas)
# class LoginTest(loginTest):
#     def setParameters(self, serial_number, description, username, password, expected_result):
#         self.serial_number = str(serial_number)
#         self.description = str(description)
#         self.username = str(username)
#         self.password = str(password)
#         self.expected_result = str(expected_result)
#     def test_login(self):
#         """账号登录数据验证"""
#         logger.info("【用例开始】--》编号：{}".format(self.serial_number))
#         expected_result = self.expected_result.split(',')
#         try:
#             list = self.login.login_account(self.username, self.password)
#             self.assertEqual(expected_result,list)
#         except Exception as e:
#             self.login.get_windows_img(self.expected_result+str(self.serial_number))
#             logger.error("**用例执行失败** %s" % e)
#             self.AssertionError.append(self.serial_number)
class Logintest(loginTest):
    """登录测试用例"""
    def test_login_1(self):
        "登录模块页眉页脚文本验证"
        logger.info("【test_login_1】加载登录模块页眉页脚文本验证")
        datas = Page_Text["登录模块-页眉页脚"]
        lists = self.login.login_head_text()
        for (testFile,list) in zip(datas,lists):
            logger.info("【用例开始】--》")
            try:
                self.assertEqual(testFile,list)
                logger.info("实际结果：{}，预期结果:{}".format(list,testFile))
            except Exception as e:
                logger.error("**用例执行失败** %s" %e)
                self.AssertionError.append(e)

    # def test_login_1_1(self):
    #     "登录模块页眉页脚文本验证"
    #     self.login.window_sizi(1024,768)
    #     location = self.login.login_location()
    #     print(location, "location")
    #     #self.login.window_sizi(1280, 720)
    #     self.login.wait_time(20)
    #     logger.info("【test_login_1】加载登录模块页眉页脚页面位置验证")
    #     location  = self.login.login_location()
    #     print(location,"location")
    #     self.login.wait_time(2)

    # def test_login_2(self):
    #     """登录模块--登录文本信息"""
    #     logger.info("【test_login_2】加载登录模块文本验证")
    #     datas = Page_Text["登录模块-登录"]
    #     lists = self.login.login_submit_text()
    #     for (testFile,list) in zip(datas,lists):
    #         logger.info("【用例开始】--》")
    #         try:
    #             self.assertEqual(testFile,list)
    #             logger.info("实际结果：{}，预期结果:{}".format(list,testFile))
    #         except Exception as e:
    #             logger.error("**用例执行失败** %s" %e)
    #             self.AssertionError.append(e)

    # def test_login_3(self):
    #     """账号登录数据验证"""
    #     logger.info("【test_login_3】加载登录模块账号登录")
    #     datas = self.get_excel_data("users",2)
    #     for testFile in datas:
    #         logger.info("【用例开始】--》编号：{}".format(testFile["serial_number"]))
    #         expected_result = testFile["expected_result"].split(',')
    #         try:
    #             list = self.login.login_account(testFile["username"], testFile["password"])
    #             self.assertEqual(expected_result,list)
    #             logger.info("实际结果：{}，预期结果:{}".format(list, expected_result))
    #         except Exception as e:
    #             self.login.get_windows_img(testFile["expected_result"]+str(testFile["serial_number"]))
    #             logger.error("**用例执行失败** %s" % e)
    #             self.AssertionError.append(testFile["serial_number"])
    #
    # def test_login_4(self):
    #     """手机号登录验证"""
    #     logger.info("【test_login_4】加载登录模块手机号登录验证")
    #     datas = self.get_excel_data("users-phone", 2)
    #     for testFile in datas:
    #         logger.info("【用例开始】--》编号：{}".format(testFile["serial_number"]))
    #         expected_result = testFile["expected_result"].split(',')
    #         try:
    #             list = self.login.login_phone(testFile["username"], testFile["code"])
    #             self.assertEqual(expected_result,list)
    #             logger.info("实际结果：{}，预期结果:{}".format(list, expected_result))
    #         except Exception as e:
    #             print("aaa",testFile["expected_result"]+str(testFile["serial_number"]))
    #             self.login.get_windows_img(testFile["expected_result"]+str(testFile["serial_number"]))
    #             logger.error("**用例执行失败** %s" % e)
    #             self.AssertionError.append(testFile["serial_number"])
    #
    # def test_register_1(self):
    #     """验证注册的文本信息是否正确"""
    #     logger.info("【test_register_1】加载注册的文本信息验证用例")
    #     datas = Page_Text["登录模块-注册账户"]
    #     lists = self.login.register_text()
    #     for (testFile,list) in zip(datas,lists):
    #         logger.info("【用例开始】--》")
    #         try:
    #             self.assertEqual(testFile, list)
    #             logger.info("实际结果:{}，预期结果:{}".format(list, testFile))
    #         except Exception as e:
    #             logger.error("**用例执行失败** %s" % e)
    #             self.AssertionError.append(e)
    #
    # def test_register_2(self):
    #     """注册账号"""
    #     logger.info("【test_register_2】加载注册账号用例")
    #     self.login.register_click()
    #     datas = self.get_excel_data("register")
    #     for testFile in datas:
    #         logger.info("【用例开始】--》")
    #         list = self.login.register(testFile["username"],testFile["pwd"],testFile["password"],testFile["phone"],testFile["code"])
    #         try:
    #             expected_result = testFile["expected_result"].split(',')
    #             self.assertEqual(expected_result, list)
    #             logger.info("实际结果：{}，预期结果:{}".format(list, expected_result))
    #         except Exception as e:
    #             logger.error("**用例执行失败** %s" % e)
    #             self.AssertionError.append(e)



