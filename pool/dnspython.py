# coding:utf-8
'''
Created on 2016年11月24日

@author: admin
'''

import dns.resolver

hosts = ["oreilly.com", "yahoo.com", "google.com", "microsoft.com", "cnn.com"]


def query(host_list=hosts):
    collection = []
    for host in host_list:
        ip = dns.resolver.query(host, "A")
        for i in ip:
            collection.append(str(i))
    return collection


if __name__ == "__main__":
    for arec in query():
        print arec
