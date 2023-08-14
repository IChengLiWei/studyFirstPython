# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject
import  urllib.request

import loadFile

url = 'https://www.baidu.com/s?'
# user-Agent伪装

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
def printFileWithUrl(url:str):

    request = urllib.request.Request(url, headers=headers)
    response = urllib.request.urlopen(request)
    content = response.read().decode('Utf8')
    print(content)
#printFileWithUrl(url)
#编解码 Unicode编码把所有语言放统一标准的一套编码\
import urllib.parse
#get请求的unicode编码
def unicodeStudy():
    name = urllib.parse.quote('刘诗诗')
    print(name)

    data = {'wd':'刘诗诗','sex' :'女'}
    nameS = urllib.parse.urlencode(data)
    return  nameS
    print(nameS)
url = url + unicodeStudy()
print(url)
printFileWithUrl(url)
