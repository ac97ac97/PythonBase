import configparser

# 读取配置文件

# config = configparser.ConfigParser()  # 创建配置解析器对象
# config.read('F:\Python_project\py_for\venv\src\ctrl_dataChangeFormat\data\Setup.ini', encoding='utf-8')  # 读取并解析读取配置文件
# print(config.sections())  # 返回所有的节
#
# section1 = config['Startup']  # 返回startup节
# print(config.options('Startup'))
#
# print(section1[RequireOS])
# print(section1[RequireIE])
#
# print(config['Product']['msi'])
# print(config['Windows 2000']['MajorVersion'])  # 返回MajorVersion对象
# print(config['Windows 2000']['ServicePackMajor'])
#
# value = config.get('Windows 2000', 'MajorVersion')  # 返回MajorVersion对象
# print(type(value))
#
# value = config.getint('Windows 2000', 'MajorVersion')  # 返回MajorVersion对象
# print(type(value))


#写入配置文件
config = configparser.ConfigParser()  #config = configparser.ConfigParser()
config.read('F:\Python_project\py_for\venv\src\ctrl_dataChangeFormat\data\Setup.ini', encoding='utf-8') #读取并解析读取配置文件
config['Startup']['RequireMSI'] = 8.0
config['Product']['RequireMSI'] = 8.0
config.add_section('Section2')      #添加节
config.set('Section2','name','Mac') #添加配置项
with open('F:\Python_project\py_for\venv\src\ctrl_dataChangeFormat\data\Setup.ini','w') as fw:
    config.write(fw)