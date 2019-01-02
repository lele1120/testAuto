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
import warnings
warnings.filterwarnings("ignore")
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
    d.app_stop("com.bs.finance")


@allure.feature("01.启动app后进入比财")
@allure.severity('Critical')
def test_go_main_01(d):
    """
    首次启动app点击进入比财
    """
    time.sleep(5)

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

    with allure.step("在登录页账号输入框输入账号"):
        input_element(d, "登录页账号输入框", USER_ID)

    with allure.step("点击获取验证码"):
        click_element(d, "登录页获取验证码按钮")  # 点击获取验证码

    #  如果弹出4位数字图片验证码 此处需加if判断
    with allure.step("输入4位验证码"):
        time.sleep(2)
        if d(text=u"请填写图像验证码").exists:
            input_element(d, "图片验证码输入框", picture_verification_code )
            with allure.step("点击确认按钮"):
                click_element(d, "图片验证码确定按钮")

    with allure.step("输入6位验证码"):
        input_element(d, "登录验证码输入框", login_verification_code)

    with allure.step("点击立即登录"):
        click_element(d, "立即登录按钮")

    with allure.step("验证是否登录成功"):
        assert not d(resourceId=get_value("首页一键登录")).exists

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

    with allure.step("检验侧边栏控件"):
        for i in range(cebian_button.__len__()):
            assert d(text=cebian_button[i]).exists  #验证侧边栏4个按钮控件存在

    with allure.step("验证账号为已登录状态，账号为" + USER_ID):
        user_id = d(resourceId=get_value("侧边栏账号")).get_text()
        assert user_id == USER_ID.replace((USER_ID[3:7]), "****")

    display_picture(d, "弹出侧边栏")


@allure.feature("04.点击侧边栏目logo")
@allure.severity('Critical')
def test_logo_click_04(d):
    """
    验证点击侧边栏logo会跳转正确跳到个人资料页，及个人资料页内控件元素存在校验
    :param d:
    :return: 无
    """
    with allure.step("侧边栏logo点击"):
        click_element(d, "侧边栏logo")

    with allure.step("验证是否跳转个人资料页"):

        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    personal_data = ["性别", "微信", "职业", "实名认证", "手机号", "所在地", "个性签名"]

    global Real_Name_Authentication  # 实名认证状态

    Real_Name_Authentication = d(resourceId=get_value("实名认证状态")).get_text()

    for i in range(personal_data.__len__()):
        assert d(text=personal_data[i]).exists  # 验证个人资料内内容是否存在

    display_picture(d, "个人资料")


@allure.feature("05.点击昵称进入修改页")
@allure.severity('Critical')
def test_nickname_click_05(d):
    """
    验证点击昵称可正确跳转修到昵称修改页
    :param d:
    :return:
    """
    with allure.step("点击昵称跳转到修改昵称页"):
        click_element(d, "个人资料昵称")

    with allure.step("验证修改昵称页title"):
        assert_title(d, "修改昵称")  # 验证是否跳转成功

    display_picture(d, "修改昵称页")


@allure.feature("06.修改昵称页修改昵称点击完成")
@allure.severity('Critical')
def test_complete_click_06(d):
    """
    昵称修改后点击完成验证个人资料页是否显示修改后昵称
    :param d:
    :return:
    """

    with allure.step("修改昵称为Alex"):
        input_element(d, "昵称文本框", "Alex")

    with allure.step("点击完成按钮返回个人资料页"):
        click_element(d, "完成按钮")

    with allure.step("验证是否跳转个人资料页"):
        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    with allure.step("验证昵称是否修改成功"):
        assert d(resourceId=get_value("个人资料昵称")).get_text() == "Alex"

    display_picture(d, "点击完成页面跳转修改昵称页")

    # 恢复数据
    click_element(d, "个人资料昵称")

    input_element(d, "昵称文本框", USER_ID.replace((USER_ID[3:7]), "****"))

    click_element(d, "完成按钮")


