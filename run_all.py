import unittest

import os

import readConfig
from common import logger
from common.HTMLTestRunner import HTMLTestRunner
from testCase.w_test.login_sta import Logintest


def get_case_list():
    list = open(os.path.join(readConfig.ProjectPath,"case_list.txt"))
    cases = []
    for value in list.readlines():
        data = str(value)
        if data != "" and not data.startswith("#"):
            cases.append(data.replace("\n",""))
    return cases


def get_list():
    suite_module = []
    list  = get_case_list()

    for value in list:
        case_path  = os.path.join(logger.projectPath,"testCase")
        discover = unittest.defaultTestLoader.discover(case_path,pattern=value.split("/")[-1]+'.py', top_level_dir=None)
        suite_module.append(discover)

    #discover = unittest.defaultTestLoader.discover(case_path,pattern= "welcome_login.py",top_level_dir=None)
    #suite_module.append(discover)
    return suite_module

if __name__ == '__main__':
    result_html = logger.Logging("Run").get_logPath()
    config = readConfig.ReadConfig()
    title = config.getConfig("title") + "测试报告"
    browser = config.getConfig("browser")
    description = "浏览器：" + browser
    testunit = unittest.TestSuite()
    list = get_list()
    print(list, "list_get_list")
    if len(list) > 0:
        for suite in get_list():
            testunit.addTest(suite)
    testunit.addTest(Logintest("test_login_1"))
    filename = os.path.join(result_html, "result.html")
    fp = open(filename, "wb")
    runner = HTMLTestRunner(stream=fp, title=title, description=description)
    runner.run(testunit)
    fp.close()

