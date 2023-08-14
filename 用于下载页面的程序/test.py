# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject
import urlLibRequest
from lxml import etree
if __name__ == '__main__':
    content = urlLibRequest.loadHtmlWithUrl('https://www.baidu.com')
    tree = etree.HTML(content)
    tree_list = tree.xpath('//input[@id="su"]/@value')
    print(tree_list)