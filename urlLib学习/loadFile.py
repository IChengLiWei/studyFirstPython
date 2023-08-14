# _*_ coding: utf-8 _*_
# @Time : 2023/8/14  
# @Author: 啊炜
# @Project: pythonProject

import urllib.request

pageUrl = 'http://www.baidu.com'
imageUrl = 'https://img0.baidu.com/it/u=2018717079,3443882001&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=666'
vidioUrl = 'https://vd3.bdstatic.com/mda-mfuf163rfmkn36i7/sc/cae_h264_nowatermark/1624963807340099361/mda-mfuf163rfmkn36i7.mp4?v_from_s=hkapp-haokan-hna&auth_key=1691994317-0-0-4ba36f00a402e63c9e6aa22f98a252a2&bcevod_channel=searchbox_feed&pd=1&cr=2&cd=0&pt=3&logid=1517504910&vid=10554454971571011271&klogid=1517504910&abtest=111803_4-112162_4'
def loadFileWithUrl(url:str,type:str):
    content = urllib.request.urlretrieve(url,filename=type)

inputVar = int(input('请输入下载内容:'))

if inputVar == 0 :
    loadFileWithUrl(pageUrl,'百度.html')
elif inputVar == 1 :
    loadFileWithUrl(imageUrl,'美女.jpg')
elif inputVar == 2 :
    loadFileWithUrl(vidioUrl,'视频.mp4')
else: print('无相关内容')
