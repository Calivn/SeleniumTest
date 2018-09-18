# -*- coding: utf-8 -*-

from PIL import Image, ImageEnhance
import pytesseract

sonList = [['需求文档链接汇总'], ['5.1前端文档', '5.2后端文档', '5.2后端文档'], ['6.0 测试环境', '6.1测试用例', '6.2测试计划'], ['【V0.0.1】版本内容']]

for a in sonList[1]:
    print(a)