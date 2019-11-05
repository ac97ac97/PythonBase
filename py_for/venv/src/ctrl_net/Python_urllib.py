# 使用urllib进行简单请求
# import urllib.request
# with urllib.request.urlopen('http://www.sina.com.cn/') as response:
#     data=response.read()
#     html=data.decode()
#     print(html)

# 发送get请求
# import urllib.request
# import urllib.parse
#
# url='http://www.51work6.com/service/mynotes/WebService.php'
# params_dict={'email':'1727346812@qq.com','type':'JSON','action':'query'}
# params_str=urllib.parse.urlencode(params_dict)
# print(params_dict)
#
# url=url + '?' +params_str #HTTP参数放在URL参数之后
# print(url)
#
# req=urllib.request.Request(url)
# with urllib.request.urlopen(req) as response:
#     data=response.read()
#     json_data=data.decode()
#     print(json_data)

# 发送post请求
# import urllib.request
# import urllib.parse
#
# url = 'http://www.51work6.com/service/mynotes/WebService.php'
# params_dict = {'email': '1727346812@qq.com', 'type': 'JSON', 'action': 'query'}
# params_str = urllib.parse.urlencode(params_dict)
# print(params_dict)
# params_bytes=params_str.encode()
#
#
# req = urllib.request.Request(url,data=params_bytes)
# with urllib.request.urlopen(req) as response:
#     data = response.read()
#     json_data = data.decode()
#     print(json_data)

# 实例：downloader

import urllib.request
import urllib.parse

url = 'http://a.hiphotos.baidu.com/image/pic/item/f603918fa0ec08fa3139e00153ee3d6d55fbda5f.jpg'

with urllib.request.urlopen(url) as response:
    data = response.read()
    f_name = 'F:\\Python_project\\py_for\\venv\\src\\ctrl_net\\download.jpg'
    with open(f_name, 'wb') as f:
        f.write(data)
        print('下载文件成功')
