# coding:utf-8
'''
Created on 2016年10月11日

@author: admin
'''
import os


class FileWriter:
    def __init__(self,fileDir,fileName,format):
        self.mkDir(fileDir)
        self.f = open(fileDir+u"/"+fileName,format)

    def mkDir(self,path):
        isExists = os.path.exists(path)
        if not isExists:
            os.makedirs(path)
    def write(self,contents):
        return self.f.write(contents)

    def close(self):
        self.f.close()