@allure.feature("07.修改昵称页点击返回icon")
@allure.severity('Critical')
def test_nickname_icon_click_07(d):
    """
    修改昵称后点击返回icon，查看个人资料页昵称未被修改
    :param d:
    :return:
    """
    with allure.step("点击昵称跳转到修改昵称页"):
        click_element(d, "个人资料昵称")

    with allure.step("验证修改昵称页是否跳转成功"):
        assert_title(d, "修改昵称")  # 验证是否跳转成功

    with allure.step("修改昵称为Alex"):
        input_element(d, "昵称文本框", "Alex")

    with allure.step("点击修改昵称页返回icon"):
        click_element(d, "返回icon")

    with allure.step("验证是否跳转个人资料页"):
        assert_title(d, "个人资料")  # 验证跳转个人资料页成功

    with allure.step("验证昵称不会被修改"):
        assert d(resourceId=get_value("个人资料昵称")).get_text() == USER_ID.replace((USER_ID[3:7]), "****")

    display_picture(d, "修改昵称页点击返回icon跳转回个人资料页")


@allure.feature("08.修改性别")
@allure.severity('Critical')
def test_modify_sex_08(d):
    """
    修改性别，如果是男就修改成女，如果是女就修改成男
    :param d:
    :return:
    """
    with allure.step("点击性别"):
        sex_text = d(resourceId=get_value("性别文本")).get_text()

        click_element(d, "性别")

    with allure.step("修改性别"):
        if sex_text == "男":
            click_element(d, "选项女")
        elif sex_text == "女":
            click_element(d, "选项男")
        else:
            print("无此选项")

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
    """
    修改职业，如果是测试就修改为码农，如果是码农就修改为测试，并校验
    :param d:
    :return:
    """
    with allure.step("点击职业"):
        click_element(d, "职业")

    with allure.step("验证跳转职业修改页title"):
        assert_title(d, "职业")

    modify_profession_text = d(resourceId=get_value("职业文本")).get_text()

    with allure.step("修改职业"):
        if modify_profession_text == "测试":
            input_element(d, "职业文本", "码农")
        elif modify_profession_text == "码农":
            input_element(d, "职业文本", "测试")
        else:
            input_element(d, "职业文本", "码农")

    with allure.step("点击完成"):
        click_element(d, "完成")

    with allure.step("验证是否修改成功"):
        modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

        if modify_profession_text == "测试":
            assert modify_profession_display == "码农"
        elif modify_profession_text == "码农":
            assert modify_profession_display == "测试"
        else:
            assert modify_profession_display == "码农"

    display_picture(d, "职业页点击返回icon跳转回个人资料页")


@allure.feature("10.修改职业点击返回icon")
@allure.severity('Critical')
def test_modify_profession_icon_10(d):
    """
    修改职业后点击返回icon
    :param d:
    :return:
    """
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
            input_element(d, "职业文本", "码农")

    with allure.step("点击返回icon"):
        click_element(d, "返回icon")

    with allure.step("验证职业是否被修改"):
        modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

        if modify_profession_text == "测试":
            assert modify_profession_display == "测试"
        elif modify_profession_text == "码农":
            assert modify_profession_display == "码农"
        else:
            assert modify_profession_display == "测试"

    display_picture(d, "职业修改页点击返回icon跳转回个人资料页")


@allure.feature("11.修改职业输入框输入内容点击取消")
@allure.severity('Critical')
def test_modify_profession_clear_11(d):
    """
    修改职业输入内容后显示取消按钮，点击取消按钮删除清空输入内容
    :param d:
    :return:
    """
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
            input_element(d, "职业文本", "码农")

    with allure.step("验证清除按钮存在"):

        assert d(resourceId=get_value("清除按钮")).exists

    with allure.step("点击清除按钮"):

        click_element(d, "清除按钮")

    with allure.step("文本内容被清除"):

        modify_profession_display = d(resourceId=get_value("职业文本")).get_text()

        assert modify_profession_display is None

        display_picture(d, "职业修改页输入后删除")

    click_element(d, "返回icon")


