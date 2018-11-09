#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import sys
import time
import allure
import pytest

import biz.get_test_value_by_yaml as get_test_value_by_yaml
print(sys.path)


@pytest.fixture(scope='module')
def driver():
    driver = get_test_value_by_yaml.get_driver_by_key("Y66手机ip")
    driver.set_fastinput_ime(True)
    driver.session("com.bs.finance")
    yield driver
    driver.app_stop("com.bs.finance")


def save_picture(driver, picture_name):
    driver.screenshot(os.path.abspath('..') + "/report/picture/" + picture_name + ".png")
    return os.path.abspath('..')+"/report/picture/" + picture_name + ".png"


@allure.story('点击头像弹出侧边栏')
def test_one(driver):
    driver(resourceId="com.bs.finance:id/iv_user").click()
    time.sleep(1)
    picture_name = sys._getframe().f_code.co_name
    pictor_url = save_picture(driver, picture_name)
    file = open(pictor_url, 'rb').read()
    with allure.step("点击头像"):
        allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片
        assert 1 == 1

@allure.story('这个是第二条case')
def test_two(driver):
    assert 1 == 1




if __name__ == '__main__':
    # 执行所有case并生成报告
    pytest.main("--alluredir "+os.path.abspath('..') + "/report/xml")
    os.system("allure generate "+os.path.abspath('..') + "/report/xml -o "+os.path.abspath('..')+"/report/html --clean")
        # time.sleep(5)
        # os.system('allure open -h 127.0.0.1 -p 8083 /Users/xuchen/PycharmProjects/testAuto/report/html')

        # git push -u origin master 提交代码到主分支

        # 命令行运行生成报告
        # cd /Users/xuchen/PycharmProjects/testAuto
        # py.test test_case --alluredir /Users/xuchen/PycharmProjects/testAuto/report/xml
        # allure generate /Users/xuchen/PycharmProjects/testAuto/report/xml -o /Users/xuchen/PycharmProjects/testAuto/report/html --clean
