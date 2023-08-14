# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject
import urllib.request
import urllib.parse
url = 'https://fanyi.baidu.com/sug'
# user-Agent伪装

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
data = {'kw':'来吧'}
data = urllib.parse.urlencode(data).encode('utf-8')

request = urllib.request.Request(url=url,data=data,headers=headers)
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
import  json
obj = json.loads(content)
print(obj)