# coding:utf-8
from urllib import urlopen
from reportlab.graphics.shapes import *
from reportlab.graphics.charts.lineplots import LinePlot
from reportlab.graphics.charts.textlabels import Label
from reportlab.graphics import renderPDF

URL = 'http://services.swpc.noaa.gov/text/predicted-sunspot-radio-flux.txt'
COMMENT_CHARS = '#:'

# 创建一个400*200像素大小 的PDF格式图形
drawing = Drawing(400, 200)
data = []
# 读取Product中数据进行筛选，将正确数据添加到data元组中
for line in urlopen(URL).readlines():
        if not line.isspace() and not line[0] in COMMENT_CHARS:
                data.append([float(n) for n in line.split()])

# 获取data元组中对应数据
pred = [row[2] for row in data]
high = [row[3] for row in data]
low = [row[4] for row in data]
times = [row[0] + row[1]/12.0 for row in data]

# LinePlot类实例化不需要任务参数，设置主要特性是:x。y、height、width和data，data点的坐标列表
lp = LinePlot()
lp.x = 50
lp.y = 50
lp.height = 125
lp.width = 300
lp.data = [zip(times, pred),zip(times,high),zip(times, low)]
# 为每条线调置笔画颜色
lp.lines[0].strokeColor = colors.blue
lp.lines[1].strokeColor = colors.red
lp.lines[2].strokeColor = colors.green

# 将设定的LinePlost类添加到drawing
drawing.add(lp)
# 添加一个String对象到drawing中
drawing.add(String(250,150, 'Sunspots',fontSize=14,fillColor=colors.red))
# renderPDF.drawToFile是把内容保存到report2.pdf
renderPDF.drawToFile(drawing, 'report3.pdf','Sunspots')
