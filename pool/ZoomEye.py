# coding:utf-8

'''
Created on 2016年9月30日

@author: admin
'''
# import urllib
# import re

import urllib2

url = "https://www.zoomeye.org"
aheaders = {'User-Agent': ''}

req_timeout = 5
req = urllib2.Request(url, headers=aheaders)
resp = urllib2.urlopen(req, timeout=req_timeout)
html = resp.read()
print(html)



# def searchObject(object):
#     try:
#         uip=urllib.urlopen('https://www.zoomeye.org/search?t=host&q=%s' % object)
#         uip.headers()
#         fip=uip.read()
#         rip=re.compile(r"\d+\.\d+\.\d+\.\d+")
#         result=rip.findall(fip)
#         print result
#         #! /usr/bin/env python
# # -*- coding=utf-8 -*- 
# # @Author pythontab.com
# 
# 
# 
# 
# if __name__ == '__main__':
#     searchObject('Symantec Messaging Gateway')
