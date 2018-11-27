from selenium import webdriver
import win32api, win32con
import time, logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s -  %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')
# logging.disable(logging.INFO)

logging.info('Start of program.')

drive = webdriver.Chrome()

# file_path = 'file:///' + os.path.abspath('frame.html')
# drive.implicitly_wait(10)

drive.get('http://www.baidu.com')
drive.find_element_by_id('kw').send_keys('abcd')
time.sleep(5)
drive.find_element_by_id('kw').send_keys('nihao')
logging.info('Ready to send key~')
time.sleep(5)

#   发送组合键
win32api.keybd_event(0x11, 0, 0, 0)
win32api.keybd_event(0x57, 0, 0, 0)
win32api.keybd_event(0x57, 0, win32con.KEYEVENTF_KEYUP, 0)
win32api.keybd_event(0x11, 0, win32con.KEYEVENTF_KEYUP, 0)
logging.info('Send key successfully!')