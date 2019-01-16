#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import os
import random
import re
import time
import allure
import pytest
import yaml
import uiautomator2 as u2
from pathlib import Path
import warnings
import sys
import datetime

from test_case.test_bicai import display_picture, click_element, assert_title, get_driver_by_key, get_value, \
    assert_element_exists_save_picture, input_element, assert_equal_save_picture, click_element_with_text

warnings.filterwarnings("ignore")
from optparse import OptionParser


@pytest.fixture(scope='module')
def d():
    global running_environment
    # running_environment = sys.argv[1]
    running_environment = "Y66手机udid"
    # running_environment = "Y66手机ip"
    d = get_driver_by_key(running_environment)  # 输入参数启动
    # d = get_driver_by_key("Y66手机ip")   # 输入手机ip启动app
    # d = get_driver_by_key("Y66手机udid")   # 输入手机udid启动
    # d = get_driver_by_key("夜神模拟器udid")   # 输入手机udid启动
    global start_time
    i = datetime.datetime.now()
    # strat_time = "启动时间为  %s/%s/%s" % (i.hour, i.minute, i.second)
    strat_time = "启动时间为  %s时%s分%s秒" % (i.hour, i.minute, i.second)
    global now_date
    now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    print(strat_time)

    # d.unlock()
    d.set_fastinput_ime(True)  # 开启快速输入
    d.session("com.bs.finance")
    yield d
    y = datetime.datetime.now()
    end_time = "结束时间为  %s时%s分%s秒" % (y.hour, y.minute, y.second)
    print(end_time)
    d.app_stop("com.bs.finance")


@allure.feature("001.启动app后进入比财")
@allure.severity('Critical')
def test_go_01(d):
    """
    首次启动app点击进入比财,如果有广告页点击x关闭，
    :param d:
    :return:
    """

    time.sleep(5)

    show_running_environment = str(running_environment) + ":" + get_value(str(running_environment))

    allure.environment(使用连接方式=str(show_running_environment))

    with allure.step("启动页点击进入比财"):
        click_element(d, "启动页进入比财")

    with allure.step("如果弹出广告页点x关闭"):
        if d(resourceId=get_value("广告页")).exists:  # 如果弹出广告页
            click_element(d, "广告页关闭")  # 点击x关闭

    with allure.step("验证启动app点击进入比财是否进入首页"):
        assert_element_exists_save_picture(d, d(text="一键登录").exists, "验证是否有文本为一键登录的控件")


@allure.feature("002.比财登录")
@allure.severity('Critical')
def test_login_02(d):
    """
    比财账号登录

    """
    global USER_ID  # 使用账号

    USER_ID = str(get_value("xc手机号"))

    picture_verification_code = str(get_value("四位图片验证码"))

    login_verification_code = str(get_value("登录验证码"))

    with allure.step("点击app首页一键登录"):
        click_element(d, "首页一键登录")

    with allure.step("在登录页账号输入框输入账号"):
        input_element(d, "登录页账号输入框", USER_ID)

    with allure.step("点击获取验证码"):
        click_element(d, "登录页获取验证码按钮")  # 点击获取验证码

    #  如果弹出4位数字图片验证码
    with allure.step("输入4位验证码"):
        time.sleep(2)
        if d(text=u"请填写图像验证码").exists:
            input_element(d, "图片验证码输入框", picture_verification_code)
            with allure.step("点击确认按钮"):
                click_element(d, "图片验证码确定按钮")

    with allure.step("输入6位验证码"):
        input_element(d, "登录验证码输入框", login_verification_code)

    with allure.step("点击立即登录"):
        click_element(d, "立即登录按钮")

    with allure.step("验证是否登录成功"):
        assert_element_exists_save_picture(d, not d(resourceId=get_value("首页一键登录")).exists, "验证是否登录")


@allure.feature("003.弹出侧边栏")
@allure.severity('Critical')
def test_sidebar_eject_03(d):
    """
     验证点击左上角图标弹出侧边栏功能
    """

    global cebian_button  # 侧边栏按钮

    global realname_status  # 实名认证状态

    cebian_button = ["我的关注", "我的消息", "我的钱包", "关于我们"]

    with allure.step("点击左上角图标"):
        click_element(d, "首页左上角图标")
        time.sleep(10)

    with allure.step("检验侧边栏控件"):
        for i in range(cebian_button.__len__()):
            assert_element_exists_save_picture(d, d(text=cebian_button[i]).exists,
                                               "验证侧边栏" + cebian_button[i] + "按钮控件存在")

    with allure.step("验证账号为已登录状态，账号为" + USER_ID):
        user_id = d(resourceId=get_value("侧边栏账号")).get_text()
        assert_equal_save_picture(d, user_id, USER_ID.replace((USER_ID[3:7]), "****"), "账号" + USER_ID + "已登录状态")


