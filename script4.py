# -*- coding: utf-8 -*-

# 图片识别

from PIL import Image
import pytesseract
from selenium import webdriver
import time

driver = webdriver.Firefox()
driver.get('http://km.nplusgroup.com/public/login.htm')

driver.get_screenshot_as_file('D:\\SeleniumTest\\yanzhengma\\image1.png')

im = Image.open('D:\\SeleniumTest\\yanzhengma\\image1.png')
box = (516, 417, 564, 437)  # 设置要裁剪的区域
region = im.crop(box)
region.save("D:\\SeleniumTest\\image_code.png")

time.sleep(3)

image_code = Image.open('image_code.png')

code_text = pytesseract.image_to_string(image_code)

print(code_text)