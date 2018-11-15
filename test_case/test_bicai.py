#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import sys
import time
import allure
import pytest
import yaml
import uiautomator2 as u2
from pathlib import Path
from optparse import OptionParser


@pytest.fixture(scope='module')
def driver():
    # driver = get_driver_by_key(sys.argv[1])
    driver = get_driver_by_key("Y66手机ip")
    driver.set_fastinput_ime(True)
    driver.session("com.bs.finance")
    yield driver
    driver.app_stop("com.bs.finance")


def save_picture(driver, picture_name):
    # picture_url = Path(os.path.abspath('.') + "/report/picture/" + picture_name + ".png")  # 适用于jenkins运行
    picture_url = Path(os.path.abspath('..') + "/report/picture/" + picture_name + ".png")  # 适用于本地调试
    driver.screenshot(picture_url)
    return picture_url


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




def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key值
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(key, val_, (list, tuple)):
            _get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身


def get_value(key):
    # yamlPath = Path(os.path.abspath('.')+"/usage/cfgyaml") # 适用于jenkins持续集成
    yamlPath = Path(os.path.abspath('..')+"/usage/cfgyaml") # 适用于本地调试持续集成

    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)
    return get_target_value(key, d, [])[0]


def get_driver_by_key(key):
    """
    :param key:使用yaml文件中的设备usb连接名称，或者ip连接名称，自动识别设备，使用ping ip和adb devices的方式判断设备是否可用
    :return: 返回设备driver
    """
    if type(key) == str:
        if key[-1] == "p":
            ip = get_value(key)
            backinfo = os.system("ping -c 5 "+ip)
            if backinfo == 0:
                driver = u2.connect_wifi(get_value(key))
                return driver
            else:
                print("未发现ip为" + ip + "的移动设备")
        elif key[-1] == "d":
            uuid = get_value(key)
            readDeviceId = list(os.popen('adb devices').readlines())
            deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
            if uuid == deviceId:
                driver = u2.connect_usb(uuid)
                return driver
            else:
                print("未发现udid为"+uuid+"的移动设备")
    else:
        print("请使用yaml文件中的设备连接名称")


if __name__ == '__main__':
#     # 执行所有case并生成报告

    pytest.main("--alluredir " + str(Path(os.path.abspath('..') + "/report/xml")))
    os.system("allure generate " + str(Path(os.path.abspath('..') + "/report/xml -o "+os.path.abspath('..') +
              "/report/html --clean")))
        # time.sleep(5)
        # os.system('allure open -h 127.0.0.1 -p 8083 /Users/xuchen/PycharmProjects/testAuto/report/html')

        # git push -u origin master 提交代码到主分支

        # 命令行运行生成报告
        # cd /Users/xuchen/PycharmProjects/testAuto
        # py.test test_case --alluredir /Users/xuchen/PycharmProjects/testAuto/report/xml
        # allure generate /Users/xuchen/PycharmProjects/testAuto/report/xml -o /Users/xuchen/PycharmProjects/testAuto/report/html --clean
