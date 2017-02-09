#!/usr/bin/env python2.7
# coding=utf-8

import json
import urllib2
# based url and required header
url = "http://192.168.3.26/zabbix/api_jsonrpc.php"
header = {"Content-Type": "application/json"}
# auth user and password
data = json.dumps(
{
    "jsonrpc": "2.0",
    "method": "item.get",
    "params": {
        "output": "extend",
        "hostids": "10084",
        "search": {
            "key_": "vfs.fs"
        },
        "sortfield": "name"
    },
    "auth": "9a2a4cd9c3de005b11acb47fa36f8b1c",
    "id": 1
})
# create request object
request = urllib2.Request(url,data)
for key in header:
    request.add_header(key,header[key])
# auth and get authid

try:
    result = urllib2.urlopen(request)
except urllib2.URLError as e:
    print "GetDisk Failed, Please Check Json:",e.code
else:
    response = json.loads(result.read())
    result.close()
    print "Disk Successful. The Info Is:", response['result']
