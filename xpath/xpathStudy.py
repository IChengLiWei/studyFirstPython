# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject

from lxml import etree
tree = etree.parse('测试文件.html')
li_list = tree.xpath('//ul/li[@id ="2"]/text()')
print(li_list)
print(len(li_list))