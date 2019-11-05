# import urllib.request
# import re
# url='http://q.stock.sohu.com/hisHq?code=cn_600519&stat=l&order=D&period=d&callback=historySearchHandler&rt=jsonp&0.18115656498417958'
# req=urllib.request.Request(url)
# with urllib.request.urlopen(req) as response:
#     data=response.read()
#     htmlstr=data.decode('gbk')
#     print(htmlstr)
#     htmlstr=htmlstr.replace('historySearchHandler(','')
#     htmlstr=htmlstr.replace(')','')
#     print('替换换后的:',htmlstr)

# 伪装成浏览器 例如:iphone safari

# import urllib.request
# url='http://www.ctrip.com'
# req=urllib.request.Request(url)
# req.add_header('User_Agent','Mozilla/5.0(iPhone; CPU iPhone OS 10_2_1 like Mac OS X) AppleWebKit/602.4.6 (KHTML,like Gecko) Version/10.0 Mobile/14D27 Safari/602.1')
#
# with urllib.request.urlopen(req) as response:
#     data=response.read()
#     htmlstr=data.decode('gbk')
#     if htmlstr.find('mobile') != -1:
#         print('移动版')

#  use  S e l e n i u m
# from selenium import webdriver
# driver=webdriver.Firefox()
# driver.get('http://q.stock.sohu.com/cn/600519/lshq.shtml')
# em=driver.find_element_by_id('BIZ_hq_historySearch')
# print(em.text)
# driver.quit()

# download img by regularExpression
# import urllib.request
# import os
# import re
#
# url = 'http://p.weather.com.cn/'
#
#
# def findallimgurl(htmlstr):
#     pattern = r'http://\S+(?:\.png|\.jpg)'
#     return re.findall(pattern, htmlstr)
#
#
# def getfilename(urlstr):
#     pos = urlstr.rfind('/')
#     return urlstr[pos + 1:]
#
# url_list=[]
# req=urllib.request.Request(url)
# with urllib.request.urlopen(req) as response:
#     data=response.read()
#     htmlstr=data.decode()
#     url_list = findallimgurl(htmlstr)
#
# for imgesrc in url_list:
#     req=urllib.request.Request(imgesrc)
#     with urllib.request.urlopen(req) as response:
#         data=response.read()
#
#         if len(data) <1024*100:
#             continue
#
#         if not os.path.exists('download'):
#             os.mkdir('download')
#         filename=getfilename(imgesrc)
#         filename='download/'+filename
#
#         with open(filename,'wb') as f:
#             f.write(data)
#
#     print('下载图片',filename)

# download img by beautifulsoup4
import urllib.request
import os
from bs4 import BeautifulSoup

url = 'http://p.weather.com.cn/'


def findallimgurl(htmlstr):
    sp = BeautifulSoup(htmlstr, 'html.parser')
    imgtaglist = sp.find_all('img')
    srclist = list(map(lambda u: u.get('src'), imgtaglist))
    filtered_srclist = filter(lambda u: u.lower().endswith('.png')
                                        or u.lower().endswith('.jpg'), srclist)
    return filtered_srclist


def getfilename(urlstr):
    pos = urlstr.rfind('/')
    return urlstr[pos + 1:]


url_list = []
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    data = response.read()
    htmlstr = data.decode()
    url_list = findallimgurl(htmlstr)

for imgesrc in url_list:
    req = urllib.request.Request(imgesrc)
    with urllib.request.urlopen(req) as response:
        data = response.read()

        if len(data) < 1024 * 100:
            continue

        if not os.path.exists('download'):
            os.mkdir('download')
        filename = getfilename(imgesrc)
        filename = 'download/' + filename

        with open(filename, 'wb') as f:
            f.write(data)

    print('下载图片', filename)
