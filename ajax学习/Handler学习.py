# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject

import  urllib.request
url = 'https://www.baidu.com'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url,headers=headers)
# 普通方式请求
response = urllib.request.urlopen(request)
# handler 请求
responseHandler = urllib.request.HTTPSHandler()
opener = urllib.request.build_opener(responseHandler)
newResponse = opener.open(request)
# 打印
content = newResponse.read().decode('utf-8')
print(content)

# 代理服务器
proxyData = {
    'http':''
}
handler = urllib.request.proxy_bypass()