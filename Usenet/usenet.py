# coding:utf-8
'''
Created on 2016年9月21日

@author: admin
'''
# 这个程序，首先从整体上进行分析，重点部分在于NewsAgent，它的作用是存储新闻来源，存储目标地址，
# 然后在分别调用来源服务器（NNTPSource以及SimpleWebSource）以及写新闻的类（PlainD
# estination和HTMLDestination）。所以从这里也看的出，NNTPSource是专门用来获取新
# 闻服务器上的信息的，SimpleWebSource是获取一个url上的数据的。而PlainDestination
# 和HTMLDestination的作用很明显，前者是用来输出获取到的内容到终端的，后者是写数据到html文
# 件中的。有了这些分析，然后在来看主程序中的内容，主程序就是来给NewsAgent添加信息源和输出目的地
# 址的。这确实是个简单的程序，不过这个程序可是用到了分层了。

from nntplib import NNTP
from time import strftime,time,localtime
from email import message_from_string
from urllib import urlopen
import textwrap
import re

day = 24*60*60


def wrap(string,max=70):
        '''

        '''
        return '\n'.join(textwrap.wrap(string)) + '\n'

class NewsAgent:
        '''
        '''
        def __init__(self):
                self.sources = []
                self.destinations = []

        def addSource(self,source):
                self.sources.append(source)

        def addDestination(self,dest):
                self.destinations.append(dest)

        def distribute(self):
                items = []
                for source in self.sources:
                        items.extend(source.getItems())
#                 for dest in self.destinations:
#                         dest.receiveItems(items)

class NewsItem:
        def __init__(self,title,body):
                self.title = title
                self.body = body

class NNTPSource:
        def __init__(self,servername, group,window):
                self.servername = servername
                self.group = group
                self.window = window

        def getItems(self):
                start = localtime(time() - self.window*day)
                date = strftime('%y%m%d',start)
                hour = strftime('%H%M%S',start)

                server = NNTP(self.servername)

                ids = server.newnews(self.group,date,hour)[1]

                for id in ids:
                        lines = server.article(id)[3]
                        message = message_from_string('\n'.join(lines))

                        title = message['subject']
                        body = message.get_payload()
                        print body
                        if message.is_multipart():
                                body = body[0]

                        yield NewsItem(title, body)

                server.quit()

class SimpleWebSource:

        def __init__(self, url, titlePattern, bodyPattern):
                self.url = url
                self.titlePattern = re.compile(titlePattern)
                self.bodyPattern = re.compile(bodyPattern)

        def getItems(self):
                text = urlopen(self.url).read()
                titles = self.titlePattern.findall(text)
                bodies = self.bodyPattern.findall(text)
                for title, body in zip(titles, bodies):
                        yield NewsItem(title, wrap(body))

class PlainDestination:

        def receiveItems(self,items):
                for item in items:
                        print item.title
                        print '-'*len(item.title)
                        print item.body

class HTMLDestination:

        def __init__(self,filename):
                self.filename = filename

        def receiveItems(self,items):
                out = open(self.filename,'w')
                print >> out,'''
                <html>
                <head>
                 <title>Today's News</title>
                </head>
                <body>
                <h1>Today's News</hi>
                '''

                print >> out, '<ul>'
                id = 0
                for item in items:
                        id += 1
                        print >> out, '<li><a href="#">%s</a></li>' % (id,item.title)
                print >> out, '</ul>'

                id = 0
                for item in items:
                        id += 1
                        print >> out, '<h2><a name="%i">%s</a></h2>' % (id,item.title)
                        print >> out, '<pre>%s</pre>' % item.body

                print >> out, '''
                </body>
                </html>
                '''


def runDefaultSetup():

        agent = NewsAgent()

        bbc_url = 'http://news.bbc.co.uk/text_only'
        bbc_title = r'(?s)a href="[^"]*">\s*<b>\s*(.*?)\s*</b>'
        bbc_body = r'(?s)</a>\s*<br/>\s*(.*?)\s*<'
        bbc = SimpleWebSource(bbc_url, bbc_title, bbc_body)

        agent.addSource(bbc)
 
#         clpa_server = 'http://news.neva.ru/'
#         clpa_group = 'alt.sex.telephone'
#         clpa_window = 1
#         clpa = NNTPSource(clpa_server, clpa_group, clpa_window)
#         
#         agent.addSource(clpa)
#         print agent.sources
# 
#         agent.addDestination(PlainDestination())
#         agent.addDestination(HTMLDestination('news.html'))
#         print agent.destinations
#  
#         agent.distribute()


if __name__ == '__main__':
        runDefaultSetup()
