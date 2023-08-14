# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject
# 豆瓣电影第一页获取并保存
import urllib.request
import urllib.parse
url = 'https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}

request = urllib.request.Request(url=url,headers=headers)

response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')
print(content)
#文件保存默认编码 为GBK 修改编码方式 encodeding = 'utf-8'
fp = open('豆瓣喜剧第一页.json','w',encoding='utf-8')
fp.write(content)
fp.close()
