# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from threading import Thread


def Chrome():
    driver = webdriver.Chrome()
    Sendkey(driver)


def Ie():
    driver = webdriver.Ie()
    Sendkey(driver)


def Firefox():
    driver = webdriver.Firefox()
    Sendkey(driver)


def Sendkey(driver):
    driver.get("http://120.26.247.216:8099/")
    driver.find_element_by_xpath('/html/body/button[1]').click()
    time.sleep(2)
    driver.find_element_by_xpath('/html/body/div/input').send_keys("Hello man!")
    time.sleep(2)
    while True:
        driver.find_element_by_xpath('/html/body/div/button').click()
        time.sleep(4)


if __name__ == "__main__":

    threads = []
    t = Thread(target=Chrome(), args=())
    threads.append(t)
    f = Thread(target=Ie(), args=())
    threads.append(f)
    g = Thread(target=Firefox(), args=())
    threads.append(g)

    # 启动所有线程
    for thr in threads:
        thr.start()
