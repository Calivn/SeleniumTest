# -*- coding: utf-8 -*-
"""
窗口切换
启用&关闭日志调试
"""

from selenium import webdriver
import time, logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
# logging.disable(logging.INFO)

logging.info('Start of program')

drive = webdriver.Firefox()

# file_path = 'file:///' + os.path.abspath('frame.html')

drive.implicitly_wait(10)

drive.get('http://www.baidu.com')

seach_windows = drive.current_window_handle

logging.info('The seach_windows is "%s"' % str(seach_windows))

drive.find_element_by_xpath('//*[@id="u1"]/a[7]').click()
drive.find_element_by_xpath('//*[@id="passport-login-pop-dialog"]/div/div/div/div[4]/a').click()

time.sleep(5)

all_handles = drive.window_handles
logging.info('The all_handles is "%s"' % str(all_handles))

for i in all_handles:
    if i != seach_windows:
        drive.switch_to.window(i)
        print("Now, show register window")
        drive.find_element_by_xpath('//*[@id="TANGRAM__PSP_3__userName"]').send_keys('abcdeftg')

time.sleep(6)

for i in all_handles:
    if i == seach_windows:
        drive.switch_to.window(i)
        print("Now, show seach window")
        drive.find_element_by_xpath('//*[@id="TANGRAM__PSP_4__closeBtn"]').click()
        drive.find_element_by_xpath('//*[@id="kw"]').send_keys('你好')
        drive.find_element_by_xpath('//*[@id="su"]').click()

logging.info('End of program')

time.sleep(4)

drive.quit()