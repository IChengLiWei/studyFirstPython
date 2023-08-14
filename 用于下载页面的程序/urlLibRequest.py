# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject
import urllib.request
import urllib.parse
currentHeaders = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
#无参数使用
def getRequestForNoParams(url:str):
   request = urllib.request.Request(url,headers=currentHeaders)
   return request
def getRequestForParms(url:str,data:dict):
    newData = urllib.parse.urlencode(data)
    url = url + newData
    print(url)
    request = urllib.request.Request(url,headers=currentHeaders)
    return request
def postRequestForParms(url:str,data:dict):
    newData = urllib.parse.urlencode(data).encode('utf-8')
    request = urllib.request.Request(url,data=newData,headers=currentHeaders)
    return request

def loadHtmlWithUrl(inputUrl:str):
    request = getRequestForNoParams(inputUrl)
    response = urllib.request.urlopen(request)
    content  = response.read().decode('utf-8')
    return content
def saveToFp(content):
    saveName = input('请输入存入名称:')
    saveName = getCompeleteName(saveName)
    fp = open(saveName,'w',encoding='utf-8')
    fp.write(content)
    fp.close()

def getCompeleteName(name:str):
    name = name + '.html'
    return name
def inputAddress(url:str):
    address = ''
    if len(url) > 0:
        address = 'https://' + url
    else:
        address = input('请输入爬取地址：')
        address = 'https://' + address
    inputA = int(input('请输入是否代理：'))
    if inputA == 0:
        content = loadHtmlWithUrlPoxies(address)
        # saveToFp(content)
    else:
        content = loadHtmlWithUrl(address)
        # saveToFp(content)
    return content

proxies_list = [
    {'http': '114.231.46.195:8888'},
    {'http': '114.231.41.196:8888'},
    {'http': '58.20.184.187:9091'},
]

import random
proxies = random.choice(proxies_list)
def loadHtmlWithUrlPoxies(inputUrl:str):
    request = getRequestForNoParams(inputUrl)
    print(proxies)
    handler = urllib.request.ProxyHandler(proxies=proxies)
    opener = urllib.request.build_opener(handler)
    response = opener.open(request)
    content = response.read().decode('utf-8')
    return content

