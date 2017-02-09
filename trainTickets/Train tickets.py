# -*- coding:utf-8 -*-
# Author : yoyojacky
# Date : 2017-01-04
# python 2.7

'''
导入库模块
'''
import urllib2
import ssl
import json
import time

'''
停用CA客户端认证
'''
ssl._create_default_https_context = ssl._create_unverified_context

'''
定义城市名称和代码对应关系
'''
city = '@bji|北京|BJP|0@sha|上海|SHH|1@tji|天津|TJP|2@cqi|重庆|CQW|3@csh|长沙|CSQ|4@cch|长春|CCT|5@cdu|成都|CDW|6@fzh|福州|FZS|7@gzh|广州|GZQ|8@gya|贵阳|GIW|9@hht|呼和浩特|HHC|10@heb|哈尔滨|HBB|11@hfe|合>肥|HFH|12@hzh|杭州|HZH|13@hko|海口|VUQ|14@jna|济南|JNK|15@kmi|昆明|KMM|16@lsa|拉萨|LSO|17@lzh|兰州|LZJ|18@nni|南宁|NNZ|19@nji|南京|NJH|20@nch|南昌|NCG|21@sya|沈阳|SYT|22@sjz|石家庄|SJP|23@tyu|太原|TYV|24@wlq|乌鲁木齐南|WMR|25@wha|武汉|WHN|26@xni|西宁|XNO|27@xan|西安|XAY|28@ych|银川|YIJ|29@zzh|郑州|ZZF|30@szh|深圳|SZQ|shenzhen|sz|31@xme|厦门|XMS|xiamen|xm|32'

city_d = {}
tmp_c = city.split('@')
for i in tmp_c:
    if not i:continue
    city_d[i.split('|')[1]] = i.split('|')[2]

'''
定义查询的车次时间,始发站,到达站,座位类型
'''
start_time = raw_input(u'请输入出发时间(格式:2016-01-02):')
city_s = city_d['上海']
city_t = city_d['济南']
yw = 'yw_num' #硬卧
rw = 'rw_num' #软卧
zy = 'zy_num' #一等座
swz = 'swz_num'

def getList():
    html = urllib2.urlopen('https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=%s&leftTicketDTO.from_station=%s&leftTicketDTO.to_station=%s&purpose_codes=ADULT' %(start_time,city_s,city_t)).read()
    res = json.loads(html)
    print res
    return res

car_info = ''
for i in getList()['data']:
    car_info_tmp = u'''
    车次: %s
        出发时间: %s
        历时: %s
        硬卧: %s
        软卧: %s
        一等座: %s
        商务座: %s \n''' %(i['queryLeftNewDTO']['station_train_code'],i['queryLeftNewDTO']['start_time'],i['queryLeftNewDTO']['lishi'],i['queryLeftNewDTO'][yw],i['queryLeftNewDTO'][rw],i['queryLeftNewDTO'][zy],i['queryLeftNewDTO'][swz])
    print car_info_tmp
    print "-----------------------------------------------"
    print u'检测时间%s' % time.strftime('%Y-%m-%d %H:%M:%S')
print u"始发站:",city_s
print u"到达站:",city_t
print u"-----------------------------------------------"