@allure.feature("12.手机号校验")
@allure.severity('Critical')
def test_phone_number_check_12(d):
    """
    个人资料手机号与登录账号对比校验
    :param d:
    :return:
    """
    with allure.step("手机号检查"):
        assert USER_ID == d(resourceId=get_value("手机号")).get_text()


@allure.feature("13.所在地修改")
@allure.severity('Critical')
def test_modify_address_13(d):
    """
    所在地修改，如果是北京朝阳区三环到四环之间或其他地址就修改为上海徐汇区城区，反之修改为北京朝阳区三环到四环之间
    :param d:
    :return:
    """
    with allure.step("点击所在地"):
        address_text = d(resourceId=get_value("居住地址文本")).get_text()
        click_element(d, "居住地址文本")

    with allure.step("验证修改地址页title"):
        assert_title(d, "居住地址")

    with allure.step("选择所在地区"):

        click_element(d, "所在地区文本")

    if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
        d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
        time.sleep(1)

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "上海徐汇区城区"
        
        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "外滩"

    elif address_text.replace(' ', '') == "上海徐汇区城区":
        d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
        time.sleep(1)

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "北京朝阳区三环到四环之间"

        input_element(d, "详细地址文本", "安定门")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "安定门"

    else:
        d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
        time.sleep(1)
        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "上海徐汇区城"

        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "外滩"

    with allure.step("点击完成"):

        click_element(d, "完成")

        modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()

        if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
            assert modify_address_text.replace(' ', '') == "上海徐汇区城区"
        elif address_text.replace(' ', '') == "上海徐汇区城区":
            assert modify_address_text.replace(' ', '') == "北京朝阳区三环到四环之间"
        else:
            assert modify_address_text.replace(' ', '') == "上海徐汇区城区"

    display_picture(d, "地址修改")


@allure.feature("14.修改所在地点击返回icon")
@allure.severity('Critical')
def test_modify_address_clear_14(d):
    """
    修改地址后点击返回icon查看内容是否未被修改
    :param d:
    :return:
    """
    with allure.step("点击所在地"):
        address_text = d(resourceId=get_value("居住地址文本")).get_text()
        click_element(d, "居住地址文本")

    with allure.step("验证修改地址页title"):
        assert_title(d, "居住地址")

    with allure.step("选择所在地区"):

        click_element(d, "所在地区文本")

    if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
        d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
        time.sleep(1)

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "上海徐汇区城区"

        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "外滩"

    elif address_text.replace(' ', '') == "上海徐汇区城区":
        d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
        time.sleep(1)

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "北京朝阳区三环到四环之间"

        input_element(d, "详细地址文本", "安定门")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "安定门"

    else:
        d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
        time.sleep(1)
        d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
        time.sleep(1)
        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '') == "上海徐汇区城"

        input_element(d, "详细地址文本", "外滩")

        assert (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '') == "外滩"

    with allure.step("点击返回icon"):

        click_element(d, "返回icon")

        modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()

        if address_text.replace(' ', '') == "上海徐汇区城区":
            assert modify_address_text.replace(' ', '') == "上海徐汇区城区"
        elif address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
            assert modify_address_text.replace(' ', '') == "北京朝阳区三环到四环之间"
        else:
            assert modify_address_text.replace(' ', '') == "上海徐汇区城区"

    display_picture(d, "地址修改后点击返回icon")


@allure.feature("15.修改个性签名")
@allure.severity('Critical')
def test_modify_personalized_signature_15(d):
    """
    修改个性签名
    :param d:
    :return:
    """
    with allure.step("点击个性签名跳转个性签名修改页"):
        click_element(d, "个性签名")
        assert_title(d, "个性签名")

    with allure.step("编辑个性签名"):

        personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

        if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":

            input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

        elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":

            input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")

        else:

            input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

    with allure.step("点击完成"):

        click_element(d, "完成")

    with allure.step("验证是否修改成功"):

        click_element(d, "个性签名")

        modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

        if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
            assert modify_personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底"
        elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":
            assert modify_personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了"
        else:
            assert modify_personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底"

    display_picture(d, "修改个性签名")

    click_element(d, "完成")


