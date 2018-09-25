# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from os import _exit
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def loginTapd(driver, url):
    driver.get(url)
    driver.find_element_by_xpath('//*[@id="username"]').send_keys('1234@1234.com')
    driver.find_element_by_xpath('//*[@id="password_input"]').send_keys('134567')
    driver.find_element_by_xpath('//*[@id="tcloud_login_button"]').submit()
    print("登陆TAPD成功!")


def createProject(driver, proName):
    # 打开项目列表主页
    driver.find_element_by_xpath('//*[@id="tree-wrapper"]/div[1]/a').click()
    # sleep(2)
    # 点击创建项目
    driver.find_element_by_xpath('//*[@class="create-project"]').click()
    # 显式等待弹框打开
    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.XPATH, '//*[@id="workspace-template-list"]/li[3]/div[1]'), '轻量敏捷项目管理'))
    driver.find_element_by_xpath('/html/body/div[5]').find_element_by_xpath('//*[@id="name"]').send_keys("%s" % proName)
    driver.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]').click()
    print("\n%s 项目创建成功！\n" % proName)
    print("\n请稍等，即将进入项目配置环节！请稍等！\n")


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
        _exit(0)
    sleep(1)


def createReport(driver):
    print("\n开始配置“缺陷统计报表”，请稍等~\n")
    reportName = ['severity', 'status']
    for i in reportName:
        WebDriverWait(driver, 10).until(
            EC.text_to_be_present_in_element((By.XPATH, '//*[@id="hd"]/div[5]/ul/li[6]/a'), '报表'))
        # 进入报表
        driver.find_element_by_xpath('//*[@id="hd"]/div[5]/ul/li[6]/a').click()
        sleep(1)

        # 进入缺陷统计
        driver.find_element_by_xpath('//*[@id="page-content"]/div[1]/a[1]').click()
        driver.find_element_by_xpath('//*[@id="page-content"]/div[2]/div[1]/div/a').click()
        sleep(1)

        # 设置报表筛选条件
        Select(driver.find_element_by_name('data[Bugreport][disxAxis]')).select_by_value('reporter')
        Select(driver.find_element_by_name('data[Bugreport][disyAxis]')).select_by_value(i)
        Select(driver.find_element_by_name('data[Bugreport][time_type]')).select_by_value('1')

        # 生成报表，并保存
        driver.find_element_by_xpath('//*[@id="distributing_chart_form"]/div[1]/div[2]/div[1]/div/a').submit()
        driver.find_element_by_xpath('//*[@id="save-report-new"]').click()
        # driver.find_element_by_xpath('//*[@id="report_title"]').send_keys('BUG跟踪')

        sleep(2)  # 这个sleep时间，用于div弹框打开
        driver.find_element_by_xpath('/html/body/div[9]').find_element_by_xpath('//*[@id="report_title"]').send_keys(
            i)  # div模拟的弹框，通过两层定位的方式确认位置
        driver.find_element_by_xpath('/html/body/div[9]').find_element_by_xpath(
            '/html/body/div[9]/div[3]/div/a[1]/span').click()

    print("\n缺陷统计报表创建成功！\n")
    sleep(2)


def createFolder(driver, projectID):
    print("开始配置“文档目录”，请稍等~")
    folderName = ['设计文档', '开发文档', '需求文档', '测试文档']

    # 进入文档
    driver.find_element_by_xpath('//*[@id="hd"]/div[5]/ul/li[5]/a').click()

    for i in folderName:
        # 创建文件夹
        buildfolder = driver.find_element_by_xpath('//*[@id="add-folder-btn"]')
        ActionChains(driver).move_to_element(buildfolder).perform()
        driver.find_element_by_xpath('//*[@id="add-new-document-folder"]').click()
        driver.find_element_by_xpath('/html/body/div[7]').find_element_by_xpath('//*[@id="folder_name"]').send_keys(
            "%s %s" % (projectID, i))
        driver.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]/span').click()

    print("文档目录创建成功！")
    sleep(2)


def copyFlow(driver, newProject, oldProject):
    print("\n开始从“%s”项目，同步需求&缺陷工作流，请稍等~\n" % oldProject)
    driver.find_element_by_xpath('//*[@id="tree-wrapper"]/div[1]/a').click()
    try:
        driver.find_element_by_xpath('//a[contains(text(), "%s")]' % oldProject).click()
    except:
        print("项目不存在！")

    testlist = ['需求', '缺陷']

    for i in testlist:
        sleep(2)
        try:
            more = driver.find_element_by_xpath('//*[@id="dropdown-nav-more"]/a/span')
            ActionChains(driver).move_to_element(more).perform()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="dropdown-nav-more"]/div/ul/li[3]/a').click()
        except:
            driver.find_element_by_xpath('//*[@id="hd"]/div[5]/div[2]/a/i').click()
        sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="page-content"]/div[1]/div[1]/div/div/ul/li[2]').find_element_by_link_text("%s" % i).click()
        driver.find_element_by_xpath('//*[@id="page-content"]/div/div/div[1]/div/div[2]/a').click()
        dri = driver.find_element_by_xpath('/html/body/div[8]')

        # 显式等待
        # WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.XPATH,'//*[@id="dialog"]'), newProject))

        sleep(3)
        dri.find_element_by_xpath('//input[@project="%s"]' % newProject).click()
        driver.find_element_by_xpath('/html/body/div[8]/div[3]/div/a[1]').click()
        driver.find_element_by_xpath('/html/body/div[8]').find_element_by_xpath(
            '/html/body/div[8]/div[3]/div/a[1]').click()
        print("\n%s工作流程已经完成同步！\n" % i)
        sleep(2)


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
    end = driver.find_element_by_xpath('//span[contains(text(), "需求")]')
    actions = ActionChains(driver)
    actions.drag_and_drop(start, end).perform()
    sleep(2)
    driver.find_element_by_xpath('//*[@id="config-menu-submit-span"]').click()
    print("\nWiki已成功启用~\n")


