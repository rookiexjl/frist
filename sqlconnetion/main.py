#!/usr/bin/python
# coding:utf-8
'''
Created on 2016年9月23日

@author: admin
'''


print 'Content-type:text/html\n'
print
#import cgitb:cgitb.enable()

import MySQLdb

conn = MySQLdb.connect(db='usernet',host='127.0.0.1',user='root',passwd='root1234')

curs = conn.cursor()

print '''
<html>
  <head>
    <title>The UserNet</title>
  </head>
  <body>
    <h1>The UserNet</h1>
'''

sql = 'SELECT * FROM messages'
curs.execute(sql)

rows = curs.fetchall()
toplevel = []
children = {}

for row in rows:
        parent_id = row[3]
        if parent_id is None:
                toplevel.append(row)
        else:
                children.setdefault(parent_id,[]).append(row)

        def format(row):
                print '<p><a href="view.cgi?id=%i">%s<a>' % (row[0],row[1])
                try:
                        kids = children[row[0]]
                except KeyError:
                        pass
                else:
                        print '<blockquote>'
                        for kid in kids:
                                format(kid)

                        print '</blockquote>'

        print '<p>'

        for row in toplevel:
                format(row)

print '''
    </p>
    <hr/>
    <p><a href="edit.cgi">Post Messages</a></p>
  </body>
</html>
'''
