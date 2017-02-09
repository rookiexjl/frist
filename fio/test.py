# coding:utf-8
'''
Created on 2016年12月20日

@author: admin
'''
import string
import threadpool

a = ['s','1','asdasd','ssd','dsad','ssd2','dasdad']
b = []
j = 0
for i in a:
    if i.find('ssd') != -1:
        b.insert(j, i)
        j = j + 1 
    else:
        b.append(i)

print b

a='30578KB/s'
wspeed = a.split('KB/s')[0]
wspeed = string.atof(wspeed)/1000
wspeed = '%.2f MB/s' % wspeed
print wspeed


wspeed = '30578KB/s'
if wspeed.find('MB/s'):
    wspeed = wspeed
elif wspeed.find('KB/s'):
    wspeed = wspeed.split('KB/s')[0]
    wspeed = string.atof(wspeed)/1000
    wspeed = '%.2f MB/s' % wspeed
elif wspeed.find('B/s'):
    wspeed = wspeed.split('B/s')[0]
    wspeed = string.atof(wspeed)/1000000
    wspeed = '%.2f MB/s' % wspeed         
print wspeed
# def Pit(disk1):
#     print disk1
# 
# if __name__ == '__main__':
#     print
#     #newlist = getdev()
#     # getRWinfo(newlist)
#     a = ['张三', 'lisi']
#     pool = threadpool.ThreadPool(30)
#     requests = threadpool.makeRequests(Pit, a)  
#     [pool.putRequest(req) for req in requests]  
#     pool.wait()

rspeed = '64825'
rspeed = string.atof(rspeed)/1000000
rspeed = '%.2f MB/s' % rspeed
print  rspeed
