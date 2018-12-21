#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import re
import sys
import time
import allure
import pytest
import yaml
import uiautomator2 as u2
from pathlib import Path
from optparse import OptionParser


@pytest.fixture(scope='module')
def d():
    d = get_driver_by_key(sys.argv[1])  # 输入参数启动
    # d = get_driver_by_key("Y66手机ip")   # 输入手机ip启动app
    # d = get_driver_by_key("Y66手机udid")   # 输入手机udid启动

    d.unlock()
    # d.set_fastinput_ime(True)
    d.session("com.bs.finance")
    yield d
    # d.app_stop("com.bs.finance")


@allure.feature("启动app后进入比财")
@allure.story("点击进入比财")
@allure.severity('Critical')
def test_go_main_01(d):
    time.sleep(2)
    with allure.step("启动页点击进入比财"):
        d(resourceId=get_value("启动页进入比财")).click()

    with allure.step("验证启动app点击进入比财是否进入首页"):
        login_button_text = d(resourceId=get_value("首页一键登录")).get_text()

        assert login_button_text == "一键登录"

    time.sleep(2)


# @allure.feature("启动app后进入比财")
@allure.story("比财登录")
@allure.severity('Critical')
def test_login_02(d):

    global USER_ID   # 使用账号

    USER_ID = str(get_value("xc手机号"))

    picture_verification_code = str(get_value("四位图片验证码"))

    login_verification_code = str(get_value("登录验证码"))

    with allure.step("点击app首页一键登录"):
        d(resourceId=get_value("首页一键登录")).click()

    with allure.step("在登录页账号输入框输入账号"):
        d(resourceId=get_value("登录页账号输入框")).set_text(USER_ID)  # 输入账号

    time.sleep(2)

    with allure.step("点击获取验证码"):
        d(resourceId=get_value("登录页获取验证码按钮")).click()  # 点击获取验证码

    time.sleep(2)

    #  如果弹出4位数字图片验证码
    with allure.step("输入4位验证码"):
        d(resourceId=get_value("图片验证码输入框")).set_text(picture_verification_code)  # 输入4位验证码

    time.sleep(2)

    with allure.step("点击确认按钮"):
        d(resourceId=get_value("图片验证码确定按钮")).click()

    time.sleep(2)

    with allure.step("输入6位验证码"):
        d(resourceId=get_value("登录验证码输入框")).set_text(login_verification_code)

    time.sleep(2)
    with allure.step("点击立即登录"):
        d(resourceId=get_value("立即登录按钮")).click()

    with allure.step("验证是否登录成功"):
        assert not d(resourceId=get_value("首页一键登录")).exists



# @allure.story("验证侧边栏功能_用户登录状态")
# @allure.severity('Critical')
# def test_cebian_function_login_status_01(d):
#     """
#      验证侧边栏功能_用户登录状态
#     """
#

#
#     global cebian_button  # 侧边栏按钮
#
#     global realname_status  # 实名认证状态
#