# @allure.feature("04.点击侧边栏目logo")
# @allure.severity('Critical')
# def test_logo_click_04(d):
#     """
#     验证点击侧边栏logo会跳转正确跳到个人资料页，及个人资料页内控件元素存在校验
#     :param d:
#     :return: 无
#     """
#     with allure.step("侧边栏logo点击"):
#         click_element(d, "侧边栏logo")
#
#     with allure.step("验证是否跳转个人资料页"):
#         assert_title(d, "个人资料")  # 验证跳转个人资料页成功
#
#     personal_data = ["性别", "微信", "职业", "实名认证", "手机号", "所在地", "个性签名"]
#
#     global Real_Name_Authentication  # 实名认证状态
#
#     Real_Name_Authentication = d(resourceId=get_value("实名认证状态")).get_text()
#
#     for i in range(personal_data.__len__()):
#         assert_element_exists_save_picture(d, d(text=personal_data[i]).exists, "控件" + personal_data[i] + "存在")
#
#
# @allure.feature("05.点击昵称进入修改页")
# @allure.severity('Critical')
# def test_nickname_click_05(d):
#     """
#     验证点击昵称可正确跳转修到昵称修改页
#     :param d:
#     :return:
#     """
#     with allure.step("点击昵称跳转到修改昵称页"):
#         click_element(d, "个人资料昵称")
#
#     with allure.step("验证修改昵称页title"):
#         assert_title(d, "修改昵称")  # 验证是否跳转成功
#
#     display_picture(d, "修改昵称页")
#
#
# @allure.feature("06.修改昵称页修改昵称点击完成")
# @allure.severity('Critical')
# def test_complete_click_06(d):
#     """
#     昵称修改后点击完成验证个人资料页是否显示修改后昵称
#     :param d:
#     :return:
#     """
#
#     with allure.step("修改昵称为Alex"):
#         input_element(d, "昵称文本框", "Alex")
#
#     with allure.step("点击完成按钮返回个人资料页"):
#         click_element(d, "完成按钮")
#
#     with allure.step("验证是否跳转个人资料页"):
#         assert_title(d, "个人资料")  # 验证跳转个人资料页成功
#
#     with allure.step("验证昵称是否修改成功"):
#         assert_equal_save_picture(d, d(resourceId=get_value("个人资料昵称")).get_text(), "Alex", "昵称修改")
#
#     # 恢复数据
#     click_element(d, "个人资料昵称")
#
#     input_element(d, "昵称文本框", USER_ID.replace((USER_ID[3:7]), "****"))
#
#     click_element(d, "完成按钮")
#
#
# @allure.feature("07.修改昵称页点击返回icon")
# @allure.severity('Critical')
# def test_nickname_icon_click_07(d):
#     """
#     修改昵称后点击返回icon，查看个人资料页昵称未被修改
#     :param d:
#     :return:
#     """
#     with allure.step("点击昵称跳转到修改昵称页"):
#         click_element(d, "个人资料昵称")
#
#     with allure.step("验证修改昵称页是否跳转成功"):
#         assert_title(d, "修改昵称")  # 验证是否跳转成功
#
#     with allure.step("修改昵称为Alex"):
#         input_element(d, "昵称文本框", "Alex")
#
#     with allure.step("点击修改昵称页返回icon"):
#         click_element(d, "返回icon")
#
#     with allure.step("验证是否跳转个人资料页"):
#         assert_title(d, "个人资料")  # 验证跳转个人资料页成功
#
#     with allure.step("验证昵称不会被修改"):
#         assert_equal_save_picture(d, d(resourceId=get_value("个人资料昵称")).get_text(),
#                                   USER_ID.replace((USER_ID[3:7]), "****"), "昵称未做修改")
#
#
# @allure.feature("08.修改性别")
# @allure.severity('Critical')
# def test_modify_sex_08(d):
#     """
#     修改性别，如果是男就修改成女，如果是女就修改成男
#     :param d:
#     :return:
#     """
#     with allure.step("点击性别"):
#         sex_text = d(resourceId=get_value("性别文本")).get_text()
#
#         click_element(d, "性别")
#
#     with allure.step("修改性别"):
#         if sex_text == "男":
#             click_element(d, "选项女")
#         elif sex_text == "女":
#             click_element(d, "选项男")
#         else:
#             print("无此选项")
#
#     with allure.step("验证性别修改是否成功"):
#         modify_sex_text = d(resourceId=get_value("性别文本")).get_text()
#         if sex_text == "男":
#             assert_equal_save_picture(d, modify_sex_text, "女", "性别修改为女")
#         elif sex_text == "女":
#             assert_equal_save_picture(d, modify_sex_text, "男", "性别修改为男")
#         else:
#             print("无此选项")
#
#
# @allure.feature("09.修改职业")
# @allure.severity('Critical')
# def test_modify_profession_09(d):
#     """
#     修改职业，如果是测试就修改为码农，如果是码农就修改为测试，并校验
#     :param d:
#     :return:
#     """
#     with allure.step("点击职业"):
#         click_element(d, "职业")
#
#     with allure.step("验证跳转职业修改页title"):
#         assert_title(d, "职业")
#
#     modify_profession_text = d(resourceId=get_value("职业文本")).get_text()
#
#     with allure.step("修改职业"):
#         if modify_profession_text == "测试":
#             input_element(d, "职业文本", "码农")
#         elif modify_profession_text == "码农":
#             input_element(d, "职业文本", "测试")
#         else:
#             input_element(d, "职业文本", "码农")
#
#     with allure.step("点击完成"):
#         click_element(d, "完成")
#
#     with allure.step("验证是否修改成功"):
#         modify_profession_display = d(resourceId=get_value("职业展示")).get_text()
#
#         if modify_profession_text == "测试":
#             assert_equal_save_picture(d, modify_profession_display, "码农", "职业修改")
#         elif modify_profession_text == "码农":
#             assert_equal_save_picture(d, modify_profession_display, "测试", "职业修改")
#         else:
#             assert_equal_save_picture(d, modify_profession_display, "码农", "职业修改")
#
#
# @allure.feature("10.修改职业点击返回icon")
# @allure.severity('Critical')
# def test_modify_profession_icon_10(d):
#     """
#     修改职业后点击返回icon
#     :param d:
#     :return:
#     """
#     with allure.step("点击职业"):
#         click_element(d, "职业")
#
#     global modify_profession_text
#
#     modify_profession_text = d(resourceId=get_value("职业文本")).get_text()
#
#     with allure.step("修改职业"):
#         if modify_profession_text == "测试":
#             input_element(d, "职业文本", "码农")
#         elif modify_profession_text == "码农":
#             input_element(d, "职业文本", "测试")
#         else:
#             input_element(d, "职业文本", "码农")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#     with allure.step("验证职业是否被修改"):
#         modify_profession_display = d(resourceId=get_value("职业展示")).get_text()
#
#         if modify_profession_text == "测试":
#             assert_equal_save_picture(d, modify_profession_display, "测试", "职业未做修改")
#         elif modify_profession_text == "码农":
#             assert_equal_save_picture(d, modify_profession_display, "码农", "职业未做修改")
#         else:
#             assert_equal_save_picture(d, modify_profession_display, "测试", "职业未做修改")
#
#
# @allure.feature("11.修改职业输入框输入内容点击取消")
# @allure.severity('Critical')
# def test_modify_profession_clear_11(d):
#     """
#     修改职业输入内容后显示取消按钮，点击取消按钮删除清空输入内容
#     :param d:
#     :return:
#     """
#     with allure.step("点击职业"):
#         click_element(d, "职业")
#
#     with allure.step("验证不存在清除按钮"):
#         assert_element_exists_save_picture(d, not d(resourceId=get_value("清除按钮")).exists, "不显示清除按钮")
#
#     with allure.step("修改职业文本框内容"):
#
#         if modify_profession_text == "测试":
#             input_element(d, "职业文本", "码农")
#         elif modify_profession_text == "码农":
#             input_element(d, "职业文本", "测试")
#         else:
#             input_element(d, "职业文本", "码农")
#
#     with allure.step("验证清除按钮存在"):
#         assert_element_exists_save_picture(d, d(resourceId=get_value("清除按钮")).exists, "显示清除按钮")
#
#     with allure.step("点击清除按钮"):
#
#         click_element(d, "清除按钮")
#
#     with allure.step("文本内容被清除"):
#
#         modify_profession_display = d(resourceId=get_value("职业文本")).get_text()
#
#         if modify_profession_display is None:
#             # display_picture(d, "清除内容_成功")
#             assert modify_profession_display is None
#         else:
#             display_picture(d, "清除内容_失败")
#             assert modify_profession_display is None
#
#     click_element(d, "返回icon")
#
#
# @allure.feature("12.手机号校验")
# @allure.severity('Critical')
# def test_phone_number_check_12(d):
#     """
#     个人资料手机号与登录账号对比校验
#     :param d:
#     :return:
#     """
#     with allure.step("手机号检查"):
#         assert_equal_save_picture(d, USER_ID, d(resourceId=get_value("手机号")).get_text(), "个人资料手机号与登录账号对比")
#
#
# @allure.feature("13.所在地修改")
# @allure.severity('Critical')
# def test_modify_address_13(d):
#     """
#     所在地修改，如果是北京朝阳区三环到四环之间或其他地址就修改为上海徐汇区城区，反之修改为北京朝阳区三环到四环之间
#     :param d:
#     :return:
#     """
#     with allure.step("点击所在地"):
#         address_text = d(resourceId=get_value("居住地址文本")).get_text()
#         click_element(d, "居住地址文本")
#
#     with allure.step("验证修改地址页title"):
#         assert_title(d, "居住地址")
#
#     with allure.step("选择所在地区"):
#
#         click_element(d, "所在地区文本")
#
#     if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
#         d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
#         time.sleep(1)
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text, "上海徐汇区城区", "所在地区修改为上海")
#
#         input_element(d, "详细地址文本", "外滩")
#         detailed_address_text = (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '')
#         print("**********************")
#         print(detailed_address_text)
#         print("**********************")
#         assert_equal_save_picture(d, detailed_address_text, "外滩", "详细地址修改为外滩")
#
#     elif address_text.replace(' ', '') == "上海徐汇区城区":
#         d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
#         time.sleep(1)
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text, "北京朝阳区三环到四环之间", "地区修改")
#
#         input_element(d, "详细地址文本", "安定门")
#
#         assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''), "安定门", "详细地址修改")
#
#     else:
#         d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
#         time.sleep(1)
#         input_element(d, "详细地址文本", "外滩")
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text, "上海徐汇区城区", "所在地区修改为上海")
#
#         input_element(d, "详细地址文本", "外滩")
#
#         assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''), "详细地址修改为外滩")
#
#     with allure.step("点击完成"):
#
#         click_element(d, "完成")
#
#         modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()
#
#         if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "地址修改")
#         elif address_text.replace(' ', '') == "上海徐汇区城区":
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "北京朝阳区三环到四环之间", "地址修改")
#         else:
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "地址修改")
#
#
# @allure.feature("14.修改所在地点击返回icon")
# @allure.severity('Critical')
# def test_modify_address_clear_14(d):
#     """
#     修改地址后点击返回icon查看内容是否未被修改
#     :param d:
#     :return:
#     """
#     with allure.step("点击所在地"):
#         address_text = d(resourceId=get_value("居住地址文本")).get_text()
#         click_element(d, "居住地址文本")
#
#     with allure.step("验证修改地址页title"):
#         assert_title(d, "居住地址")
#
#     with allure.step("选择所在地区"):
#
#         click_element(d, "所在地区文本")
#
#     if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
#         d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
#         time.sleep(1)
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text,
#                                   "上海徐汇区城区", "地区修改")
#
#         input_element(d, "详细地址文本", "外滩")
#
#         assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
#                                   "外滩", "文本修改")
#
#     elif address_text.replace(' ', '') == "上海徐汇区城区":
#         d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
#         time.sleep(1)
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text, "北京朝阳区三环到四环之间", "地区修改")
#
#         input_element(d, "详细地址文本", "安定门")
#
#         assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
#                                   "安定门", "详细地址修改")
#
#     else:
#         d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
#         time.sleep(1)
#         d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
#         time.sleep(1)
#         input_element(d, "详细地址文本", "外滩")
#         location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
#         assert_equal_save_picture(d, location_text, "上海徐汇区城区", "地区修改")
#
#         input_element(d, "详细地址文本", "外滩")
#
#         assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
#                                   "外滩", "文本修改")
#
#     with allure.step("点击返回icon"):
#
#         click_element(d, "返回icon")
#
#         modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()
#
#         if address_text.replace(' ', '') == "上海徐汇区城区":
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "点击返回icon居住地址校验")
#         elif address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "北京朝阳区三环到四环之间", "点击返回icon居住地址校验")
#         else:
#             assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "点击返回icon居住地址校验")
#
#
# @allure.feature("15.修改个性签名")
# @allure.severity('Critical')
# def test_modify_personalized_signature_15(d):
#     """
#     修改个性签名
#     :param d:
#     :return:
#     """
#     with allure.step("点击个性签名跳转个性签名修改页"):
#         click_element(d, "个性签名")
#         assert_title(d, "个性签名")
#
#     with allure.step("编辑个性签名"):
#
#         personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()
#
#         if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
#
#             input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")
#
#         elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":
#
#             input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")
#
#         else:
#
#             input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")
#
#     with allure.step("点击完成"):
#
#         click_element(d, "完成")
#
#     with allure.step("验证是否修改成功"):
#
#         click_element(d, "个性签名")
#
#         modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()
#
#         if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
#             assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
#                                       "噜起袖子加油干一张蓝图绘到底", "修改个性签名")
#         elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":
#             assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
#                                       "企业要想好踏踏实实搞成天作报告那可好不了", "修改个性签名")
#         else:
#             assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
#                                       "噜起袖子加油干一张蓝图绘到底", "修改个性签名")
#
#     click_element(d, "完成")
#
#
# @allure.feature("16.修改个性签名后点击返回icon")
# @allure.severity('Critical')
# def test_modify_personalized_signature_clear_16(d):
#     """
#     修改个性签名点击返回icon
#     :param d:
#     :return:
#     """
#     with allure.step("点击个性签名跳转个性签名修改页"):
#         click_element(d, "个性签名")
#         assert_title(d, "个性签名")
#
#     with allure.step("编辑个性签名"):
#
#         personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()
#
#         if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
#             input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")
#
#         else:
#             input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")
#
#     with allure.step("点击返回icon"):
#
#         click_element(d, "返回icon")
#
#     with allure.step("验证是否修改成功"):
#
#         click_element(d, "个性签名")
#
#         modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()
#
#         if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
#             assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
#                                       "企业要想好踏踏实实搞成天作报告那可好不了", "修改点返回icon签名不会修改")
#         else:
#             assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
#                                       "噜起袖子加油干一张蓝图绘到底", "修改点返回icon签名不会修改")
#
#     click_element(d, "返回icon")
#
#     click_element(d, "返回icon")
#
#
# @allure.feature("17.验证实名状态")
# @allure.severity('Critical')
# def test_check_real_name_authentication_state_17(d):
#     """
#     根据个人资料中实名认证状态检验是否已实名
#     :param d:
#     :return:
#     """
#     with allure.step("点击实名认证"):
#
#         click_element(d, "是否实名")
#
#     with allure.step("是否已实名验证"):
#
#         if Real_Name_Authentication == "已认证":
#
#             assert_title(d, "认证完成")
#
#             display_picture(d, "用户已实名")
#
#         elif Real_Name_Authentication == "未认证":
#
#             assert_title(d, "身份证认证")
#
#             display_picture(d, "用户未实名")
#
#
# @allure.feature("18.实名认证页返回icon点击")
# @allure.severity('Critical')
# def test_real_name_click_icon_18(d):
#     """
#     实名状态页点击返回icon
#     :param d:
#     :return:
#     """
#     with allure.step("实名验证页面点击返回icon"):
#         click_element(d, "返回icon")
#
#     display_picture(d, "实名认证页面点击返回icon")
#
#
# @allure.feature("19.验证绑卡状态")
# @allure.severity('Critical')
# def test_check_tied_card_state_19(d):
#     """
#     根据个人资料中实名认证状态检验是否绑卡
#     :param d:
#     :return:
#     """
#     with allure.step("点击绑卡状态"):
#
#         click_element(d, "是否绑卡")
#
#     with allure.step("是否已绑定卡"):
#
#         if Real_Name_Authentication == "已认证":
#
#             assert_title(d, "银行卡")
#             global cards_number
#             cards_name_a = []
#             cards_name_b = []
#             card_name = d(resourceId=get_value("银行名称"))  # 获取卡数量
#
#             for i in range(card_name.__len__()):
#                 print(card_name[i].get_text())
#                 cards_name_a.append(card_name[i].get_text())
#             print(cards_name_a)
#
#             d(scrollable=True).scroll(steps=30)  # 向下滑动
#
#             time.sleep(5)
#
#             for i in range(card_name.__len__()):
#                 print(card_name[i].get_text())
#                 cards_name_b.append(card_name[i].get_text())
#
#             print(cards_name_b)
#
#             cards_name_c = list(set(cards_name_a + cards_name_b))
#
#             print(cards_name_c)
#
#             cards_number = cards_name_c.__len__()
#
#         elif Real_Name_Authentication == "未认证":
#
#             assert_title(d, "身份证认证")
#
#
# @allure.feature("20.绑定银行卡页icon点击")
# @allure.severity('Critical')
# def test_tied_card_click_icon_20(d):
#     """
#     绑卡页点击返回icon
#     :param d:
#     :return:
#     """
#     with allure.step("实名验证页面点击返回icon"):
#         click_element(d, "返回icon")
#
#     display_picture(d, "实名认证页面点击返回icon")
#
#
# @allure.feature("21.已实名中点击查看榜单返回app首页")
# @allure.severity('Critical')
# def test_check_list_click_21(d):
#     """
#     已经实名用户点击查看绑定
#     :param d:
#     :return:
#     """
#     with allure.step("点击实名认证"):
#
#         click_element(d, "是否实名")
#
#     with allure.step("点击查看榜单"):
#
#         if Real_Name_Authentication == "已认证":
#             click_element(d, "查看榜单")
#             assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
#             click_element(d, "首页左上角图标")
#         else:
#             print("用户未实名")
#             click_element(d, "返回icon")
#             pass
#
#
# @allure.feature("22.添加银行卡")
# @allure.severity('Critical')
# def test_add_bank_cards_22(d):
#     """
#     添加银行卡
#     :param d:
#     :return:
#     """
#     with allure.step("点击绑卡状态"):
#
#         click_element(d, "是否绑卡")
#
#     with allure.step("添加银行卡"):
#
#         if Real_Name_Authentication == "已认证":
#
#             d(scrollable=True).scroll(steps=10)
#
#             click_element(d, "添加银行卡")
#
#             with allure.step("数字键盘显示"):
#
#                 for i in range(10):
#                     num_element = "com.bs.finance:id/tv_keyboard_" + str(i)
#                     assert_element_exists_save_picture(d, d(resourceId=num_element).exists, "数字键盘显示")
#
#                 assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/fl_keyboard_del").exists,
#                                                    "删除键盘显示")
#
#             display_picture(d, "添加银行卡")
#
#             with allure.step("隐藏数字键盘"):
#
#                 click_element(d, "隐藏数字键盘")
#
#                 for i in range(10):
#                     num_element = "com.bs.finance:id/tv_keyboard_" + str(i)
#                     assert_element_exists_save_picture(d, not d(resourceId=num_element).exists, "隐藏数字键盘")
#
#                 assert_element_exists_save_picture(d, not d(resourceId="com.bs.finance:id/fl_keyboard_del").exists,
#                                                    "隐藏数字键盘删除键")
#
#             with allure.step("添加银行卡title校验"):
#
#                 assert_title(d, "添加银行卡")
#
#             with allure.step("点击返回icon"):
#
#                 click_element(d, "返回icon")
#
#                 assert_title(d, "银行卡")
#
#                 click_element(d, "返回icon")
#
#         else:
#             print("用户未实名认证")
#
#
# @allure.feature("23.点击我的关注")
# @allure.severity('Critical')
# def test_click_my_concern_23(d):
#     """
#     点击我的关注，校验内容
#     :param d:
#     :return:
#     """
#     with allure.step("我的关注"):
#         click_element(d, "我的关注")
#
#         assert_title(d, "我的关注")
#
#         global product_type
#
#         product_type = ["货币基金", "理财产品", "纯债基金", "智能存款", "活期存款", "结构性存款"]
#
#         with allure.step("校验我的关注内容"):
#             for i in range(product_type.__len__()):
#                 assert_element_exists_save_picture(d, d(text=product_type[i]).exists, "校验我的关注内容")
#
#
# @allure.feature("24.验证关注内内容")
# @allure.severity('Critical')
# def test_click_my_concern_content_24(d):
#     """
#     验证我的关注内下一页内容
#     :param d:
#     :return:
#     """
#     with allure.step("将关注页内容保存到字典"):
#         product_type_dict = {}
#         for i in range(product_type.__len__()):
#             product_type_dict[product_type[i]] = d(resourceId=get_value("关注产品类型"))[i].get_text()
#
#         print(product_type_dict)
#
#     for j in range(product_type.__len__()):
#         d(text=product_type[j]).click()
#         time.sleep(2)
#         with allure.step("for循环对比关注条数和类型页展示条数"):
#             if int(product_type_dict[product_type[j]]) == 0:
#                 display_picture(d, "无关注" + str(j + 1))
#                 print(product_type_dict[product_type[j]])
#                 assert_title(d, product_type[j])
#                 assert_element_exists_save_picture(d, d(resourceId=get_value("缺省页文本")).exists, "无关注省却页展示")
#                 assert_equal_save_picture(d, d(resourceId=get_value("缺省页文本")).get_text(),
#                                           "对不起，目前没有数据", "省缺页文本校验")
#                 click_element(d, "返回icon")
#             else:
#                 display_picture(d, "有关注" + str(j + 1))
#                 print("我的关注页统计:" + product_type_dict[product_type[j]] + "条")
#                 print("产品类型页显示:" + str(d(resourceId=get_value("产品标题")).__len__()) + "条")
#                 assert_element_exists_save_picture(d, not d(resourceId=get_value("缺省页文本")).exists, "有关注不展示缺省页")
#                 with allure.step("对比我的关注页统计条数和产品类型页显示条数"):
#                     assert_equal_save_picture(d, int(product_type_dict[product_type[j]]),
#                                               d(resourceId=get_value("产品标题")).__len__(), "关注条目数量校验")
#                 with allure.step("点击返回icon"):
#                     click_element(d, "返回icon")
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("25.点击我的消息")
# @allure.severity('Critical')
# def test_click_my_news_25(d):
#     """
#     点击我的消息
#     :param d:
#     :return:
#     """
#
#     massage_type = ["系统消息", "产品消息", "活动"]
#
#     with allure.step("点击我的消息"):
#         click_element_with_text(d, "我的消息", "我的消息")
#
#     with allure.step("校验跳转后title"):
#         assert_title(d, "消息")
#
#     with allure.step("校验消息内内容"):
#         for i in range(massage_type.__len__()):
#             with allure.step("点击消息内条目跳转" + "进入" + str(massage_type[i])):
#                 click_element_with_text(d, "我的消息", massage_type[i])
#             with allure.step("校验跳转后title显示"):
#                 assert_title(d, massage_type[i])
#             with allure.step("点击返回icon"):
#                 click_element(d, "返回icon")
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("26.点击我的钱包")
# @allure.severity('Critical')
# def test_click_bicai_wallet_26(d):
#     """
#     点击我的钱包跳转
#     :param d:
#     :return:
#     """
#     global remaining_sum_type  # 首次点击进入账户余额显示/隐藏状态记录
#     global change_remaining_sum_type  # 再次进入账户余额显示/隐藏状态记录
#     with allure.step("点击我的钱包"):
#         click_element_with_text(d, "我的钱包", "我的钱包")
#         assert_title(d, "我的钱包")
#
#
# @allure.feature("27.点击常见问题")
# @allure.severity('Critical')
# def test_click_common_problem_27(d):
#     """
#     点击常见问题跳转
#     :param d:
#     :return:
#     """
#
#     with allure.step("点击常见问题"):
#         click_element(d, "常见问题")
#         assert_title(d, "常见问题")
#         click_element(d, "返回icon")
#
#
# @allure.feature("28.点击明细")
# @allure.severity('Critical')
# def test_click_detailed_28(d):
#     """
#     点击明细，跳转明细页默认选择收益明细
#     :param d:
#     :return:
#     """
#     with allure.step("点击明细"):
#         d(description=u"明细").click()
#         time.sleep(2)
#         assert_title(d, "明细")
#
#     with allure.step("默认选择为收益明细"):
#         assert_element_exists_save_picture(d, d(className="android.widget.ImageView", instance=3).exists, "默认选择收益明细")
#
#     with allure.step("日期图标显示"):
#         assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/iv_date").exists, "日期图标显示")
#
#
# @allure.feature("29.点击交易记录")
# @allure.severity('Critical')
# def test_click_business_record_29(d):
#     """
#     切换交易明细页，日期图标被隐藏
#     :param d:
#     :return:
#     """
#     with allure.step("点击交易记录"):
#         click_element(d, "交易记录")
#         assert_title(d, "明细")
#
#     with allure.step("交易记录下划线显示"):
#         assert_element_exists_save_picture(d, d(className="android.widget.ImageView", instance=2).exists,
#                                            "交易记录下划线显示")
#
#     with allure.step("日期图标显示"):
#         assert_element_exists_save_picture(d, not d(resourceId="com.bs.finance:id/iv_date").exists, "日期图标隐藏")
#
#
# @allure.feature("30.点击交易记录页内容")
# @allure.severity('Critical')
# def test_click_business_record_content_30(d):
#     """
#     如果交易记录页中有内容点击进入
#     :param d:
#     :return:
#     """
#     if d(className="android.widget.RelativeLayout", instance=2).exists:
#         with allure.step("点击交易记录页首条记录"):
#             d(className="android.widget.RelativeLayout", instance=2).click()
#             time.sleep(2)
#             assert_title(d, "交易明细")
#
#         with allure.step("点击返回icon"):
#             click_element(d, "返回icon")
#     else:
#         print("该账号没有做过交易")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("31.点击提现")
# @allure.severity('Critical')
# def test_click_cash_withdrawal_31(d):
#     """
#     点击提现
#     :param d:
#     :return:
#     """
#     with allure.step("点击提现"):
#         d(description=u"提现").click()
#         time.sleep(2)
#         assert_title(d, "余额提现")
#
#     with allure.step("正则匹配可提现余额"):
#         global balance  # 可提现余额
#         balance_text = d(resourceId="com.bs.finance:id/wallet_get_cash_tv_money_tip").get_text()
#         balance = re.findall(r'-?\d+\.?\d*e?-?\d*?', balance_text)
#         print("可提现余额：" + str(balance[0]))
#
#
# @allure.feature("32.验证进入提现页提现按钮默认不可点")
# @allure.severity('Critical')
# def test_cash_withdrawal_clickenable_32(d):
#     """
#     验证页面跳转后提现按钮不可点击
#     :param d:
#     :return:
#     """
#     with allure.step("验证进入提现页提现按钮默认不可点"):
#         assert_element_exists_save_picture(d, not d(resourceId=get_value("提现按钮")).info["clickable"],
#                                            "提现按钮默认不可点")
#
#
# @allure.feature("33.验证输入大于等于10元提现金额按钮可点击")
# @allure.severity('Critical')
# def test_cash_withdrawal_clickable_33(d):
#     """
#     验证页面输入大于等于10元随机金额提现按钮可以点击
#     :param d:
#     :return:
#     """
#
#     with allure.step("验证输入大于等于10元提现按钮可以点击"):
#         if float(balance[0]) >= 10.00:
#             input_money_text = random.uniform(10.00, float(balance[0]))
#             input_money = round(input_money_text, 2)  # 随机生成大于10元小于可提现金额随机浮点数
#             input_element(d, "余额提现页金额输入框", str(input_money))
#             assert_element_exists_save_picture(d, d(resourceId=get_value("提现按钮")).info["clickable"],
#                                                "余额和提现金额大于10提现按钮可点击")
#
#
# @allure.feature("34.验证输入小等10元提现金额按钮不可点击")
# @allure.severity('Critical')
# def test_cash_withdrawal_clickable__less_than_ten_34(d):
#     """
#     验证页面输入小于10元随机金额提现按钮不可点击
#     :param d:
#     :return:
#     """
#     with allure.step("验证输入小于10元提现按钮不可点击"):
#         input_element(d, "余额提现页金额输入框", str(9.99))
#         assert_element_exists_save_picture(d, not d(resourceId=get_value("提现按钮")).info["clickable"],
#                                            "余额提现金额小于10提现不可点")
#
#     click_element(d, "返回icon")
#
#
# @allure.feature("35.账户余额隐藏显示状态校验")
# @allure.severity('Critical')
# def test_balance_display_hide_35(d):
#     """
#     账户余额校验
#     :param d:
#     :return:
#     """
#     with allure.step("获取账户余额显示隐藏状态"):
#         if d(description=u"****").exists:
#             print("当前账户余额金额显示状态为:隐藏")
#             remaining_sum_type = 1  # 金额隐藏
#
#         elif d(description=str(balance[0])).exists:
#             print("当前账户余额金额显示状态为:显示")
#             remaining_sum_type = 0  # 金额显示
#
#     with allure.step("点击显示/隐藏图标"):
#         d(className="android.widget.Button").click()
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#     with allure.step("再次点击进入我的钱包"):
#         click_element_with_text(d, "我的钱包", "我的钱包")
#         assert_title(d, "我的钱包")
#
#     with allure.step("获取改变后账户余额显示隐藏状态"):
#         if d(description=str(balance[0])).exists:
#             print("当前账户余额金额显示状态为:显示")
#             change_remaining_sum_type = 1  # 金额显示
#
#         elif d(description=u"****").exists:
#             print("当前账户余额金额显示状态为:隐藏")
#             change_remaining_sum_type = 0  # 金额隐藏
#
#     with allure.step("金额显示/隐藏状态对比"):
#         assert_equal_save_picture(d, remaining_sum_type, change_remaining_sum_type, "金额显示/隐藏状态对比")
#
#
# @allure.feature("36.点击我的钱包银行卡跳转")
# @allure.severity('Critical')
# def test_click_card_button_36(d):
#     """
#     点击我的钱包银行卡跳转
#     :param d:
#     :return:
#     """
#     card_button_text = "银行卡(" + str(cards_number) + ")"
#     with allure.step("点击银行卡跳转"):
#         d(description=card_button_text).click()
#         time.sleep(2)
#
#     with allure.step("校验是否跳转成功"):
#         assert_title(d, "银行卡")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("37.点击II类户跳转")
# @allure.severity('Critical')
# def test_click_type_two_accounts_37(d):
#     """
#     点击二类户跳转
#     :param d:
#     :return:
#     """
#     with allure.step("点击II类户（图片）跳转"):
#         d(description=u"A37H3tXWoJVwAAAAAASUVORK5CYII=").click()
#         time.sleep(1)
#
#     with allure.step("校验是否跳转成功"):
#         assert_title(d, "II类户")
#         type_two_accounts_number = (d(resourceId="com.bs.finance:id/bg_bank_item")).__len__()
#         print("已绑定二类户数量为:" + str(type_two_accounts_number))
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#     with allure.step("点击II类户按钮跳转并校验已经绑定二类户数量"):
#         type_two_accounts_text = "Ⅱ类户(" + str(type_two_accounts_number) + ")"
#         d(description=str(type_two_accounts_text)).click()
#         time.sleep(2)
#
#     with allure.step("校验是否跳转成功"):
#         assert_title(d, "II类户")
#
#
# @allure.feature("38.点击未开户")
# @allure.severity('Critical')
# def test_click_not_opening_bank_38(d):
#     """
#     点击二类户跳转
#     :param d:
#     :return:
#     """
#     with allure.step("点击未开户"):
#         click_element_with_text(d, "未开户", "未开户")
#     with allure.step("校验是否跳转到未开户"):
#         assert_element_exists_save_picture(d, d(resourceId=get_value("查看全部银行")).exists, "查看全部银行按钮显示")
#
#         if d(resourceId=get_value("银行卡展示")).__len__() >= 1:
#
#             if d(resourceId=get_value("银行名称")).get_text() == "晋享财富":
#                 assert_element_exists_save_picture(d, d(resourceId=get_value("立即开户")).exists, "跳转到未开户")
#
#                 with allure.step("如果有未开户点击立即开户跳转"):
#                     click_element(d, "立即开户")
#                     # time.sleep(5)
#                     # assert_title(d, "安全登录")
#                     d(resourceId=get_value("晋商弹框")).get_text()
#                     assert_equal_save_picture(d, d(resourceId=get_value("晋商弹框")).get_text(),
#                                               "晋商银行系统升级中，暂时无法提供服务，敬请期待。", "晋商升级弹窗")
#                     click_element(d, "晋商弹框确定")
#                     assert_title(d, "II类户")
#                     # click_element(d, "返回icon")
#                     # assert_title(d, "我的钱包")
#
#
# @allure.feature("39.点击查看全部银行")
# @allure.severity('Critical')
# def test_click_look_all_bank_39(d):
#     """
#     点击查看全部银行
#     :param d:
#     :return:
#     """
#     with allure.step("点击查看全部银行"):
#         click_element(d, "查看全部银行")
#
#     with allure.step("校验是否跳转成功"):
#         assert_element_exists_save_picture(d, d(text="收藏银行").exists, "跳转全部银行收藏银行显示")
#
#     with allure.step("恢复脚本在侧边栏目我的钱包状态"):
#         click_element(d, "底部导航栏（比财）")
#         click_element(d, "首页左上角图标")
#         click_element_with_text(d, "我的钱包", "我的钱包")
#
#
# @allure.feature("40.点击卡券跳转到卡券页")
# @allure.severity('Critical')
# def test_click_card_ticket_40(d):
#     """
#     点击卡券跳转到卡券页
#     :param d:
#     :return:
#     """
#     with allure.step("点击卡券"):
#         d(description=u"卡券").click()
#         time.sleep(2)
#         assert_title(d, "卡券")
#
#     with allure.step("点击返回icon返回我的钱包页"):
#         click_element(d, "返回icon")
#         assert_title(d, "我的钱包")
#
#     click_element(d, "返回icon")
#
#
# @allure.feature("41.点击关于我们")
# @allure.severity('Critical')
# def test_click_understand_bicai_41(d):
#     """
#     点击关于我们
#     :param d:
#     :return:
#     """
#     with allure.step("点击关于我们"):
#         click_element_with_text(d, "关于我们", "关于我们")
#
#     with allure.step("校验收否成功跳转关于我们"):
#         assert_title(d, "关于我们")
#
#     with allure.step("点击使用帮助"):
#         d(description=u"使用帮助").click(timeout=10)
#
#     with allure.step("点击安全说明"):
#         d(description=u"安全说明").click(timeout=10)
#
#     click_element(d, "返回icon")
#
#
# @allure.feature("42.点击签到")
# @allure.severity('Critical')
# def test_click_sign_in_42(d):
#     """
#     点击签到
#     :param d:
#     :return:
#     """
#     if d(resourceId="com.bs.finance:id/tab3_dot").exists:
#         not_sign_in = 1  # 签到上方红点存在，今日还未点击过签到按钮
#     else:
#         not_sign_in = 0  # 签到上方红点不存在，今日已点击过签到按钮
#
#     time.sleep(5)
#
#     with allure.step("点击签到"):
#         click_element(d, "签到")
#
#         time.sleep(5)
#
#     with allure.step("校验是否跳转成功"):
#         assert_title(d, "签到")
#         # time.sleep(10)
#         # 需要添加 查找当天数据 没查到向下滑动 再查 获取当天记录对比
#         # sign_in_state = d(className="android.view.View")[29].info['contentDescription']
#         # assert_equal_save_picture(d, sign_in_state, "今日已签到", "签到")
#
#
# @allure.feature("43.签到抽奖校验")
# @allure.severity('Critical')
# def test_click_sign_in_luck_draw_43(d):
#     """
#     签到抽奖校验
#     :param d:
#     :return:
#     """
#     with allure.step("签到抽奖校验"):
#
#         for i in range(d(className="android.widget.Image").__len__()):
#             if d(className="android.widget.Image")[i].info['contentDescription'] == "5@2x":
#                 print("今日未抽奖")
#                 with allure.step("点击抽奖"):
#                     d(className="android.widget.Image")[i].click()
#                     time.sleep(5)
#                     d(className="android.widget.Image")[i].click()
#                     global red_envelope_money
#                     for j in range(d(className="android.view.View").__len__()):
#                         if "获得" in str(d(className="android.view.View")[j].info['contentDescription']):
#                             global red_envelope_money
#                             red_envelope_money_text = (d(className="android.view.View")[j]).info['contentDescription']
#                             print(red_envelope_money_text)
#                             red_envelope_money = re.findall(r'-?\d+\.?\d*e?-?\d*?', red_envelope_money_text)
#                             print("抽中金额:" + str(red_envelope_money) + "元")
#
#                             with allure.step("点击查看中奖记录"):
#                                 d(description=u"查看我的中奖记录").click()
#                                 #     red_envelope_money_record_text = (d(className="android.view.View")[1]).info['contentDescription']
#                                 #     red_envelope_record_money = re.findall(r'-?\d+\.?\d*e?-?\d*?', red_envelope_money_record_text)
#                                 #
#                                 #     assert_equal_save_picture(d, red_envelope_money, red_envelope_record_money, "抽到红包与最新记录金额对比")
#                                 #
#                                 #     record_date = (d(className="android.view.View")[2]).info['contentDescription']
#                                 #
#                                 #     assert_equal_save_picture(d, record_date, now_date, "抽奖日期对比")
#                                 #
#                                 with allure.step("点击返回"):
#                                     d(className="android.widget.ImageView")[0].click()  # 点击返回
#
#                                     assert_element_exists_save_picture(d, d(description=u"我的中奖记录",
#                                                                             className="android.view.View").exists,
#                                                                        "返回签到页")
#                             break
#
#         print("该用户已抽奖")
#
#         # with allure.step("向下滑动，点击活动规则"):
#         #     d(scrollable=True).scroll.vert.backward()
#         #
#         #     time.sleep(2)
#
#
# @allure.feature("44.查看活动规则")
# @allure.severity('Critical')
# def test_look_activity_rules_44(d):
#     """
#     查看活动规则
#     :param d:
#     :return:
#     """
#     with allure.step("查看活动规则"):
#         d(description=u"活动规则").click(timeout=10)
#
#         time.sleep(2)
#
#         assert_element_exists_save_picture(d, d(description=u"签到抽奖规则").exists, "签到规则跳转")
#
#     with allure.step("点击活动规则关闭"):
#         d(className="android.view.View", instance=1).click(timeout=10)
#
#
# @allure.feature("45.点击分享")
# @allure.severity('Critical')
# def test_click_share_friend_45(d):
#     """
#     点击分享给朋友
#     :param d:
#     :return:
#     """
#     time.sleep(2)
#     with allure.step("点击分享按钮"):
#         d(description=u"分享").click(timeout=10)  # 点击分享
#
#     with allure.step("点击发送给朋友"):
#         d(description=u"发送给朋友", className="android.view.View").click(timeout=10)  # 点击发送给朋友
#
#     with allure.step("选择要发送的人"):
#         d(resourceId="com.tencent.mm:id/lp", text=u"熊出没").click(timeout=10)  # 选择要发送的人
#
#     with allure.step("点击分享"):
#         d(resourceId="com.tencent.mm:id/an3").click(timeout=10)  # 点击分享
#
#     with allure.step("点击返回比财"):
#         d(resourceId="com.tencent.mm:id/an2").click(timeout=10)  # 返回比财
#
#
# @allure.feature("46.点击分享圈")
# @allure.severity('Critical')
# def test_click_share_circle_of_friend_46(d):
#     """
#     点击分享给朋友圈
#     :param d:
#     :return:
#     """
#     time.sleep(2)
#
#     with allure.step("点击分享按钮"):
#         d(description=u"分享").click(timeout=10)  # 点击分享
#
#     with allure.step("点击发送给朋友"):
#         d(description=u"发送到朋友圈").click(timeout=10)  # 点击发送给朋友圈
#
#     with allure.step("选择要发送的人"):
#         d(resourceId="com.tencent.mm:id/hg").click(timeout=10)  # 选择要发送的人
#
#
# @allure.feature("47.签到页查看我的中奖记录")
# @allure.severity('Critical')
# def test_click_my_winning_record_47(d):
#     """
#     在签到页点击我的中奖记录
#     :param d:
#     :return:
#     """
#     with allure.step("向下滑动"):
#         d(scrollable=True).scroll(steps=30)  # 向下滑动
#         time.sleep(2)
#     with allure.step("点击我的中奖记录"):
#         d(description=u"我的中奖记录").click(timeout=10)
#         time.sleep(2)
#         assert_title(d, "签到")
#
#     with allure.step("我的中奖记录中含有今日已发放记录"):
#         assert_element_exists_save_picture(d, d(description=str(now_date)).exists, "签到记录中记录今日签到记录")
#
#     with allure.step("点击我的中奖记录"):
#         click_element(d, "左上角关闭")
#
#
# @allure.feature("48.点击用户调研")
# @allure.severity('Critical')
# def test_click_user_survey_48(d):
#     """
#     点击用户调研
#     :param d:
#     :return:
#     """
#     with allure.step("点击有奖调研"):
#         click_element(d, "有奖调研")
#         assert_title(d, "用户调研")
#
#     with allure.step("点击左上角关闭"):
#         click_element(d, "左上角关闭")
#
#
@allure.feature("0049.点击设置")
@allure.severity('Critical')
def test_click_set_up_49(d):
    """
    点击设置
    :param d:
    :return:
    """
    with allure.step("点击设置"):
        time.sleep(5)

        click_element(d, "侧边栏设置")

    with allure.step("title校验"):
        assert_title(d, "设置")


