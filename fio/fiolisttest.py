# coding:utf-8
import subprocess



def getRinfo(listdev):
    print '********************************r***********************************************'
    print '***disk***         ****speed****         ***iops****       *******lat***********'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=read -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        speed = data[6].split(',')[1].strip().split('bw=')[1]
        iops = data[6].split(',')[2].strip().split('iops=')[1]
        unit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        lat = data[8].split(',')[2].strip().split('avg=')[1]
        print disk + speed.rjust(23) + iops.rjust(20)+(lat+unit).rjust(28)


def getWinfo(listdev):
    print '********************************w***********************************************'
    print '***disk***         ****speed****         ***iops****       *******lat***********'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=write -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        speed = data[6].split(',')[1].strip().split('bw=')[1]
        iops = data[6].split(',')[2].strip().split('iops=')[1]
        unit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        lat = data[8].split(',')[2].strip().split('avg=')[1]
        print disk + speed.rjust(23) + iops.rjust(20)+(lat+unit).rjust(28)

def getRWinfo(listdev):
    print '********************************rw**********************************************'
    print '***disk***         ***rspeed****         ***riops***       *******rlat**********         ***wspeed***          ***wiops***      *******wlat******'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=rw -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        rspeed = data[6].split(',')[1].strip().split('bw=')[1]
        riops = data[6].split(',')[2].strip().split('iops=')[1]
        runit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat = data[8].split(',')[2].strip().split('avg=')[1]
        wspeed = data[15].split(',')[1].strip().split('bw=')[1]
        wiops = data[15].split(',')[2].strip().split('iops=')[1]
        wunit = data[17].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        wlat = data[17].split(',')[2].strip().split('avg=')[1]
        print disk + rspeed.rjust(23) + riops.rjust(20)+(rlat+runit).rjust(28)+ wspeed.rjust(21)+wiops.rjust(21)+(wlat+wunit).rjust(23)


def getRandRinfo(listdev):
    print '********************************randr*******************************************'
    print '***disk***         ****speed****         ***iops****       ********lat**********'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=randread -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        speed = data[6].split(',')[1].strip().split('bw=')[1]
        iops = data[6].split(',')[2].strip().split('iops=')[1]
        unit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        lat = data[8].split(',')[2].strip().split('avg=')[1]
        print disk + speed.rjust(23) + iops.rjust(20)+(lat+unit).rjust(28)	

def getRandWinfo(listdev):
    print '********************************randw*******************************************'
    print '***disk***         ****speed****         ***iops****       *******lat***********'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=randwrite -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        speed = data[6].split(',')[1].strip().split('bw=')[1]
        iops = data[6].split(',')[2].strip().split('iops=')[1]
        unit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        lat = data[8].split(',')[2].strip().split('avg=')[1]
        print disk + speed.rjust(23) + iops.rjust(20)+(lat+unit).rjust(28)


def getRandRWinfo(listdev):
    print '********************************randrw******************************************'
    print '***disk***         ***rspeed****         ***riops***       ******rlat***********         ***wspeed***          ***wiops***      *******wlat******'
    for disk in listdev:
        cmd = 'fio -filename=%s -direct=1 -iodepth 1 -thread -rw=randrw -ioengine=psync -bs=8k -size=1m -numjobs=10 -runtime=60 -group_reporting -name=mytest' % disk
        p = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
        data = []
        for line in p.stdout.readlines():
            data.append(line)
        rspeed = data[6].split(',')[1].strip().split('bw=')[1]
        riops = data[6].split(',')[2].strip().split('iops=')[1]
        runit = data[8].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        rlat = data[8].split(',')[2].strip().split('avg=')[1]
        wspeed = data[15].split(',')[1].strip().split('bw=')[1]
        wiops = data[15].split(',')[2].strip().split('iops=')[1]
        wunit = data[17].split(',')[0].split(':')[0].strip().split('lat (')[1].split(')')[0]
        wlat = data[17].split(',')[2].strip().split('avg=')[1]
        print disk + rspeed.rjust(23) + riops.rjust(20)+(rlat+runit).rjust(28)+ wspeed.rjust(21)+wiops.rjust(21)+(wlat+wunit).rjust(23)

def getdev():
    listdev=[]
    p = subprocess.Popen('blkid -s PARTUUID', shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    for dev in p.stdout.readlines():
        listdev.append(dev.split(':')[0])
    return listdev


if __name__ == '__main__':
    #listdev=getdev()
    listdev=['/dev/sdb1']
    getRinfo(listdev)
    print
    getWinfo(listdev)
    print
    getRWinfo(listdev)
    print
    getRandRinfo(listdev)
    print
    getRandWinfo(listdev)
    print
    getRandRWinfo(listdev)
