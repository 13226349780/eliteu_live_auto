from configparser import ConfigParser

import os

ProjectPath = os.path.split(os.path.realpath(__file__))[0]  #获取当前项目路径
ConfigPath = os.path.join(ProjectPath, "config.ini")
class ReadConfig:
    def __init__(self):
        self.read_config = ConfigParser()
        self.read_config.read(ConfigPath)
        print(self.read_config, "ConfigPath")

    def getConfig(self, property):
        """通过property 取配置文件的对应值"""
        return self.read_config.get("CONFIG", property)

