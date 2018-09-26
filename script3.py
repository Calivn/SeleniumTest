# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time, os, re
import pprint

# <editor-fold desc="警告框处理">
"""
drive = webdriver.Firefox()
drive.implicitly_wait(10)

drive.get('http://www.baidu.com')

link = drive.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(drive).move_to_element(link).perform()

drive.find_element_by_xpath('//*[@id="wrapper"]/div[6]/a[1]').click()

drive.find_element_by_xpath('//*[@id="gxszButton"]/a[1]').click()

time.sleep(5)

a = drive.switch_to.alert.accept()  # 与旧方法switch_to_alert().accept语法的差异

drive.quit()

print("Yes")
"""
# </editor-fold>

# <editor-fold desc="文件上传">
"""
driver = webdriver.Firefox()

file_path = 'file:///' + os.path.abspath('upfile.html')
driver.get(file_path)

driver.find_element_by_name('file').send_keys('D:\\LR.txt')
"""
# </editor-fold>

# <editor-fold desc="从Teamcola导出日志">
"""
fp = webdriver.FirefoxProfile()
fp.set_preference("browser.download.folderList",2)
fp.set_preference("browser.download.manager.showWhenStarting",False)
fp.set_preference("browser.download.dir", os.getcwd())
fp.set_preference("browser.helperApps.neverAsk.saveToDisk", "text/csv")

driver = webdriver.Firefox(firefox_profile=fp)  # 此处设置，可以不弹出弹框，直接下载到指定路径

driver.get('https://nplus.teamcola.com/login/')

driver.find_element_by_xpath('//*[@id="username"]').send_keys('1231@231.com')
driver.find_element_by_xpath('//*[@id="pw"]').send_keys('213213')
driver.find_element_by_xpath('//*[@id="btn-login"]').submit()

time.sleep(2)
driver.find_element_by_xpath('//*[@id="btn-today"]').click()    #切换到当前一周

date_str = driver.find_element_by_xpath('//*[@id="my-worklog"]/div[3]/div[1]/div[1]/div[2]').text   # 获取当前一周日期

# 通过正则，将日期字符串中的中文替换为“-”，并切割字符串
ch_re = u'[\u4e00-\u9fa5]'
date_str = re.sub(ch_re, '-', date_str)     # 通过正则替换
date_list = date_str.split(' ~ ')

driver.find_element_by_xpath('//*[@id="link-export-worklogs"]').click()     # 导出

time.sleep(2)

driver.find_element_by_xpath('//*[@id="export-start-date"]').clear()
driver.find_element_by_xpath('//*[@id="export-start-date"]').send_keys(date_list[0].rstrip('-'))
driver.find_element_by_xpath('//*[@id="export-end-date"]').clear()
driver.find_element_by_xpath('//*[@id="export-end-date"]').send_keys(date_list[1].rstrip('-'))
driver.find_element_by_xpath('/html/body/div[3]/div[2]/button').click()

time.sleep(2)

driver.quit()
"""
# </editor-fold>

# <editor-fold desc="截屏">
"""
driver = webdriver.Firefox()

driver.get('http://www.baidu.com')

try:
    driver.find_element_by_xpath('xxxx').send_keys('nihao')

except:
    driver.save_screenshot("D:\\abc.png")

driver.quit()
"""
# </editor-fold>
