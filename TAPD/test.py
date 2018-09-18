# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains


def openProject(driver, projectName):
    # 进入项目
    driver.find_element_by_xpath('//*[@id="tree-wrapper"]/div[1]/a').click()
    try:
        driver.find_element_by_xpath('//a[contains(text(), "%s")]' % projectName).click()  # 模糊匹配项目名称
    except:
        print("项目不存在！请确认项目准确名称！")
        print("程序即将退出！")
        sleep(3)
        driver.quit()
    sleep(1)


def enableWiki(driver):
    print("\n正在启用Wiki~\n")
    try:
        more = driver.find_element_by_xpath('//*[@id="dropdown-nav-more"]/a/span')
        ActionChains(driver).move_to_element(more).perform()
        sleep(1)
        driver.find_element_by_xpath('//*[@id="dropdown-nav-more"]/div/ul/li[3]/a').click()
    except:
        driver.find_element_by_xpath('//*[@id="hd"]/div[5]/div[2]/a/i').click()

    driver.find_element_by_xpath('//a[contains(text(), "应用设置")]').click()
    driver.find_element_by_xpath('//*[@id="page-content"]/div/div/div[1]/div/div[2]/a').click()

    start = driver.find_element_by_xpath('//span[contains(text(), "Wiki")]')
    end1 = driver.find_element_by_xpath('//*[@id="visible-menu-list"]')
    end = driver.find_element_by_xpath('//span[contains(text(), "需求")]')
    actions = ActionChains(driver)
    actions.drag_and_drop_by_offset(start, xoffset=-2200, yoffset=20).click_and_hold().perform()
    # actions.drag_and_drop(start, end1).perform()
    sleep(5)
    # driver.find_element_by_xpath('//*[@id="config-menu-submit-span"]').click()
    print("\nWiki已成功启用~\n")


projectName = "模板项目"

tapdUrl = 'https://www.tapd.cn/cloud_logins/login'
driver = webdriver.Chrome()

driver.get(tapdUrl)
driver.find_element_by_xpath('//*[@id="username"]').send_keys('zhucheng@nplusgroup.com')
driver.find_element_by_xpath('//*[@id="password_input"]').send_keys('!QAZ2wsx')
driver.find_element_by_xpath('//*[@id="tcloud_login_button"]').submit()
print("登陆成功")

driver.find_element_by_xpath('//*[@id="tree-wrapper"]/div[1]/a').click()

openProject(driver, projectName)

enableWiki(driver)

print("即将退出程序~~")

sleep(3)

driver.quit()