#
#     cebian_button = ["我的消息", "比财钱包", "我的关注", "了解比财"]
#
#     time.sleep(5)
#
#     with allure.step("点击左上角图标"):
#         d(resourceId=get_value("首页左上角图标")).click()
#
#     with allure.step("获取侧边栏账号文本"):
#         user_id = d(resourceId=get_value("侧边栏账号")).get_text()
#
#     with allure.step("验证账号为已登录状态，账号为" + USER_ID):
#         assert user_id == USER_ID.replace((USER_ID[3:7]), "****")
#
#
# @allure.story("验证侧边栏功能_个人资料")
# def test_cebian_function_realname_status_02(d):
#     """
#         验证侧边栏功能_个人资料
#     """
#     with allure.step("点击是侧边栏logo"):
#         d(resourceId=get_value("侧边栏目logo")).click(timeout=2)
#
#         realname_status = d(resourceId=get_value("个人资料实名认证")).get_text()
#
#     with allure.step("点击返回icon"):
#         d(resourceId=get_value("返回icon")).click(timeout=2)
#
#
# @allure.story("验证侧边栏功能_用户是否实名")
# def test_cebian_function_authentication_03(d):
#     """
#      验证侧边栏功能_用户是否实名
#     """
#
#     with allure.step("点击是否实名"):
#         user_id = d(resourceId=get_value("是否实名")).get_text()
#         d(resourceId=get_value("是否实名")).click(timeout=2)
#
#     with allure.step("点击返回icon"):
#         d(resourceId=get_value("返回icon")).click(timeout=2)
#
#     with allure.step("点击是否绑卡"):
#         user_id = d(resourceId=get_value("是否绑卡")).get_text()
#         d(resourceId=get_value("是否绑卡")).click(timeout=2)
#
#     with allure.step("点击返回icon"):
#         d(resourceId=get_value("返回icon")).click(timeout=2)
#
#
# @allure.story("验证侧边栏功能_功能键_我的消息跳转")
# def test_cebian_function_first_key_04(d):
#     """
#      验证侧边栏功能_功能键_我的消息跳转
#     """
#
#     for i in range(cebian_button.__len__()):
#         with allure.step("点击"+cebian_button[i]):
#             d(text=cebian_button[i]).click(timeout=3)
#         with allure.step("验证点击"+cebian_button[i]+"能否跳转"):
#             time.sleep(5)
#             title = d(resourceId=get_value("标题")).get_text()
#
#             if i == 0:
#                 try:
#                     assert title == (cebian_button[i])[2:4]
#                     picture_name = cebian_button[i]
#                     pictor_url = save_picture(d, picture_name)
#                     file = open(pictor_url, 'rb').read()
#                     allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片
#                 except Exception as msg:
#                     picture_name = cebian_button[i]
#                     pictor_url = save_picture(d, picture_name)
#                     file = open(pictor_url, 'rb').read()
#                     allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片
#                     print(msg)
#             else:
#                 try:
#                     assert title == cebian_button[i]
#                     picture_name = cebian_button[i]
#                     pictor_url = save_picture(d, picture_name)
#                     file = open(pictor_url, 'rb').read()
#                     allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片
#                 except Exception as msg:
#                     picture_name = sys._getframe().f_code.co_name + str[i]
#                     pictor_url = save_picture(d, picture_name)
#                     file = open(pictor_url, 'rb').read()
#                     allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片、
#                     print(msg)
#
#         with allure.step("点击返回icon"):
#             d(resourceId=get_value("返回icon")).click(timeout=1)

    # time.sleep(1)
    # picture_name = sys._getframe().f_code.co_name
    # pictor_url = save_picture(d, picture_name)
    # file = open(pictor_url, 'rb').read()


    # with allure.step("点击头像"):
    #     allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片
    #     assert 1 == 1


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
                d = u2.connect_wifi(get_value(key))
                return d
            else:
                print("未发现ip为" + ip + "的移动设备")
        elif key[-1] == "d":
            uuid = get_value(key)
            readDeviceId = list(os.popen('adb devices').readlines())
            deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
            if uuid == deviceId:
                d = u2.connect_usb(uuid)
                return d
            else:
                print("未发现udid为"+uuid+"的移动设备")
    else:
        print("请使用yaml文件中的设备连接名称")


def save_picture(d, picture_name):
    # picture_url = Path(os.path.abspath('.') + "/report/picture/" + picture_name + ".png")  # 适用于jenkins运行
    picture_url = Path(os.path.abspath('..') + "/report/picture/" + picture_name + ".png")  # 适用于本地调试
    d.screenshot(picture_url)
    return picture_url


if __name__ == '__main__':
    """
    执行所有case并生成报告
    """

    # pytest.main("--alluredir " + str(Path(os.path.abspath('..') + "/report/xml")))
    #
    # os.system("allure generate " + str(Path(os.path.abspath('..') + "/report/xml -o " + os.path.abspath('..') +
    #                                         "/report/html --clean")))

    pytest.main("--alluredir ${WORKSPACE}/report")

    os.system("allure generate ${WORKSPACE}/report/xml -o ${WORKSPACE}/report/html --clean")

        # time.sleep(5)
        # os.system('allure open -h 127.0.0.1 -p 8083 /Users/xuchen/PycharmProjects/testAuto/report/html')

        # git push -u origin master 提交代码到主分支

        # 命令行运行生成报告
        # cd /Users/xuchen/PycharmProjects/testAuto
        # py.test test_case --alluredir /Users/xuchen/PycharmProjects/testAuto/report/xml
        # allure generate /Users/xuchen/PycharmProjects/testAuto/report/xml -o /Users/xuchen/PycharmProjects/testAuto/report/html --clean
