#!/usr/bin/python
# coding:utf-8
'''
Created on 2016年9月23日

@author: admin
'''

print 'Content-type:text/html\n'

import cgitb;cgitb.enable()

def quote(string):
        if string:
                return string.replace("'","\\'")
        else:
                return string

import MySQLdb
conn = MySQLdb.connect(db='usernet',host='127.0.0.1',user='root',passwd='root1234')
curs = conn.cursor()

import cgi, sys
form = cgi.FieldStorage()

sender = quote(form.getvalue('sender'))
subject = quote(form.getvalue('subject'))
text = quote(form.getvalue('text'))
reply_to = form.getvalue('reply_to')

if not (sender and subject and text):
        print 'Please supply sender,subject,text'
        sys.exit()

if reply_to is not None:
        query = """
        INSERT INTO messages(reply_to,sender,subject,text)
        VALUES(%d,'%s','%s','%s')""" % (int(reply_to),sender,subject,text)
else:
        query = """
        INSERT INTO messages(sender,subject,text)
        VALUES('%s','%s','%s')""" % (sender,subject,text)

curs.execute(query)
conn.commit()

print '''
<html>
  <head>
    <title>Messages Save</title>
  </head>
  <body>
    <h1>Messages Saved</h1>
    <hr/>
    <a href='main.cgi'>Back to the main page</a>
  </body>
</html>s
'''
