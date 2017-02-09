# coding:utf-8
'''
Created on 2016年10月11日

@author: admin
'''

import  re
import requests

try:
    import cookielib
except:
    import http.cookiejar as cookielib


class Spider:
    def __init__(self,userAgent):

        self.user_agent = userAgent
        self.headers = {
            'User-Agent' : self.user_agent
        }
    def getHttp(self,url,param=None):
        return requests.get(url,param,headers=self.headers)

    def postHttp(self,url,postData=None):
        return requests.post(url, data=postData,headers=self.headers)

    def sessionPostHttp(self,url,param=None):
        session = requests.session()
        session.cookies = cookielib.LWPCookieJar(filename='cookies')
        try:
            session.cookies.load(ignore_discard=True)
            print(url,param)
            return session.post(url,data=param,json=None,headers=self.headers)
        except:
            print("Cookie 未能加载")
            return None

    def sessionGetHttp(self,url,param=None):
        session = requests.session()
        session.cookies = cookielib.LWPCookieJar(filename='cookies')
        try:
            session.cookies.load(ignore_discard=True)
            return session.get(url, headers=self.headers, allow_redirects=False)
        except:
            print("Cookie 未能加载")
            return None
    def parseReg(self,content,strPattern,count):
        pattern = re.compile(strPattern,re.S)
        items = re.findall(pattern,content)

        contents=[]

        for item in items:
            temArr = []
            for i in range(0,count):
                temArr.append(item[i])
            contents.append(temArr)

        return contents

    def getContents(self,url,strPattern,count,method="get",param=None):
        page = ""
        if method == "get":
            page = self.getHttp(url,param).text
        else:
            page = self.postHttp(url,param).text

        pattern = re.compile(strPattern,re.S)
        items = re.findall(pattern,page)
        contents=[]

        for item in items:
            temArr = []
            for i in range(0,count):
                temArr.append(item[i])
            contents.append(temArr)

        return contents


# demo = Spider("Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko")
#
# t = demo.getHttp("https://www.baidu.com/index.php?tn=02049043_23_pg")