# @allure.feature("50.点击比财支付密码管理")
# @allure.severity('Critical')
# def test_click_bicai_payment_password_management_50(d):
#     """
#     点击比财支付密码管理
#     :param d:
#     :return:
#     """
#     with allure.step("点击比财支付密码管理"):
#         d(text=u"比财支付密码管理").click()
#         time.sleep(2)
#
#     with allure.step("title校验"):
#         assert_title(d, "密码管理")
#
#
# @allure.feature("51.点击修改密码")
# @allure.severity('Critical')
# def test_click_change_password_51(d):
#     """
#     点击修改密码
#     :param d:
#     :return:
#     """
#     with allure.step("点击修改密码"):
#         d(text=u"修改密码").click()
#         time.sleep(2)
#
#     with allure.step("隐藏数字键盘"):
#         click_element(d, "隐藏数字键盘")
#
#     with allure.step("title校验"):
#         assert_title(d, "修改支付密码")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("52.点击忘记密码")
# @allure.severity('Critical')
# def test_click_forget_password_52(d):
#     """
#     点击忘记密码
#     :param d:
#     :return:
#     """
#     with allure.step("点击忘记密码"):
#         d(text=u"忘记密码").click()
#         time.sleep(2)
#
#     with allure.step("title校验"):
#         assert_title(d, "忘记支付密码")
#
#     with allure.step("控件验证"):
#         user_id = d(resourceId=get_value("反显手机号")).get_text()
#         assert_equal_save_picture(d, user_id, USER_ID.replace((USER_ID[3:7]), "****"), "账号" + USER_ID + "已反显")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("53.点击首页默认")
# @allure.severity('Critical')
# def test_click_home_page_default_53(d):
#     """
#     点击首页默认
#     :param d:
#     :return:
#     """
#     with allure.step("点击首页默认版本"):
#         d(text=u"首页默认显示版本").click()
#
#     with allure.step("title校验"):
#         assert_title(d, "首页默认版本")
#
#     with allure.step("控件存在验证"):
#         assert_element_exists_save_picture(d, "行情版单选", "行情版单选显示")
#         assert_element_exists_save_picture(d, "对比版单选", "对比版单选显示")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("54.消息推送提醒")
# @allure.severity('Critical')
# def test_click_news_push_54(d):
#     """
#     点击消息推送提醒
#     :param d:
#     :return:
#     """
#     with allure.step("开启消息推送提醒"):
#         click_element(d, "消息推送提醒")
#
#     with allure.step("关闭消息推送提醒"):
#         click_element(d, "消息推送提醒")
#
#
# @allure.feature("55.默认安全购买渠道设置")
# @allure.severity('Critical')
# def test_default_purchase_channel_55(d):
#     """
#     默认安全购买渠道设置
#     :param d:
#     :return:
#     """
#     with allure.step("点击默认安全购买渠道设置"):
#         click_element(d, "默认安全购买渠道设置")
#
#     with allure.step("title跳转验证"):
#         assert_title(d, "安全购买渠道设置")
#
#     bank_name = d(resourceId=get_value("银行名称"))
#     for i in range(bank_name.__len__()):
#         print("银行名称为:" + bank_name[i].get_text())
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("56.点击版本更新说明")
# @allure.severity('Critical')
# def test_click_new_version_56(d):
#     """
#     点击版本更新说明
#     :param d:
#     :return:
#     """
#     with allure.step("点击版本更新说明"):
#         click_element(d, "版本更新说明")
#         time.sleep(5)
#
#     with allure.step("校验title"):
#         assert_title(d, "版本更新说明")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("57.点击隐私政策")
# @allure.severity('Critical')
# def test_click_privacy_policy_57(d):
#     """
#     点击隐私政策
#     :param d:
#     :return:
#     """
#     with allure.step("点击隐私政策"):
#         click_element(d, "隐私政策")
#
#     with allure.step("校验title"):
#         assert_title(d, "北京比财数据科技有限公司隐私隐私声明(V1.0版)")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("58.点击联系我们")
# @allure.severity('Critical')
# def test_click_call_me_58(d):
#     """
#     点击联系我们
#     :param d:
#     :return:
#     """
#     with allure.step("点击联系我们"):
#         click_element(d, "联系我们")
#
#     with allure.step("校验title"):
#         assert_title(d, "联系我们")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")
#
#
# @allure.feature("59.点击意见反馈")
# @allure.severity('Critical')
# def test_click_give_feedback_59(d):
#     """
#     点击意见反馈
#     :param d:
#     :return:
#     """
#     with allure.step("点击意见反馈"):
#         click_element(d, "意见反馈")
#
#     with allure.step("校验title"):
#         assert_title(d, "建议与反馈")
#
#     with allure.step("点击返回icon"):
#         click_element(d, "返回icon")


@allure.feature("0060.app退出")
@allure.severity('Critical')
def test_sign_out_app_60(d):
    """
    退出app
    :param d:
    :return:
    """
    with allure.step("点击安全退出"):
        click_element(d, "安全退出")

    with allure.step("点击确认退出_是"):
        click_element(d, "确认退出_是")

    with allure.step("验证app已成功退出"):
        assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

    display_picture(d, "app退出")



