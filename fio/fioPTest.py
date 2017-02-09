# coding:utf-8
import subprocess
import string
import threadpool


def getRWinfo(disk):
    disk1 = disk.split('/dev/')[1]
    cmd = 'fio -filename=%s -direct=1 -iodepth=32 -thread -rw=rw -size=1m -ioengine=libaio -bs=8k  -numjobs=10 -runtime=30 -group_reporting -name=mytest -rwmixwrite=70 -output=%s.txt' % (disk,disk1)
    p1 = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    disk2 = disk1 + "w"
    cmd1 = 'fio -filename=%s -direct=1 -iodepth=32 -thread -rw=randrw -size=1m -ioengine=libaio -bs=8k -numjobs=10 -runtime=30 -group_reporting -name=mytest -rwmixwrite=70 -output=%sr.txt' % (disk,disk2)
    p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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


if __name__ == '__main__':
    print
    print '*********************************************************FIOPerformanceTest************************************************************'
    print '---------------------------------------------------------------------------------------------------------------------------------------'
    print '***DISK***      ***WSPEED****      ***RSPEED***    ****LAT*****     ***RIOPS***      ***WIOPS***      *****LAT******      ****LIFE*****'
    print '---------------------------------------------------------------------------------------------------------------------------------------'
    newlist = getdev()
    pool = threadpool.ThreadPool(3)
    requests = threadpool.makeRequests(getRWinfo, newlist)  
    [pool.putRequest(req) for req in requests]  
    pool.wait()

