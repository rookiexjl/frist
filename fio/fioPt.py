# coding:utf-8
import subprocess
import string


def getRWinfo(newlist):
    for disk in newlist:
        print '*********************************************************FIOPerformanceTest************************************************************'
        print '---------------------------------------------------------------------------------------------------------------------------------------'
        print '***DISK***      ***WSPEED****      ***RSPEED***    ****LAT*****     ***RIOPS***      ***WIOPS***      *****LAT******      ****LIFE*****'
        print '---------------------------------------------------------------------------------------------------------------------------------------'
        cmd = 'fio -filename=%s -direct=1 -iodepth=32 -thread -rw=rw -size=1g -ioengine=libaio -bs=8k  -numjobs=10 -runtime=10 -group_reporting -name=mytest -rwmixwrite=70' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        rspeed = data[6].split(',')[1].strip().split('bw=')[1].split('KB/s')[0]
        rspeed = string.atof(rspeed)/1000
        rspeed = '%.2f MB/s' % rspeed
        runit1 = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat1 = data[8].split(',')[2].strip().split('avg=')[1]
        if data[16].find('iops')!=-1:
            wspeed = data[16].split(',')[1].strip().split('bw=')[1].split('KB/s')[0]
            wspeed = string.atof(wspeed)/1000
            wspeed = '%.2f MB/s' % wspeed
    
            wunit1 = data[18].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat1 = data[18].split(',')[2].strip().split('avg=')[1]
        else:
            wspeed = data[17].split(',')[1].strip().split('bw=')[1].split('KB/s')[0]
            wspeed = string.atof(wspeed)/1000
            wspeed = '%.2f MB/s' % wspeed
    
            wunit1 = data[19].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat1 = data[19].split(',')[2].strip().split('avg=')[1]
        latc1 = ''
        unit1 = ''
        if runit1 == wunit1:
            if runit1 == 'msec':
                lat1 = (string.atof(rlat1)+string.atof(wlat1))/2
                latc1 = '%.2f' % lat1
                unit1 = wunit1
            else:
                lat1 = (string.atof(rlat1)+string.atof(wlat1))/2000
                latc1 = '%.2f' % lat1
                unit1 = 'msec'
        else:
            if string.atof(rlat1) < string.atof(wlat1):
                lat1 = (string.atof(rlat1)*1000+string.atof(wlat1))/2000
                latc1 = '%.2f' % lat1
                unit1 = runit1
            else:
                lat1 =(string.atof(rlat1)+string.atof(wlat1)*1000)/2000
                latc1 = '%.2f' % lat1
                unit1 = wunit1 
    
        cmd1 = 'fio -filename=%s -direct=1 -iodepth=32 -thread -rw=randrw -size=100g -ioengine=libaio -bs=8k -numjobs=10 -runtime=10 -group_reporting -name=mytest -rwmixwrite=70' % disk
        p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data1 = []
        for line in p1.stdout.readlines():
            data1.append(line)
        riops = data1[6].split(',')[2].strip().split('iops=')[1]
        runit2 = data1[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat2 = data1[8].split(',')[2].strip().split('avg=')[1]
        if data1[16].find('iops')!=-1:
            wiops = data1[16].split(',')[2].strip().split('iops=')[1]
            wunit2 = data1[18].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat2 = data1[18].split(',')[2].strip().split('avg=')[1]
        else:
            wiops = data1[17].split(',')[2].strip().split('iops=')[1]
            wunit2 = data1[19].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat2 = data1[19].split(',')[2].strip().split('avg=')[1]
        latc2 = ''
        unit2 = ''
        if runit2 == wunit2:
            if runit1 == 'msec':
                lat2 = (string.atof(rlat2)+string.atof(wlat2))/2
                latc2 = '%.2f' % lat2
                unit2 = wunit2
            else:
                lat2 = (string.atof(rlat2)+string.atof(wlat2))/2000
                latc2 = '%.2f' % lat2
                unit2 = 'msec'
        else:
            if string.atof(rlat2) < string.atof(wlat2):
                lat2 = (string.atof(rlat2)*1000+string.atof(wlat2))/2000
                latc2 = '%.2f' % lat2
                unit2 = runit2
            else:
                lat2 =(string.atof(rlat2)+string.atof(wlat2)*1000)/2000
                latc2 = '%.2f' % lat2
                unit2 = wunit2
        print disk + rspeed.rjust(20) + wspeed.rjust(18) + (latc1+unit1).rjust(16) + riops.rjust(16) + wiops.rjust(17)+(latc2+unit2).rjust(20)
        print '---------------------------------------------------------------------------------------------------------------------------------------'


def getdev():
    listdev = []
    rmlist = []
    newlistdev = []
    newlist = []
    p = subprocess.Popen('lsblk -l', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for dev in p.stdout.readlines():
        listdev.append(dev[0:3])
        if dev.find('/boot')!=-1:
            rmlist.append(dev[0:3])
    listdev1 = set(listdev)
    l = list(listdev1)
    l.sort()
    for i in l:
        if i[0:2] == 'sd':
            newlistdev.append(i)
    newlistdev.remove(rmlist[0])
    for i in newlistdev:
        newlist.append('/dev/'+i)
    return newlist

def Pit(disk1):
    print disk1

if __name__ == '__main__':
    print
    newlist = getdev()
    getRWinfo(newlist)
#     pool = threadpool.ThreadPool(30)
#     requests = threadpool.makeRequests(getRWinfo, newlist)  
#     [pool.putRequest(req) for req in requests]  
#     pool.wait()

