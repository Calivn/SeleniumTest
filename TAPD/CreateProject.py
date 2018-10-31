# -*- coding: utf-8 -*-

from selenium import webdriver
from time import sleep
from os import _exit
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait


def login_tapd(driver, user, passwd):
    driver.get("https://www.tapd.cn/cloud_logins/login")
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(user)
    driver.find_element_by_xpath('//*[@id="password_input"]').send_keys(passwd)
    driver.find_element_by_xpath('//*[@id="tcloud_login_button"]').submit()
    print("登陆TAPD成功!")


def createProject(driver, proName):
    # 打开项目列表主页
    driver.find_element_by_xpath('//*[@id="tree-wrapper"]/div[1]/a').click()
    try:
        driver.find_element_by_xpath('//a[contains(text(), "%s")]' % proName)
        print("项目已存在,即将退出~~")
        sleep(3)
        driver.quit()
        _exit(0)
    except:
        # 点击创建项目
        try:
            driver.find_element_by_xpath('//*[@class="create-project"]').click()
            # 显式等待弹框打开
            WebDriverWait(driver, 10).until(
                EC.text_to_be_present_in_element((By.XPATH, '//*[@id="workspace-template-list"]/li[3]/div[1]'),
                                                 '轻量敏捷项目管理'))
            driver.find_element_by_xpath('/html/body/div[5]').find_element_by_xpath('//*[@id="name"]').send_keys(
                "%s" % proName)
            driver.find_element_by_xpath('//*[@id="tdialog-buttonwrap"]/a[1]').click()
            sleep(12)
            print("\n%s 项目创建成功！\n" % proName)
            sleep(1)
            driver.find_element_by_xpath('//*[@id="tdialog"]/div/div[1]/div[1]/i').click()
            sleep(3)
            drivers.find_element_by_xpath('/html/body/div[12]/div[2]/div[1]').click()
            sleep(1)
        except:
            print("请确认该账户是否具备项目创建权限！")
            drivers.quit()


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
        driver.find_element_by_xpath('//a[contains(text(), "Wiki")]')
        print("\nWiki已成功启用~\n")
    except:
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
    wikiTemp = ["【示例】代码规范", "【示例】知识沉淀", "【示例】迭代1回顾", "【示例】迭代回顾"]
    workList = ['1.项目背景', '2.项目需求', '3.UE设计', '4.UI设计', '5.开发文档', '6.测试', '7.项目部署', '版本记录']
    rootXpath = ['//a[@title="3.UE设计"]', '//a[@title="5.开发文档"]',
                 '//a[@title="6.测试"]', '//a[@title="版本记录"]']
    sonList = [['需求文档链接汇总'], ['5.1前端文档', '5.2后端文档', '5.3代码路径'], ['6.0 测试环境', '6.1测试用例', '6.2测试计划'], ['【V0.0.1】版本内容']]

    # 进入wiki
    driver.find_element_by_xpath('//a[contains(text(), "Wiki")]').click()
    sleep(1)

    # 删除wiki示例
    def getSwitchXpath(driver, name):
        FirstId = driver.find_element_by_xpath('//span[contains(text(), "%s")]' % name).get_attribute('id')
        switchXpath = FirstId[:-4] + 'switch'
        driver.find_element_by_xpath('//*[@id="%s"]' % switchXpath).click()

    try:
        getSwitchXpath(driver, "首页")
        sleep(1)
        for x in wikiTemp:
            if x == "【示例】代码规范":
                getSwitchXpath(driver, "【示例】知识沉淀")
            elif x == "【示例】迭代1回顾":
                getSwitchXpath(driver, "【示例】迭代回顾")
            sleep(2)
            driver.find_element_by_xpath('//span[contains(text(), "%s")]' % x).click()
            sleep(1)
            driver.find_element_by_xpath('//span[contains(@onclick, "%s")]' % x).click()
            sleep(2)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[4]/span').click()
            sleep(2)
            drivers.find_element_by_xpath('/html/body/div[8]/div[3]/div/a[1]').click()
    except:
        pass

    # 创建新的wiki目录
    for i in workList:
        sleep(2)
        driver.find_element_by_xpath('//span[contains(text(), "首页")]').click()
        driver.find_element_by_xpath('//span[contains(@onclick,"首页")]').click()
        sleep(1)
        try:
            sleep(1)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]').click()
        except:
            sleep(1)
            driver.find_element_by_xpath('//*[@id="diy_pop"]/ul/li[1]').click()
        while not driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').is_enabled():
            driver.refresh()
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
                driver.find_element_by_xpath('//span[contains(text(), "添加wiki页面")]').click()
            except:
                sleep(2)
                driver.find_element_by_xpath('//span[contains(text(), "添加wiki页面")]').click()
            sleep(2)
            while not driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').is_enabled():
                driver.refresh()
                sleep(2)
            driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys(a)
            driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()

    sleep(2)
    try:
        driver.find_element_by_xpath('//*[@id="page-content"]/div[1]/div/a/span').click()
        while not driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').is_enabled():
            driver.refresh()
            sleep(2)
        driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys('老版本文档链接汇总')
        driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()
    except:
        sleep(3)
        driver.find_element_by_xpath('//*[@id="page-content"]/div[1]/div/a/span').click()
        while not driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').is_enabled():
            driver.refresh()
            sleep(2)
        driver.find_element_by_xpath('//*[@id="WikiName"]').send_keys('老版本文档链接汇总')
        driver.find_element_by_xpath('//*[@id="wiki_div_submit"]').submit()

    print("\nWiki文档目录创建成功！\n")
    sleep(2)


