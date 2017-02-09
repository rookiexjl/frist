import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root1234',db='sys',port=3306)
    cur=conn.cursor()
    cur.execute('select * from session')
    cur.close()
    conn.close()
    print 'success'
except MySQLdb.Error,e:
    print "Mysql Error %d: %s" % (e.args[0], e.args[1])
