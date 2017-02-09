#-*- coding: UTF-8 -*-
import boto
from boto.s3.connection import S3Connection
from boto.s3.key import Key
import mysql.connector
import threading
import time

mysql_conn=mysql.connector.connect(host="192.168.2.111",user="root",passwd="root1234",db="tsm_dev")
cursor = mysql_conn.cursor()
cursor.execute("select access_key, secret_key from os_auth")
users = cursor.fetchmany(500)

host = '192.168.2.246'
port = 8080
is_secure = False


def uploadFile(aws_access_key_id, aws_secret_access_key, to_key, from_file):
    connection = boto.s3.connection.S3Connection(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        port=port,
        host=host,
        is_secure=is_secure,
        calling_format=boto.s3.connection.OrdinaryCallingFormat())

    bucket_name = "";
    buckets = connection.get_all_buckets()
    for bucket in buckets:
        tmp_name = bucket.name
        if tmp_name.find("recycle-bin--") == -1:
            bucket_name = tmp_name

    con = connection.get_bucket(bucket_name)
    file_key=Key(con, to_key)
    file_key.set_contents_from_filename(from_file)

    print "upload success , aws_access_key_id: ", aws_access_key_id


i = 0
while i<1:

    for os_auth in users:
        print os_auth
        aws_access_key_id, aws_secret_access_key = os_auth
        
        to_key = "test/" + time.ctime()  + ".zip"
        from_file = "E:\\learn\\python\\spliter\\app1.zip"
        # uploadFile(aws_access_key_id, aws_secret_access_key, to_key, from_file)
        thread = threading.Thread(target=uploadFile,args=(aws_access_key_id, aws_secret_access_key, to_key, from_file))
    

        thread.start()
    i+=1