# -*- coding: utf-8 -*-

# <editor-fold desc="登陆126邮箱，并发送邮件">
from selenium import webdriver
import time

firstUrl = 'http://www.126.com'

drive = webdriver.Chrome()
drive.get(firstUrl)
time.sleep(5)

xx = drive.find_elements_by_tag_name('iframe')[0]
drive.switch_to.frame(xx)  # 切换frame
# drive.switch_to.frame('//*[@id="x-URS-iframe1543234481505.8179"]')
drive.find_element_by_xpath('//*[@name="email"]').send_keys('zhucheng139122@126.com')
drive.find_element_by_xpath('//*[@name="password"]').send_keys('qazs~19890518')
drive.find_element_by_xpath('//*[@id="dologin"]').click()
time.sleep(3)
drive.find_element_by_link_text(u"登录").click()

time.sleep(3)

drive.find_element_by_xpath('//*[@id="_mail_component_59_59"]').click()
time.sleep(2)
drive.find_element_by_xpath('//*[contains(@id,"_attachBrowser")]/input').send_keys('G:\\test.txt')
# drive.find_element_by_xpath('//*[@id="1543232660810_attachBrowser"]').send_keys('G:\\test.txt')

time.sleep(5)

# drive.quit()
# </editor-fold>