@allure.feature("16.修改个性签名后点击返回icon")
@allure.severity('Critical')
def test_modify_personalized_signature_clear_16(d):
    """
    修改个性签名点击返回icon
    :param d:
    :return:
    """
    with allure.step("点击个性签名跳转个性签名修改页"):
        click_element(d, "个性签名")
        assert_title(d, "个性签名")

    with allure.step("编辑个性签名"):

        personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

        if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
            input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

        else:
            input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")

    with allure.step("点击返回icon"):

        click_element(d, "返回icon")

    with allure.step("验证是否修改成功"):

        click_element(d, "个性签名")

        modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

        if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
            assert modify_personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了"
        else:
            assert modify_personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底"

    display_picture(d, "修改个性签名点击返回icon")

    click_element(d, "返回icon")

    click_element(d, "返回icon")


@allure.feature("17.验证实名状态")
@allure.severity('Critical')
def test_check_real_name_authentication_state_17(d):
    """
    根据个人资料中实名认证状态检验是否已实名
    :param d:
    :return:
    """
    with allure.step("点击实名认证"):

        click_element(d, "是否实名")

    with allure.step("是否已实名验证"):

        if Real_Name_Authentication == "已认证":

            assert_title(d, "认证完成")

            display_picture(d, "用户已实名")

        elif Real_Name_Authentication == "未认证":

            assert_title(d, "身份证认证")

            display_picture(d, "用户未实名")


@allure.feature("18.实名认证页返回icon点击")
@allure.severity('Critical')
def test_real_name_click_icon_18(d):
    """
    实名状态页点击返回icon
    :param d:
    :return:
    """
    with allure.step("实名验证页面点击返回icon"):
        click_element(d, "返回icon")

    display_picture(d, "实名认证页面点击返回icon")


@allure.feature("19.验证绑卡状态")
@allure.severity('Critical')
def test_check_tied_card_state_19(d):
    """
    根据个人资料中实名认证状态检验是否绑卡
    :param d:
    :return:
    """
    with allure.step("点击绑卡状态"):

        click_element(d, "是否绑卡")

    with allure.step("是否已绑定卡"):

        if Real_Name_Authentication == "已认证":

            assert_title(d, "银行卡")

            display_picture(d, "已绑定银行卡")

        elif Real_Name_Authentication == "未认证":

            assert_title(d, "身份证认证")

            display_picture(d, "用户未实名")


@allure.feature("20.绑定银行卡页icon点击")
@allure.severity('Critical')
def test_tied_card_click_icon_20(d):
    """
    绑卡页点击返回icon
    :param d:
    :return:
    """
    with allure.step("实名验证页面点击返回icon"):
        click_element(d, "返回icon")

    display_picture(d, "实名认证页面点击返回icon")


@allure.feature("21.已实名中点击查看榜单返回app首页")
@allure.severity('Critical')
def test_check_list_click_21(d):
    """
    已经实名用户点击查看绑定
    :param d:
    :return:
    """
    with allure.step("点击实名认证"):

        click_element(d, "是否实名")

    with allure.step("点击查看榜单"):

        if Real_Name_Authentication == "已认证":
            click_element(d, "查看榜单")
            assert d(resourceId=get_value("首页左上角图标")).exists  # 验证是否有文本为一键登录的控件
            display_picture(d, "点击查看榜单返回首页")
            click_element(d, "首页左上角图标")
        else:
            print("用户未实名")
            click_element(d, "返回icon")
            pass


@allure.feature("22.添加银行卡")
@allure.severity('Critical')
def test_add_bank_cards_22(d):
    """
    添加银行卡
    :param d:
    :return:
    """
    with allure.step("点击绑卡状态"):

        click_element(d, "是否绑卡")

    with allure.step("添加银行卡"):

        if Real_Name_Authentication == "已认证":

            click_element(d, "添加银行卡")

            with allure.step("数字键盘显示"):

                for i in range(10):
                    num_element = "com.bs.finance:id/tv_keyboard_"+str(i)
                    assert d(resourceId=num_element).exists

                assert d(resourceId="com.bs.finance:id/fl_keyboard_del").exists

            display_picture(d, "添加银行卡")

            with allure.step("隐藏数字键盘"):

                click_element(d, "隐藏数字键盘")

                for i in range(10):
                    num_element = "com.bs.finance:id/tv_keyboard_"+str(i)
                    assert not d(resourceId=num_element).exists

                assert not d(resourceId="com.bs.finance:id/fl_keyboard_del").exists

            with allure.step("添加银行卡title校验"):

                assert_title(d, "添加银行卡")

            with allure.step("点击返回icon"):

                click_element(d, "返回icon")

                assert_title(d, "银行卡")

                click_element(d, "返回icon")

        else:
            print("用户未实名认证")