def createWiki(driver):
    print("开始配置“Wiki目录”，请稍等~")
    wikiTemp = ['//*[@id="wiki_structure_5_a"]', '//*[@id="wiki_structure_4_a"]',
                '//*[@id="wiki_structure_3_a"]', '//*[@id="wiki_structure_2_a"]', ]
    workList = ['1.项目背景', '2.项目需求', '3.UE设计', '4.UI设计', '5.开发文档', '6.测试', '7.项目部署', '版本记录']
    rootXpath = ['//a[@title="3.UE设计"]', '//a[@title="5.开发文档"]',
                 '//a[@title="6.测试"]', '//a[@title="版本记录"]']
    sonList = [['需求文档链接汇总'], ['5.1前端文档', '5.2后端文档', '5.3代码路径'], ['6.0 测试环境', '6.1测试用例', '6.2测试计划'], ['【V0.0.1】版本内容']]

    # 进入文档
    driver.find_element_by_xpath('//a[contains(text(), "Wiki")]').click()
    sleep(1)

    # 删除wiki示例
    try:
        driver.find_element_by_xpath('//*[@id="wiki_structure_1_switch"]').click()
        sleep(1)
        for x in wikiTemp:
            if x == '//*[@id="wiki_structure_5_a"]':
                drivers.find_element_by_xpath('//*[@id="wiki_structure_4_switch"]').click()
            elif x == '//*[@id="wiki_structure_3_a"]':
                drivers.find_element_by_xpath('//*[@id="wiki_structure_2_switch"]').click()
            sleep(2)
            buildfolder = driver.find_element_by_xpath(x)
            ActionChains(driver).move_to_element(buildfolder).perform()
            buildfolder.find_element_by_class_name('dropdown-toggle').click()
            sleep(1)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[4]/span').click()
            # abc = driver.find_element_by_xpath('/html/body/div[8]')
            sleep(2)
            drivers.find_element_by_xpath('/html/body/div[8]/div[3]/div/a[1]').click()
    except:
        pass

    # 创建新的wiki目录
    for i in workList:
        sleep(2)
        driver.find_element_by_xpath('//*[@id="wiki_structure_1_span"]').click()
        driver.find_element_by_xpath('//*[@id="diyBtn_wiki_structure_1"]/span').click()
        try:
            sleep(1)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]/span').click()
        except:
            sleep(2)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]/span').click()
        sleep(2)
        driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys(i)
        driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()

    # 创建wiki子目录
    for i in range(0, len(rootXpath) - 1):
        for a in sonList[i]:
            sleep(2)
            folder = driver.find_element_by_xpath(rootXpath[i])
            folder.click()
            folder.find_element_by_class_name('dropdown-toggle').click()
            try:
                sleep(1)
                driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]/span').click()
            except:
                sleep(2)
                driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]/span').click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys(a)
            driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()

    sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="page-content"]/div[1]/div/a/span').click()
        driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys('老版本文档链接汇总')
        driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()
    except:
        sleep(3)
        driver.find_element_by_xpath('//*[@id="page-content"]/div[1]/div/a/span').click()
        driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys('老版本文档链接汇总')
        driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()

    print("\nWiki文档目录创建成功！\n")
    sleep(2)


if __name__ == '__main__':
    proName = input("请输入项目名称：")
    # projectId = input("输入项目号：")

    # proName = "Pepper平板展示"
    # projectId = "testid"

    tapdUrl = 'https://www.tapd.cn/cloud_logins/login'

    # 显式调用浏览器
    drivers = webdriver.Chrome()

    # 隐式调用浏览器
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # drivers = webdriver.Chrome(chrome_options=option)

    loginTapd(drivers, tapdUrl)

    # 创建项目
    createProject(drivers, proName)
    sleep(12)
    openProject(drivers, proName)

    # 创建BUG报告
    createReport(drivers)

    # createFolder(drivers, projectId)
    # oldProject = input("\n您想从哪个项目复制需求&BUG的工作流程：\n")
    oldProject = '模板项目'

    # 复制项目需求&BUG工作流
    copyFlow(drivers, proName, oldProject)

    openProject(drivers, proName)

    # 配置Wiki
    enableWiki(drivers)
    createWiki(drivers)

    print("Program will now quit~")
    sleep(3)
    drivers.quit()
