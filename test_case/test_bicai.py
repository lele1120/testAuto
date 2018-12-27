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

    # d.unlock()
    d.set_fastinput_ime(True)
    d.session("com.bs.finance")
    yield d
    # d.app_stop("com.bs.finance")


@allure.feature("01.启动app后进入比财")
@allure.severity('Critical')
def test_go_main_01(d):
    """
    首次启动app点击进入比财
    """
    # time.sleep(5)

    with allure.step("启动页点击进入比财"):

        click_element(d, "启动页进入比财")

    time.sleep(2)

    with allure.step("验证启动app点击进入比财是否进入首页"):

        assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

    time.sleep(2)

    display_picture(d, "app首页未登录")


@allure.feature("02.比财登录")
@allure.severity('Critical')
def test_login_02(d):
    """
    比财账号登录

    """
    global USER_ID   # 使用账号

    USER_ID = str(get_value("xc手机号"))

    picture_verification_code = str(get_value("四位图片验证码"))

    login_verification_code = str(get_value("登录验证码"))

    with allure.step("点击app首页一键登录"):
        click_element(d, "首页一键登录")

    # time.sleep(5)

    with allure.step("在登录页账号输入框输入账号"):
        input_element(d, "登录页账号输入框", USER_ID)

    # time.sleep(5)

    with allure.step("点击获取验证码"):
        click_element(d, "登录页获取验证码按钮")  # 点击获取验证码

    time.sleep(5)

    #  如果弹出4位数字图片验证码 此处需加if判断
    with allure.step("输入4位验证码"):
        input_element(d, "图片验证码输入框", picture_verification_code )

    # time.sleep(3)

    with allure.step("点击确认按钮"):
        click_element(d, "图片验证码确定按钮")

    # time.sleep(3)

    with allure.step("输入6位验证码"):
        input_element(d, "登录验证码输入框", login_verification_code)

    # time.sleep(3)
    with allure.step("点击立即登录"):
        click_element(d, "立即登录按钮")

    with allure.step("验证是否登录成功"):
        assert not d(resourceId=get_value("首页一键登录")).exists

    # time.sleep(3)

    display_picture(d, "app首页已登录")


@allure.feature("03.弹出侧边栏")
@allure.severity('Critical')
def test_sidebar_eject_03(d):
    """
     验证点击左上角图标弹出侧边栏功能
    """

    global cebian_button  # 侧边栏按钮

    global realname_status  # 实名认证状态

    cebian_button = ["我的关注", "我的消息", "比财钱包", "了解比财"]

    with allure.step("点击左上角图标"):
        click_element(d, "首页左上角图标")

        # time.sleep(3)

    with allure.step("检验侧边栏控件"):
        for i in range(cebian_button.__len__()):
            assert d(text=cebian_button[i]).exists  #验证侧边栏4个按钮控件存在

    with allure.step("验证账号为已登录状态，账号为" + USER_ID):
        user_id = d(resourceId=get_value("侧边栏账号")).get_text()
        assert user_id == USER_ID.replace((USER_ID[3:7]), "****")

    display_picture(d, "弹出侧边栏")

    # time.sleep(3)


@allure.feature("04.点击侧边栏目logo")
@allure.severity('Critical')
def test_logo_click_04(d):
    with allure.step("侧边栏logo点击"):
        click_element(d, "侧边栏logo")

    # time.sleep(3)

    with allure.step("验证是否跳转个人资料页"):

        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    personal_data = ["性别", "微信", "职业", "实名认证", "手机号", "所在地", "个性签名"]

    for i in range(personal_data.__len__()):
        assert d(text=personal_data[i]).exists  # 验证个人资料内内容是否存在

    display_picture(d, "个人资料")

    # time.sleep(3)


@allure.feature("05.点击昵称进入修改页")
@allure.severity('Critical')
def test_nickname_click_05(d):
    with allure.step("点击昵称跳转到修改昵称页"):
        click_element(d, "个人资料昵称")

    with allure.step("验证修改昵称页title"):
        assert_title(d, "修改昵称")  # 验证是否跳转成功

    # time.sleep(3)

    display_picture(d, "修改昵称页")


@allure.feature("06.修改昵称页修改昵称点击完成")
@allure.severity('Critical')
def test_complete_click_06(d):

    # time.sleep(3)

    with allure.step("修改昵称为Alex"):
        input_element(d, "昵称文本框", "Alex")

    # time.sleep(3)

    with allure.step("点击完成按钮返回个人资料页"):
        click_element(d, "完成按钮")

    # time.sleep(3)

    with allure.step("验证是否跳转个人资料页"):
        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    with allure.step("验证昵称是否修改成功"):
        assert d(resourceId=get_value("个人资料昵称")).get_text() == "Alex"

    # time.sleep(3)

    display_picture(d, "点击完成页面跳转修改昵称页")

    # 恢复数据
    click_element(d, "个人资料昵称")
    # time.sleep(1)
    input_element(d, "昵称文本框", USER_ID.replace((USER_ID[3:7]), "****"))
    # time.sleep(1)
    click_element(d, "完成按钮")