@allure.feature("23.点击我的关注")
@allure.severity('Critical')
def test_click_my_concern_23(d):
    """
    点击我的关注，校验内容
    :param d:
    :return:
    """
    with allure.step("我的关注"):
        click_element(d, "我的关注")

        assert_title(d, "我的关注")

        global product_type

        product_type = ["货币基金", "理财产品", "纯债基金", "智能存款", "活期存款", "结构性存款"]

        with allure.step("检验我的关注内容"):
            for i in range(product_type.__len__()):
                assert d(text=product_type[i]).exists

        display_picture(d, "我的关注")


@allure.feature("24.验证关注内内容")
@allure.severity('Critical')
def test_click_my_concern_content_24(d):
    """
    验证我的关注内下一页内容
    :param d:
    :return:
    """
    with allure.step("将关注页内容保存到字典"):
        product_type_dict = {}
        for i in range(product_type.__len__()):
            product_type_dict[product_type[i]] = d(resourceId=get_value("关注产品类型"))[i].get_text()

        print(product_type_dict)

    for j in range(product_type.__len__()):
        d(text=product_type[j]).click()
        time.sleep(2)
        if int(product_type_dict[product_type[j]]) == 0:
            display_picture(d, "无关注" + str(j + 1))
            print(product_type_dict[product_type[j]])
            assert_title(d, product_type[j])
            assert d(resourceId=get_value("缺省页文本")).exists
            assert d(resourceId=get_value("缺省页文本")).get_text() == "对不起，目前没有数据"
            click_element(d, "返回icon")
        else:
            display_picture(d, "有关注" + str(j + 1))
            print("***" + product_type_dict[product_type[j]] + "***")
            print("++++" + str(d(resourceId=get_value("产品标题")).__len__()) + "+++")
            assert not d(resourceId=get_value("缺省页文本")).exists
            assert int(product_type_dict[product_type[j]]) == d(resourceId=get_value("产品标题")).__len__()
            click_element(d, "返回icon")

    click_element(d, "返回icon")


@allure.feature("99.app退出")
@allure.severity('Critical')
def test_sign_out_app_99(d):
    """
    退出app
    :param d:
    :return:
    """
    with allure.step("点击设置"):

        click_element(d, "侧边栏设置")

    with allure.step("点击安全退出"):

        click_element(d, "安全退出")

    with allure.step("点击确认退出_是"):

        click_element(d, "确认退出_是")

    with allure.step("验证app已成功退出"):

        assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

    display_picture(d, "app退出")


def click_element(d, element_name):
    """
    :param d: 控件默认为d
    :param element_name: 控件名称详见yaml文件
    :return: 无
    封装控件点击操作
    """
    d(resourceId=get_value(element_name)).wait(timeout=10.0)
    d(resourceId=get_value(element_name)).click()
    time.sleep(1)


def input_element(d, element_name, input_text):
    """

    :param d: 控件默认为d
    :param element_name: 控件名称详见yaml文件
    :param input_text: 需要输入的内容
    :return: 无
    """
    d(resourceId=get_value(element_name)).wait(timeout=10.0)
    d(resourceId=get_value(element_name)).set_text(input_text)
    time.sleep(1)


def assert_title(d, title):
    """
    :param d: 控件默认为d
    :param title: 页面标题
    :return: 无
    验证页面是否跳转成功

    """
    assert title == d(resourceId=get_value("标题")).get_text()
    time.sleep(1)


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
