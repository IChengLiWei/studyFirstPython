# _*_ coding: utf-8 _*_
# @Time : 2023/8/10  
# @Author: 啊炜
# @Project: pythonLearn

def fileStaduy1():
    fileUrl = 'text.py'
    fp = open(fileUrl, 'r')
    print(fp.readline())
    fp.close()
# 序列化
import  json
def fileStudy2():
   nameList = ['zs','ls']
   fileUrl = 'text.py'
   fp = open(fileUrl, 'a')
   json.dump(nameList,fp)
   fp.close()

def fileStudyRead():
    fileUrl = 'text.py'
    fp = open(fileUrl, 'r')
    result = json.load(fp)
    print(result)
    print(type(result))
    fp.close()

fileStudyRead()