@allure.feature("07.修改昵称页点击返回icon")
@allure.severity('Critical')
def test_nickname_icon_click_07(d):
    with allure.step("点击昵称跳转到修改昵称页"):
        click_element(d, "个人资料昵称")

    with allure.step("验证修改昵称页是否跳转成功"):
        assert_title(d, "修改昵称")  # 验证是否跳转成功

    # time.sleep(3)

    with allure.step("修改昵称为Alex"):
        input_element(d, "昵称文本框", "Alex")

    # time.sleep(3)

    with allure.step("点击修改昵称页返回icon"):
        click_element(d, "返回icon")

    # time.sleep(3)

    with allure.step("验证是否跳转个人资料页"):
        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    with allure.step("验证昵称不会被修改"):
        assert d(resourceId=get_value("个人资料昵称")).get_text() == USER_ID.replace((USER_ID[3:7]), "****")

    display_picture(d, "修改昵称页点击返回icon跳转回个人资料页")


@allure.feature("08.修改性别")
@allure.severity('Critical')
def test_modify_sex_08(d):
    with allure.step("点击性别"):
        sex_text = d(resourceId=get_value("性别文本")).get_text()

        click_element(d, "性别")

    # time.sleep(3)

    with allure.step("修改性别"):
        if sex_text == "男":
            click_element(d, "选项女")
        elif sex_text == "女":
            click_element(d, "选项男")
        else:
            print("无此选项")

    time.sleep(3)

    with allure.step("验证性别修改是否成功"):
        modify_sex_text = d(resourceId=get_value("性别文本")).get_text()
        if sex_text == "男":
            assert modify_sex_text == "女"
        elif sex_text == "女":
            assert modify_sex_text == "男"
        else:
            print("无此选项")

    display_picture(d, "性别修改")


@allure.feature("09.修改职业")
@allure.severity('Critical')
def test_modify_profession_09(d):
    with allure.step("点击职业"):
        click_element(d, "职业")

    modify_profession_text = d(resourceId=get_value("职业文本")).get_text()

    with allure.step("修改职业"):
        if modify_profession_text == "测试":
            input_element(d, "职业文本", "码农")
        elif modify_profession_text == "码农":
            input_element(d, "职业文本", "测试")
        else:
            print("输入错误")

    with allure.step("点击完成"):
        click_element(d, "完成")

    with allure.step("验证是否修改成功"):
        modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

        if modify_profession_text == "测试":
            assert modify_profession_display == "码农"
        elif modify_profession_text == "码农":
            assert modify_profession_display == "测试"
        else:
            print("输入错误")

    display_picture(d, "职业页点击返回icon跳转回个人资料页")


@allure.feature("10.修改职业点击返回icon")
@allure.severity('Critical')
def test_modify_profession_icon_10(d):
    with allure.step("点击职业"):
        click_element(d, "职业")

    global modify_profession_text

    modify_profession_text = d(resourceId=get_value("职业文本")).get_text()

    with allure.step("修改职业"):
        if modify_profession_text == "测试":
            input_element(d, "职业文本", "码农")
        elif modify_profession_text == "码农":
            input_element(d, "职业文本", "测试")
        else:
            print("输入错误")

    with allure.step("点击返回icon"):
        click_element(d, "返回icon")

    with allure.step("验证职业是否被修改"):
        modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

        if modify_profession_text == "测试":
            assert modify_profession_display == "测试"
        elif modify_profession_text == "码农":
            assert modify_profession_display == "码农"
        else:
            print("输入错误")

    display_picture(d, "职业修改页点击返回icon跳转回个人资料页")


@allure.feature("11.修改职业输入框输入内容点击取消")
@allure.severity('Critical')
def test_modify_profession_clear_11(d):
    with allure.step("点击职业"):
        click_element(d, "职业")

    with allure.step("验证不存在清除按钮"):
        assert not d(resourceId=get_value("清除按钮")).exists

    with allure.step("修改职业文本框内容"):

        if modify_profession_text == "测试":
            input_element(d, "职业文本", "码农")
        elif modify_profession_text == "码农":
            input_element(d, "职业文本", "测试")
        else:
            print("输入错误")

    with allure.step("验证清除按钮存在"):

        assert d(resourceId=get_value("清除按钮")).exists

    with allure.step("点击清除按钮"):

        click_element(d, "清除按钮")

    with allure.step("文本内容被清除"):

        modify_profession_display = d(resourceId=get_value("职业文本")).get_text()

        assert modify_profession_display is None

        display_picture(d, "职业修改页输入后删除")

    click_element(d, "返回icon")




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
#             title = d(resourceId=get_value("个人资料标题")).get_text()
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


def click_element(d, element_name):
    """

    :param d: 控件默认为d
    :param element_name: 控件名称详见yaml文件
    :return: 无
    封装控件点击操作
    """
    d(resourceId=get_value(element_name)).wait(timeout=10.0)
    d(resourceId=get_value(element_name)).click()
    time.sleep(3)


def input_element(d, element_name, input_text):
    """

    :param d: 控件默认为d
    :param element_name: 控件名称详见yaml文件
    :param input_text: 需要输入的内容
    :return: 无
    """
    d(resourceId=get_value(element_name)).wait(timeout=10.0)
    d(resourceId=get_value(element_name)).set_text(input_text)
    time.sleep(3)


def assert_title(d, title):
    """

    :param d: 控件默认为d
    :param title: 页面标题
    :return: 无
    验证页面是否跳转成功

    """
    assert title == d(resourceId=get_value("标题")).get_text()
    time.sleep(3)


def display_picture(d, picture_name):
    """

    :param d: 控件名称，默认为d
    :param picture_name: 图片名称
    :return: 无
    """
    pictor_url = save_picture(d, picture_name)
    file = open(pictor_url, 'rb').read()
    allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片


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
    """

    :param key: 关键字
    :return:无
    """
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
