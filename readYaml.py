import yaml
import os

filePath = os.path.dirname(__file__)
print(filePath)
fileNamePath = os.path.split(os.path.realpath(__file__))[0]
print(fileNamePath)
yamlPath = os.path.join(fileNamePath+'/testFile', 'test_data.yaml')
print(yamlPath)
f = open(yamlPath, 'r', encoding='utf-8')
cont = f.read()
yl = yaml.load(cont)


