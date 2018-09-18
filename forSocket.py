# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from threading import Thread


def test_Socket(browser, url):
    driver = None

    if browser == "ie":
        driver = webdriver.Ie()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    elif browser == "chrome":
        driver = webdriver.Chrome()

    if driver is None:
        exit()

    driver.get(url)
    driver.find_element_by_xpath('/html/body/button[1]').click()
    time.sleep(1)
    driver.find_element_by_xpath('/html/body/div/input').send_keys("Hello man!")
    time.sleep(3)
    while True:
        driver.find_element_by_xpath('/html/body/div/button').click()
        time.sleep(8)


if __name__ == "__main__":

    data = {
        "ie": "http://120.26.247.216:8099/",
        "firefox": "http://120.26.247.216:8099/",
        "chrome": "http://120.26.247.216:8099/"
    }

    threads = []
    for b, url in data.items():
        t = Thread(target=test_Socket, args=(b, url))
        threads.append(t)

    for thr in threads:
        thr.start()
        time.sleep(2)