def clearTemp(driver):
    """删除项目模板"""

    """清理需求模板"""
    print("开始清理模板需求~")
    try:
        driver.find_element_by_xpath('//a[@title="需求"]').click()
        sleep(2)
        requestXpath = driver.find_element_by_xpath('//a[contains(text(), "【示例】父需求")]')
        requestId = requestXpath.get_attribute('id')
        ActionChains(driver).move_to_element(requestXpath).perform()  # 悬停
        driver.find_element_by_xpath('//*[@id="tr_%s:"]/td[2]/div/div/div/a' % requestId).click()  # 根据id动态定位
        driver.find_element_by_xpath('//*[@id="%s-delete_story"]/a' % requestId[6:]).click()
        driver.find_element_by_xpath('/html/body/div[11]/div[3]/div/a[1]').click()
        print("模板需求已成功删除！")
    except:
        print("模板需求已清除~")

    """清理迭代模板"""
    print("开始清理模板迭代~")
    try:
        homeWindows = driver.current_window_handle
        driver.find_element_by_xpath('//a[contains(text(), "迭代")]').click()
        sleep(1)
        driver.find_element_by_xpath('//a[contains(text(), "【示例】父需求")]').click()
        sleep(1)
        allWindows = driver.window_handles
        for handle in allWindows:
            if handle != homeWindows:
                driver.switch_to.window(handle)
                sleep(1)
                # 删除迭代模板
                driver.find_element_by_xpath('//*[@id="locate_more_operations "]/a/span').click()
                driver.find_element_by_xpath('//*[@id="delete_story"]').click()
                driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/a[1]/span').click()
                sleep(1)
                driver.close()
        driver.switch_to.window(homeWindows)
        print("模板迭代已成功删除！")
    except:
        print("模板迭代已清除~")

    """清理BUG模板"""
    print("开始清理模板BUG~")
    try:
        driver.find_element_by_xpath('//a[@title="缺陷"]').click()
        for i in [2, 1]:
            bugName = "【示例】缺陷" + str(i)
            bugXpath = driver.find_element_by_xpath('//a[contains(text(), "%s")]' % bugName)
            ActionChains(driver).move_to_element(bugXpath).perform()
            sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="bug_list_content"]/tbody/tr[%d]/td[2]/div/div[1]/div/a' % (i + 1)).click()
            sleep(1)
            driver.find_element_by_xpath(
                '//*[@id="bug_list_content"]/tbody/tr[%d]/td[2]/div/div[1]/div/div/ul/li[3]/a/i' % (i + 1)).click()
            driver.find_element_by_xpath('/html/body/div[7]/div[3]/div/a[1]').click()
        print("模板BUG已成功删除！")
    except:
        print("模板BUG已清除~")


if __name__ == '__main__':
    username = input("请输入你的TAPD账户：\n(即企业邮箱，请务必确保该账户有项目创建权限)\n")
    password = input("\n请输入你的账户密码：")
    proName = input("\n请输入项目名称：\n（项目名称请输入中英文、下划线、空格、英文句号和数字，且只能以中英文开头，不超过30字符）\n")
    # tapdUrl = 'https://www.tapd.cn/cloud_logins/login'
    print('''
1、完整创建项目                2、仅创建Wiki目录
3、仅同步需求&缺陷工作流       4、仅清除项目模板
            ''')
    select = str(input())
    # 显式调用浏览器
    drivers = webdriver.Chrome()

    # 隐式调用浏览器
    # option = webdriver.ChromeOptions()
    # option.add_argument("headless")
    # drivers = webdriver.Chrome(chrome_options=option)

    tag = True
    while tag:
        if select == '1':
            login_tapd(drivers, username, password)

            # 创建项目
            createProject(drivers, proName)
            openProject(drivers, proName)

            # 删除项目模板
            clearTemp(drivers)

            # 创建BUG报告
            createReport(drivers)
            oldProject = '模板项目'

            # 复制项目需求&BUG工作流
            copyFlow(drivers, proName, oldProject)

            openProject(drivers, proName)

            # 配置Wiki
            enableWiki(drivers)
            createWiki(drivers)
            tag = False
        elif select == '2':
            login_tapd(drivers, username, password)
            openProject(drivers, proName)

            # 配置Wiki
            enableWiki(drivers)
            createWiki(drivers)
            tag = False
        elif select == '3':
            login_tapd(drivers, username, password)
            openProject(drivers, proName)
            oldProject = '模板项目'
            copyFlow(drivers, proName, oldProject)
            tag = False
        elif select == '4':
            login_tapd(drivers, username, password)
            openProject(drivers, proName)

            # 删除项目模板
            clearTemp(drivers)
            tag = False
        else:
            print("请重新选择！")

    print("已完成，即将关闭程序~")
    sleep(3)
    drivers.quit()
