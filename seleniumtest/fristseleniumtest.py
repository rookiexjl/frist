# coding:utf-8
'''
Created on 2016年9月23日

@author: admin
'''
import os
from selenium import webdriver

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver
driver = webdriver.Chrome(chromedriver)
driver.get('http://www.baidu.com.cn')

driver.find_element_by_id('kw').send_keys('Selenium2')
driver.find_element_by_id('su').click()
driver.quit()
