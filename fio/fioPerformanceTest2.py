# coding:utf-8
import subprocess
import string


def getRWinfo(listdev):
    print '*********************************************************FIOPerformanceTest************************************************************'
    print '---------------------------------------------------------------------------------------------------------------------------------------'
    print '***DISK***      ***WSPEED****      ***RSPEED***    ****LAT*****     ***RIOPS***      ***WIOPS***      *****LAT******      ****LIFE*****'
    print '---------------------------------------------------------------------------------------------------------------------------------------'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=rw -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest -rwmixwrite=30' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        rspeed = data[6].split(',')[1].strip().split('bw=')[1]
        runit1 = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat1 = data[8].split(',')[2].strip().split('avg=')[1]
        if data[15].find('iops')!=-1:
            wspeed = data[15].split(',')[1].strip().split('bw=')[1]
            wunit1 = data[17].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat1 = data[17].split(',')[2].strip().split('avg=')[1]
        else:
            wspeed = data[16].split(',')[1].strip().split('bw=')[1]
            wunit1 = data[18].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat1 = data[18].split(',')[2].strip().split('avg=')[1]
        latc1 = ''
        unit1 = ''
        if runit1 == wunit1:
            lat1 = (string.atof(rlat1)+string.atof(wlat1))/2
            latc1 = '%.2f' % lat1
            unit1 = wunit1
        else:
            if string.atof(rlat1) < string.atof(wlat1):
                lat1 = (string.atof(rlat1)*1000+string.atof(wlat1))/2
                latc1 = '%.2f' % lat1
                unit1 = wunit1
            else:
                lat1 =(string.atof(rlat1)+string.atof(wlat1)*1000)/2
                latc1 = '%.2f' % lat1
                unit1 = runit1 

        cmd1 = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=randrw -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest -rwmixwrite=30 ' % disk
        p1 = subprocess.Popen(cmd1, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data1 = []
        for line in p1.stdout.readlines():
            data1.append(line)
        riops = data1[6].split(',')[2].strip().split('iops=')[1]
        runit2 = data1[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat2 = data1[8].split(',')[2].strip().split('avg=')[1]
        if data1[15].find('iops')!=-1:
            wiops = data1[15].split(',')[2].strip().split('iops=')[1]
            wunit2 = data1[17].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat2 = data1[17].split(',')[2].strip().split('avg=')[1]
        else:
            wiops = data1[16].split(',')[2].strip().split('iops=')[1]
            wunit2 = data1[18].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
            wlat2 = data1[18].split(',')[2].strip().split('avg=')[1]
        latc2 = ''
        unit2 = ''
        if runit2 == wunit2:
            lat2 = (string.atof(rlat2)+string.atof(wlat2))/2
            latc2 = '%.2f' % lat2
            unit2 = wunit2
        else:
            if string.atof(rlat2) < string.atof(wlat2):
                lat2 = (string.atof(rlat2)*1000+string.atof(wlat2))/2
                latc2 = '%.2f' % lat2
            else:
                lat2 =(string.atof(rlat2)+string.atof(wlat2)*1000)/2
                latc2 = '%.2f' % lat2
                unit2 = runit2
        print disk + rspeed.rjust(20) + wspeed.rjust(18) + (latc1+unit1).rjust(16) + riops.rjust(16) + wiops.rjust(17)+(latc2+unit2).rjust(20)
        print '---------------------------------------------------------------------------------------------------------------------------------------'


def getdev():
    listdev=[]
    p = subprocess.Popen('blkid -s PARTUUID', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for dev in p.stdout.readlines():
        listdev.append(dev.split(':')[0])
    return listdev


if __name__ == '__main__':
    #listdev=getdev()
    listdev=['/dev/sdb1']
    #getRWinfo(listdev)
    print
    getdev()
    # getRWinfo(listdev)

