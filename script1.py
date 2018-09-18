# -*- coding: utf-8 -*-

# <editor-fold desc="登陆126邮箱，并发送邮件">
from selenium import webdriver
import time

firstUrl = 'http://www.126.com'

drive = webdriver.Chrome()
drive.get(firstUrl)
time.sleep(5)

drive.switch_to.frame('x-URS-iframe')  # 切换frame

drive.find_element_by_xpath('//*[@name="email"]').send_keys('zhucheng139122')
drive.find_element_by_xpath('//*[@name="password"]').send_keys('qazs~19890518')
drive.find_element_by_xpath('//*[@id="dologin"]').click()
time.sleep(3)
drive.find_element_by_link_text(u"登录").click()

time.sleep(3)

drive.find_element_by_xpath('//*[@id="_mail_component_68_68"]').click()
time.sleep(2)
drive.find_element_by_class_name('nui-editableAddr-ipt').send_keys('zhucheng@nplusgroup.com')
drive.find_element_by_xpath('//*[@class="nui-ipt-input" and @tabindex="1"]').send_keys('abcdefg')   # 双重标签定位
drive.find_element_by_xpath('/html/body/div[2]/div[1]/div[2]/header/div/div[1]/div/span[2]').click()

time.sleep(5)

drive.quit()
# </editor-fold>
