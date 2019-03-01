#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import re
import time
import pytest
import random
from os import path
from Params.params import get_value
from Common import Operate
from Common import Consts
from Common import Assert
import sys

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestSidebar:
    @pytest.allure.feature('Home')
    @pytest.allure.feature("01.启动app后进入比财")
    @pytest.allure.severity('blocker')
    def test_go_main_01(self, d):
        """
        首次启动app点击进入比财,如果有广告页点击x关闭， 
        :param d:
        :return:
        """

        time.sleep(5)

        with pytest.allure.step("启动页点击进入比财"):

            action.click_element(d, "启动页进入比财")

        with pytest.allure.step("如果弹出广告页点x关闭"):
            if d(resourceId=get_value("广告页")).exists:

                action.click_element(d, "广告页关闭")

        with pytest.allure.step("验证启动app点击进入比财是否进入首页"):

            test.assert_element_exists_save_picture(d, d(text="一键登录").exists, "验证是否有文本为一键登录的控件")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @pytest.allure.feature("02.比财登录")
    @pytest.allure.severity('blocker')
    def test_login_02(self, d):
        """
        比财账号登录

        """

        global USER_ID   # 使用账号

        USER_ID = str(get_value("xc手机号"))

        picture_verification_code = str(get_value("四位图片验证码"))

        login_verification_code = str(get_value("登录验证码"))

        with pytest.allure.step("点击app首页一键登录"):
            action.click_element(d, "首页一键登录")

        with pytest.allure.step("在登录页账号输入框输入账号"):
            action.input_element(d, "登录页账号输入框", USER_ID)

        with pytest.allure.step("点击获取验证码"):
            action.click_element(d, "登录页获取验证码按钮")

        with pytest.allure.step("输入4位验证码"):
            time.sleep(2)
            if d(text=u"请填写图像验证码").exists:
                action.input_element(d, "图片验证码输入框", picture_verification_code )
                with pytest.allure.step("点击确认按钮"):
                    action.click_element(d, "图片验证码确定按钮")

        with pytest.allure.step("输入6位验证码"):
            action.input_element(d, "登录验证码输入框", login_verification_code)

        with pytest.allure.step("点击立即登录"):
            action.click_element(d, "立即登录按钮")

        with pytest.allure.step("验证是否登录成功"):
            test.assert_element_exists_save_picture(d, not d(resourceId=get_value("首页一键登录")).exists, "验证是否登录")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @pytest.allure.feature("03.弹出侧边栏")
    @pytest.allure.severity('blocker')
    def test_sidebar_eject_03(self, d):
        """
         验证点击左上角图标弹出侧边栏功能
        """

        global cebian_button  # 侧边栏按钮

        global realname_status  # 实名认证状态

        cebian_button = ["我的关注", "我的消息", "我的钱包", "关于我们"]

        with pytest.allure.step("点击左上角图标"):
            action.click_element(d, "首页左上角图标")
            time.sleep(10)

        with pytest.allure.step("检验侧边栏控件"):
            for i in range(cebian_button.__len__()):
                test.assert_element_exists_save_picture(d, d(text=cebian_button[i]).exists, "验证侧边栏"+cebian_button[i]+"按钮控件存在")

        with pytest.allure.step("验证账号为已登录状态，账号为" + USER_ID):
            user_id = d(resourceId=get_value("侧边栏账号")).get_text()
            test.assert_equal_save_picture(d, user_id, USER_ID.replace((USER_ID[3:7]), "****"), "账号" + USER_ID + "已登录状态")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("04.点击侧边栏目logo")
    @pytest.allure.severity('critical')
    def test_logo_click_04(self, d):
        """
        验证点击侧边栏logo会跳转正确跳到个人资料页，及个人资料页内控件元素存在校验
        :param d:
        :return: 无
        """

        with pytest.allure.step("侧边栏logo点击"):
            action.click_element(d, "侧边栏logo")

        with pytest.allure.step("验证是否跳转个人资料页"):

            test.assert_title(d, "个人资料")  # 验证跳转个人资料页成功

        personal_data = ["性别", "微信", "职业", "实名认证", "手机号", "所在地", "个性签名"]

        global Real_Name_Authentication  # 实名认证状态

        Real_Name_Authentication = d(resourceId=get_value("实名认证状态")).get_text()

        for i in range(personal_data.__len__()):
            test.assert_element_exists_save_picture(d, d(text=personal_data[i]).exists, "控件" + personal_data[i] + "存在")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("05.点击昵称进入修改页")
    @pytest.allure.severity('critical')
    def test_nickname_click_05(self, d):
        """
        验证点击昵称可正确跳转修到昵称修改页
        :param d:
        :return:
        """

        with pytest.allure.step("点击昵称跳转到修改昵称页"):
            action.click_element(d, "个人资料昵称")

        with pytest.allure.step("验证修改昵称页title"):
            test.assert_title(d, "修改昵称")  # 验证是否跳转成功

        action.display_picture(d, "修改昵称页")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("06.修改昵称页修改昵称点击完成")
    @pytest.allure.severity('critical')
    def test_complete_click_06(self, d):
        """
        昵称修改后点击完成验证个人资料页是否显示修改后昵称
        :param d:
        :return:
        """

        with pytest.allure.step("修改昵称为Alex"):
            action.input_element(d, "昵称文本框", "Alex")

        with pytest.allure.step("点击完成按钮返回个人资料页"):
            action.click_element(d, "完成按钮")

        with pytest.allure.step("验证是否跳转个人资料页"):
            test.assert_title(d, "个人资料")  # 验证跳转个人资料页成功

        with pytest.allure.step("验证昵称是否修改成功"):
            test.assert_equal_save_picture(d, d(resourceId=get_value("个人资料昵称")).get_text(), "Alex", "昵称修改")

        # 恢复数据
        action.click_element(d, "个人资料昵称")

        action.input_element(d, "昵称文本框", USER_ID.replace((USER_ID[3:7]), "****"))

        action.click_element(d, "完成按钮")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("07.修改昵称页点击返回icon")
    @pytest.allure.severity('critical')
    def test_nickname_icon_click_07(self, d):
        """
        修改昵称后点击返回icon，查看个人资料页昵称未被修改
        :param d:
        :return:
        """

        with pytest.allure.step("点击昵称跳转到修改昵称页"):
            action.click_element(d, "个人资料昵称")

        with pytest.allure.step("验证修改昵称页是否跳转成功"):
            test.assert_title(d, "修改昵称")  # 验证是否跳转成功

        with pytest.allure.step("修改昵称为Alex"):
            action.input_element(d, "昵称文本框", "Alex")

        with pytest.allure.step("点击修改昵称页返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证是否跳转个人资料页"):
            test.assert_title(d, "个人资料")  # 验证跳转个人资料页成功

        with pytest.allure.step("验证昵称不会被修改"):
            test.assert_equal_save_picture(d, d(resourceId=get_value("个人资料昵称")).get_text(), USER_ID.replace((USER_ID[3:7]), "****"), "昵称未做修改")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("08.修改性别")
    @pytest.allure.severity('critical')
    def test_modify_sex_08(self, d):
        """
        修改性别，如果是男就修改成女，如果是女就修改成男
        :param d:
        :return:
        """

        with pytest.allure.step("点击性别"):
            sex_text = d(resourceId=get_value("性别文本")).get_text()

            action.click_element(d, "性别")

        with pytest.allure.step("修改性别"):
            if sex_text == "男":
                action.click_element(d, "选项女")
            elif sex_text == "女":
                action.click_element(d, "选项男")
            else:
                print("无此选项")

        with pytest.allure.step("验证性别修改是否成功"):
            modify_sex_text = d(resourceId=get_value("性别文本")).get_text()
            if sex_text == "男":
                test.assert_equal_save_picture(d, modify_sex_text, "女", "性别修改为女")
            elif sex_text == "女":
                test.assert_equal_save_picture(d, modify_sex_text, "男", "性别修改为男")
            else:
                print("无此选项")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("09.修改职业")
    @pytest.allure.severity('critical')
    def test_modify_profession_09(self, d):
        """
        修改职业，如果是测试就修改为码农，如果是码农就修改为测试，并校验
        :param d:
        :return:
        """

        with pytest.allure.step("点击职业"):
            action.click_element(d, "职业")

        with pytest.allure.step("验证跳转职业修改页title"):
            test.assert_title(d, "职业")

        modify_profession_text = d(resourceId=get_value("职业文本")).get_text()

        with pytest.allure.step("修改职业"):
            if modify_profession_text == "测试":
                action.input_element(d, "职业文本", "码农")
            elif modify_profession_text == "码农":
                action.input_element(d, "职业文本", "测试")
            else:
                action.input_element(d, "职业文本", "码农")

        with pytest.allure.step("点击完成"):
            action.click_element(d, "完成")

        with pytest.allure.step("验证是否修改成功"):
            modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

            if modify_profession_text == "测试":
                test.assert_equal_save_picture(d, modify_profession_display, "码农", "职业修改")
            elif modify_profession_text == "码农":
                test.assert_equal_save_picture(d, modify_profession_display, "测试", "职业修改")
            else:
                test.assert_equal_save_picture(d, modify_profession_display, "码农", "职业修改")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("10.修改职业点击返回icon")
    @pytest.allure.severity('critical')
    def test_modify_profession_icon_10(self, d):
        """
        修改职业后点击返回icon
        :param d:
        :return:
        """

        with pytest.allure.step("点击职业"):
            action.click_element(d, "职业")

        global modify_profession_text

        modify_profession_text = d(resourceId=get_value("职业文本")).get_text()

        with pytest.allure.step("修改职业"):
            if modify_profession_text == "测试":
                action.input_element(d, "职业文本", "码农")
            elif modify_profession_text == "码农":
                action.input_element(d, "职业文本", "测试")
            else:
                action.input_element(d, "职业文本", "码农")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证职业是否被修改"):
            modify_profession_display = d(resourceId=get_value("职业展示")).get_text()

            if modify_profession_text == "测试":
                test.assert_equal_save_picture(d, modify_profession_display, "测试", "职业未做修改")
            elif modify_profession_text == "码农":
                test.assert_equal_save_picture(d, modify_profession_display, "码农", "职业未做修改")
            else:
                test.assert_equal_save_picture(d, modify_profession_display, "测试", "职业未做修改")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("11.修改职业输入框输入内容点击取消")
    @pytest.allure.severity('critical')
    def test_modify_profession_clear_11(self, d):
        """
        修改职业输入内容后显示取消按钮，点击取消按钮删除清空输入内容
        :param d:
        :return:
        """

        with pytest.allure.step("点击职业"):
            action.click_element(d, "职业")

        with pytest.allure.step("验证不存在清除按钮"):
            test.assert_element_exists_save_picture(d, not d(resourceId=get_value("清除按钮")).exists, "不显示清除按钮")

        with pytest.allure.step("修改职业文本框内容"):

            if modify_profession_text == "测试":
                action.input_element(d, "职业文本", "码农")
            elif modify_profession_text == "码农":
                action.input_element(d, "职业文本", "测试")
            else:
                action.input_element(d, "职业文本", "码农")

        with pytest.allure.step("验证清除按钮存在"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("清除按钮")).exists, "显示清除按钮")

        with pytest.allure.step("点击清除按钮"):

            action.click_element(d, "清除按钮")

        with pytest.allure.step("文本内容被清除"):

            modify_profession_display = d(resourceId=get_value("职业文本")).get_text()

            if modify_profession_display is None:
                # action.display_picture(d, "清除内容_成功")
                assert modify_profession_display is None
            else:
                action.display_picture(d, "清除内容_失败")
                assert modify_profession_display is None

        action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("12.手机号校验")
    @pytest.allure.severity('critical')
    def test_phone_number_check_12(self, d):
        """
        个人资料手机号与登录账号对比校验
        :param d:
        :return:
        """

        with pytest.allure.step("手机号检查"):
            test.assert_equal_save_picture(d, USER_ID, d(resourceId=get_value("手机号")).get_text(), "个人资料手机号与登录账号对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("13.所在地修改")
    @pytest.allure.severity('critical')
    def test_modify_address_13(self, d):
        """
        所在地修改，如果是北京朝阳区三环到四环之间或其他地址就修改为上海徐汇区城区，反之修改为北京朝阳区三环到四环之间
        :param d:
        :return:
        """

        with pytest.allure.step("点击所在地"):
            address_text = d(resourceId=get_value("居住地址文本")).get_text()
            action.click_element(d, "居住地址文本")

        with pytest.allure.step("验证修改地址页title"):
            test.assert_title(d, "居住地址")

        with pytest.allure.step("选择所在地区"):

            action.click_element(d, "所在地区文本")

        if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
            d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
            time.sleep(1)
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text, "上海徐汇区城区", "所在地区修改为上海")

            action.input_element(d, "详细地址文本", "外滩")
            detailed_address_text = (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', '')
            print("**********************")
            print(detailed_address_text)
            print("**********************")
            test.assert_equal_save_picture(d, detailed_address_text, "外滩", "详细地址修改为外滩")

        elif address_text.replace(' ', '') == "上海徐汇区城区":
            d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
            time.sleep(1)
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text, "北京朝阳区三环到四环之间", "地区修改")

            action.input_element(d, "详细地址文本", "安定门")

            test.assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''), "安定门", "详细地址修改")

        else:
            d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
            time.sleep(1)
            action.input_element(d, "详细地址文本", "外滩")
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text, "上海徐汇区城区", "所在地区修改为上海")

            action.input_element(d, "详细地址文本", "外滩")

            test.assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''), location_text, "详细地址修改为外滩")

        with pytest.allure.step("点击完成"):

            action.click_element(d, "完成")

            modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()

            if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "地址修改")
            elif address_text.replace(' ', '') == "上海徐汇区城区":
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "北京朝阳区三环到四环之间", "地址修改")
            else:
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "地址修改")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("14.修改所在地点击返回icon")
    @pytest.allure.severity('critical')
    def test_modify_address_clear_14(self, d):
        """
        修改地址后点击返回icon查看内容是否未被修改
        :param d:
        :return:
        """

        with pytest.allure.step("点击所在地"):
            address_text = d(resourceId=get_value("居住地址文本")).get_text()
            action.click_element(d, "居住地址文本")

        with pytest.allure.step("验证修改地址页title"):
            test.assert_title(d, "居住地址")

        with pytest.allure.step("选择所在地区"):

            action.click_element(d, "所在地区文本")

        if address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
            d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
            time.sleep(1)
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text,
                                      "上海徐汇区城区", "地区修改")

            action.input_element(d, "详细地址文本", "外滩")

            test.assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
                                      "外滩", "文本修改")

        elif address_text.replace(' ', '') == "上海徐汇区城区":
            d(resourceId="com.bs.finance:id/textView", text=u"北京").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"朝阳区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"三环到四环之间").click()
            time.sleep(1)
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text, "北京朝阳区三环到四环之间", "地区修改")

            action.input_element(d, "详细地址文本", "安定门")

            test.assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
                                      "安定门", "详细地址修改")

        else:
            d(resourceId="com.bs.finance:id/textView", text=u"上海").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"徐汇区").click()
            time.sleep(1)
            d(resourceId="com.bs.finance:id/textView", text=u"城区").click()
            time.sleep(1)
            action.input_element(d, "详细地址文本", "外滩")
            location_text = (d(resourceId=get_value("所在地区文本")).get_text()).replace(' ', '')
            test.assert_equal_save_picture(d, location_text, "上海徐汇区城区", "地区修改")

            action.input_element(d, "详细地址文本", "外滩")

            test.assert_equal_save_picture(d, (d(resourceId=get_value("详细地址文本")).get_text()).replace(' ', ''),
                                      "外滩", "文本修改")

        with pytest.allure.step("点击返回icon"):

            action.click_element(d, "返回icon")

            modify_address_text = d(resourceId=get_value("居住地址文本")).get_text()

            if address_text.replace(' ', '') == "上海徐汇区城区":
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "点击返回icon居住地址校验")
            elif address_text.replace(' ', '') == "北京朝阳区三环到四环之间":
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "北京朝阳区三环到四环之间", "点击返回icon居住地址校验")
            else:
                test.assert_equal_save_picture(d, modify_address_text.replace(' ', ''), "上海徐汇区城区", "点击返回icon居住地址校验")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("15.修改个性签名")
    @pytest.allure.severity('critical')
    def test_modify_personalized_signature_15(self, d):
        """
        修改个性签名
        :param d:
        :return:
        """

        with pytest.allure.step("点击个性签名跳转个性签名修改页"):
            action.click_element(d, "个性签名")
            test.assert_title(d, "个性签名")

        with pytest.allure.step("编辑个性签名"):

            personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

            if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":

                action.input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

            elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":

                action.input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")

            else:

                action.input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

        with pytest.allure.step("点击完成"):

            action.click_element(d, "完成")

        with pytest.allure.step("验证是否修改成功"):

            action.click_element(d, "个性签名")

            modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

            if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
                test.assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
                                          "噜起袖子加油干一张蓝图绘到底", "修改个性签名")
            elif personalized_signature_text.replace(' ', '') == "噜起袖子加油干一张蓝图绘到底":
                test.assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
                                          "企业要想好踏踏实实搞成天作报告那可好不了", "修改个性签名")
            else:
                test.assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
                                          "噜起袖子加油干一张蓝图绘到底", "修改个性签名")

        action.click_element(d, "完成")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("16.修改个性签名后点击返回icon")
    @pytest.allure.severity('critical')
    def test_modify_personalized_signature_clear_16(self, d):
        """
        修改个性签名点击返回icon
        :param d:
        :return:
        """

        with pytest.allure.step("点击个性签名跳转个性签名修改页"):
            action.click_element(d, "个性签名")
            test.assert_title(d, "个性签名")

        with pytest.allure.step("编辑个性签名"):

            personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

            if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
                action.input_element(d, "个性签名文本框", "噜起袖子加油干一张蓝图绘到底")

            else:
                action.input_element(d, "个性签名文本框", "企业要想好踏踏实实搞成天作报告那可好不了")

        with pytest.allure.step("点击返回icon"):

            action.click_element(d, "返回icon")

        with pytest.allure.step("验证是否修改成功"):

            action.click_element(d, "个性签名")

            modify_personalized_signature_text = d(resourceId=get_value("个性签名文本框")).get_text()

            if personalized_signature_text.replace(' ', '') == "企业要想好踏踏实实搞成天作报告那可好不了":
                test.assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
                                          "企业要想好踏踏实实搞成天作报告那可好不了", "修改点返回icon签名不会修改")
            else:
                test.assert_equal_save_picture(d, modify_personalized_signature_text.replace(' ', ''),
                                          "噜起袖子加油干一张蓝图绘到底", "修改点返回icon签名不会修改")

        action.click_element(d, "返回icon")

        action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("17.验证实名状态")
    @pytest.allure.severity('critical')
    def test_check_real_name_authentication_state_17(self, d):
        """
        根据个人资料中实名认证状态检验是否已实名
        :param d:
        :return:
        """

        with pytest.allure.step("点击实名认证"):

            action.click_element(d, "是否实名")

        with pytest.allure.step("是否已实名验证"):

            if Real_Name_Authentication == "已认证":

                test.assert_title(d, "认证完成")

                action.display_picture(d, "用户已实名")

            elif Real_Name_Authentication == "未认证":

                test.assert_title(d, "身份证认证")

                action.display_picture(d, "用户未实名")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("18.实名认证页返回icon点击")
    @pytest.allure.severity('critical')
    def test_real_name_click_icon_18(self, d):
        """
        实名状态页点击返回icon
        :param d:
        :return:
        """

        with pytest.allure.step("实名验证页面点击返回icon"):
            action.click_element(d, "返回icon")

        action.display_picture(d, "实名认证页面点击返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("19.验证绑卡状态")
    @pytest.allure.severity('critical')
    def test_check_tied_card_state_19(self, d):
        """
        根据个人资料中实名认证状态检验是否绑卡
        :param d:
        :return:
        """

        with pytest.allure.step("点击绑卡状态"):

            action.click_element(d, "是否绑卡")

        with pytest.allure.step("是否已绑定卡"):

            if Real_Name_Authentication == "已认证":

                test.assert_title(d, "银行卡")
                global cards_number
                cards_name_a = []
                cards_name_b = []
                card_name = d(resourceId=get_value("银行名称"))  # 获取卡数量

                for i in range(card_name.__len__()):
                    print(card_name[i].get_text())
                    cards_name_a.append(card_name[i].get_text())
                print(cards_name_a)

                d(scrollable=True).scroll(steps=30)  # 向下滑动

                time.sleep(5)

                for i in range(card_name.__len__()):
                    print(card_name[i].get_text())
                    cards_name_b.append(card_name[i].get_text())

                print(cards_name_b)

                cards_name_c = list(set(cards_name_a + cards_name_b))

                print(cards_name_c)

                cards_number = cards_name_c.__len__()

            elif Real_Name_Authentication == "未认证":

                test.assert_title(d, "身份证认证")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("20.绑定银行卡页icon点击")
    @pytest.allure.severity('critical')
    def test_tied_card_click_icon_20(self, d):
        """
        绑卡页点击返回icon
        :param d:
        :return:
        """

        with pytest.allure.step("实名验证页面点击返回icon"):
            action.click_element(d, "返回icon")

        action.display_picture(d, "实名认证页面点击返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("21.已实名中点击查看榜单返回app首页")
    @pytest.allure.severity('critical')
    def test_check_list_click_21(self, d):
        """
        已经实名用户点击查看绑定
        :param d:
        :return:
        """

        with pytest.allure.step("点击实名认证"):

            action.click_element(d, "是否实名")

        with pytest.allure.step("点击查看榜单"):

            if Real_Name_Authentication == "已认证":
                action.click_element(d, "查看榜单")
                test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
                action.click_element(d, "首页左上角图标")
            else:
                print("用户未实名")
                action.click_element(d, "返回icon")
                pass
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("22.添加银行卡")
    @pytest.allure.severity('critical')
    def test_add_bank_cards_22(self, d):
        """
        添加银行卡
        :param d:
        :return:
        """

        with pytest.allure.step("点击绑卡状态"):

            action.click_element(d, "是否绑卡")

        with pytest.allure.step("添加银行卡"):

            if Real_Name_Authentication == "已认证":

                d(scrollable=True).scroll(steps=10)

                action.click_element(d, "添加银行卡")

                with pytest.allure.step("数字键盘显示"):

                    for i in range(10):
                        num_element = "com.bs.finance:id/tv_keyboard_"+str(i)
                        test.assert_element_exists_save_picture(d, d(resourceId=num_element).exists, "数字键盘显示")

                    test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/fl_keyboard_del").exists, "删除键盘显示")

                action.display_picture(d, "添加银行卡")

                with pytest.allure.step("隐藏数字键盘"):

                    action.click_element(d, "隐藏数字键盘")

                    for i in range(10):
                        num_element = "com.bs.finance:id/tv_keyboard_"+str(i)
                        test.assert_element_exists_save_picture(d, not d(resourceId=num_element).exists, "隐藏数字键盘")

                    test.assert_element_exists_save_picture(d, not d(resourceId="com.bs.finance:id/fl_keyboard_del").exists,
                                                       "隐藏数字键盘删除键")

                with pytest.allure.step("添加银行卡title校验"):

                    test.assert_title(d, "添加银行卡")

                with pytest.allure.step("点击返回icon"):

                    action.click_element(d, "返回icon")

                    test.assert_title(d, "银行卡")

                    action.click_element(d, "返回icon")

            else:
                print("用户未实名认证")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("23.点击我的关注")
    @pytest.allure.severity('critical')
    def test_click_my_concern_23(self, d):
        """
        点击我的关注，校验内容
        :param d:
        :return:
        """
    
        with pytest.allure.step("我的关注"):
            action.click_element(d, "我的关注")

            test.assert_title(d, "我的关注")

            global product_type

            product_type = ["货币基金", "理财产品", "纯债基金", "智能存款", "活期存款", "结构性存款"]

            with pytest.allure.step("校验我的关注内容"):
                for i in range(product_type.__len__()):
                    test.assert_element_exists_save_picture(d, d(text=product_type[i]).exists, "校验我的关注内容")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("24.验证关注内内容")
    @pytest.allure.severity('critical')
    def test_click_my_concern_content_24(self, d):
        """
        验证我的关注内下一页内容
        :param d:
        :return:
        """
     
        with pytest.allure.step("将关注页内容保存到字典"):
            product_type_dict = {}
            for i in range(product_type.__len__()):
                product_type_dict[product_type[i]] = d(resourceId=get_value("关注产品类型"))[i].get_text()

            print(product_type_dict)

        for j in range(product_type.__len__()):
            d(text=product_type[j]).click()
            time.sleep(2)
            with pytest.allure.step("for循环对比关注条数和类型页展示条数"):
                if int(product_type_dict[product_type[j]]) == 0:
                    action.display_picture(d, "无关注" + str(j + 1))
                    print(product_type_dict[product_type[j]])
                    test.assert_title(d, product_type[j])
                    test.assert_element_exists_save_picture(d, d(resourceId=get_value("缺省页文本")).exists, "无关注省却页展示")
                    test.assert_equal_save_picture(d, d(resourceId=get_value("缺省页文本")).get_text(),
                                              "对不起，目前没有数据", "省缺页文本校验")
                    action.click_element(d, "返回icon")
                else:
                    action.display_picture(d, "有关注" + str(j + 1))
                    print("我的关注页统计:" + product_type_dict[product_type[j]] + "条")
                    print("产品类型页显示:" + str(d(resourceId=get_value("产品标题")).__len__()) + "条")
                    test.assert_element_exists_save_picture(d, not d(resourceId=get_value("缺省页文本")).exists, "有关注不展示缺省页")
                    with pytest.allure.step("对比我的关注页统计条数和产品类型页显示条数"):
                        test.assert_equal_save_picture(d, int(product_type_dict[product_type[j]]),
                                                  d(resourceId=get_value("产品标题")).__len__(), "关注条目数量校验")
                    with pytest.allure.step("点击返回icon"):
                        action.click_element(d, "返回icon")
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("25.点击我的消息")
    @pytest.allure.severity('critical')
    def test_click_my_news_25(self, d):
        """
        点击我的消息
        :param d:
        :return:
        """
        massage_type = ["系统消息", "产品消息", "活动"]

        with pytest.allure.step("点击我的消息"):
            action.click_element_with_text(d, "我的消息", "我的消息")

        with pytest.allure.step("校验跳转后title"):
            test.assert_title(d, "消息")

        with pytest.allure.step("校验消息内内容"):
            for i in range(massage_type.__len__()):
                with pytest.allure.step("点击消息内条目跳转"+"进入"+str(massage_type[i])):
                    action.click_element_with_text(d, "我的消息", massage_type[i])
                with pytest.allure.step("校验跳转后title显示"):
                    test.assert_title(d, massage_type[i])
                with pytest.allure.step("点击返回icon"):
                    action.click_element(d, "返回icon")
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("26.点击我的钱包")
    @pytest.allure.severity('critical')
    def test_click_bicai_wallet_26(self, d):
        """
        点击我的钱包跳转
        :param d:
        :return:
        """
        global remaining_sum_type  # 首次点击进入账户余额显示/隐藏状态记录
        global change_remaining_sum_type  # 再次进入账户余额显示/隐藏状态记录
        with pytest.allure.step("点击我的钱包"):
            action.click_element_with_text(d, "我的钱包", "我的钱包")
            test.assert_title(d, "我的钱包")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("27.点击常见问题")
    @pytest.allure.severity('critical')
    def test_click_common_problem_27(self, d):
        """
        点击常见问题跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击常见问题"):
            action.click_element(d, "常见问题")
            test.assert_title(d, "常见问题")
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("28.点击明细")
    @pytest.allure.severity('critical')
    def test_click_detailed_28(self, d):
        """
        点击明细，跳转明细页默认选择收益明细
        :param d:
        :return:
        """
        with pytest.allure.step("点击明细"):
            d(description=u"明细").click()
            time.sleep(2)
            test.assert_title(d, "明细")

        with pytest.allure.step("默认选择为收益明细"):
            test.assert_element_exists_save_picture(d, d(className="android.widget.ImageView", instance=3).exists, "默认选择收益明细")

        with pytest.allure.step("日期图标显示"):
            test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/iv_date").exists, "日期图标显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("29.点击交易记录")
    @pytest.allure.severity('critical')
    def test_click_business_record_29(self, d):
        """
        切换交易明细页，日期图标被隐藏
        :param d:
        :return:
        """
        with pytest.allure.step("点击交易记录"):
            action.click_element(d, "交易记录")
            test.assert_title(d, "明细")

        with pytest.allure.step("交易记录下划线显示"):
            test.assert_element_exists_save_picture(d, d(className="android.widget.ImageView", instance=2).exists,
                                               "交易记录下划线显示")

        with pytest.allure.step("日期图标显示"):
            test.assert_element_exists_save_picture(d,not d(resourceId="com.bs.finance:id/iv_date").exists, "日期图标隐藏")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("30.点击交易记录页内容")
    @pytest.allure.severity('critical')
    def test_click_business_record_content_30(self, d):
        """
        如果交易记录页中有内容点击进入
        :param d:
        :return:
        """
        if d(className="android.widget.RelativeLayout", instance=2).exists:
            with pytest.allure.step("点击交易记录页首条记录"):
                d(className="android.widget.RelativeLayout", instance=2).click()
                time.sleep(2)
                test.assert_title(d, "交易明细")

            with pytest.allure.step("点击返回icon"):
                action.click_element(d, "返回icon")
        else:
            print("该账号没有做过交易")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("31.点击提现")
    @pytest.allure.severity('critical')
    def test_click_cash_withdrawal_31(self, d):
        """
        点击提现
        :param d:
        :return:
        """
        with pytest.allure.step("点击提现"):
            d(description=u"提现").click()
            time.sleep(2)
            test.assert_title(d, "余额提现")

        with pytest.allure.step("正则匹配可提现余额"):
            global balance  # 可提现余额
            balance_text = d(resourceId="com.bs.finance:id/wallet_get_cash_tv_money_tip").get_text()
            balance = re.findall(r'-?\d+\.?\d*e?-?\d*?', balance_text)
            print("可提现余额：" + str(balance[0]))
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("32.验证进入提现页提现按钮默认不可点")
    @pytest.allure.severity('critical')
    def test_cash_withdrawal_clickenable_32(self, d):
        """
        验证页面跳转后提现按钮不可点击
        :param d:
        :return:
        """
        with pytest.allure.step("验证进入提现页提现按钮默认不可点"):
            test.assert_element_exists_save_picture(d, not d(resourceId=get_value("提现按钮")).info["clickable"],
                                               "提现按钮默认不可点")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("33.验证输入大于等于10元提现金额按钮可点击")
    @pytest.allure.severity('critical')
    def test_cash_withdrawal_clickable_33(self, d):
        """
        验证页面输入大于等于10元随机金额提现按钮可以点击
        :param d:
        :return:
        """
        with pytest.allure.step("验证输入大于等于10元提现按钮可以点击"):
            if float(balance[0]) >= 10.00:
                input_money_text = random.uniform(10.00, float(balance[0]))
                input_money = round(input_money_text, 2)  # 随机生成大于10元小于可提现金额随机浮点数
                action.input_element(d, "余额提现页金额输入框", str(input_money))
                test.assert_element_exists_save_picture(d, d(resourceId=get_value("提现按钮")).info["clickable"],
                                                   "余额和提现金额大于10提现按钮可点击")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("34.验证输入小等10元提现金额按钮不可点击")
    @pytest.allure.severity('critical')
    def test_cash_withdrawal_clickable__less_than_ten_34(self, d):
        """
        验证页面输入小于10元随机金额提现按钮不可点击
        :param d:
        :return:
        """
        with pytest.allure.step("验证输入小于10元提现按钮不可点击"):
            action.input_element(d, "余额提现页金额输入框", str(9.99))
            test.assert_element_exists_save_picture(d, not d(resourceId=get_value("提现按钮")).info["clickable"],
                                               "余额提现金额小于10提现不可点")

        action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("35.账户余额隐藏显示状态校验")
    @pytest.allure.severity('critical')
    def test_balance_display_hide_35(self, d):
        """
        账户余额校验
        :param d:
        :return:
        """
        with pytest.allure.step("获取账户余额显示隐藏状态"):
            if d(description=u"****").exists:
                print("当前账户余额金额显示状态为:隐藏")
                remaining_sum_type = 1  # 金额隐藏

            elif d(description=str(balance[0])).exists:
                print("当前账户余额金额显示状态为:显示")
                remaining_sum_type = 0  # 金额显示

        with pytest.allure.step("点击显示/隐藏图标"):
            d(className="android.widget.Button").click()

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("再次点击进入我的钱包"):
            action.click_element_with_text(d, "我的钱包", "我的钱包")
            test.assert_title(d, "我的钱包")

        with pytest.allure.step("获取改变后账户余额显示隐藏状态"):
            if d(description=str(balance[0])).exists:
                print("当前账户余额金额显示状态为:显示")
                change_remaining_sum_type = 1  # 金额显示

            elif d(description=u"****").exists:
                print("当前账户余额金额显示状态为:隐藏")
                change_remaining_sum_type = 0  # 金额隐藏

        with pytest.allure.step("金额显示/隐藏状态对比"):
            test.assert_equal_save_picture(d, remaining_sum_type, change_remaining_sum_type, "金额显示/隐藏状态对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("36.点击我的钱包银行卡跳转")
    @pytest.allure.severity('critical')
    def test_click_card_button_36(self, d):
        """
        点击我的钱包银行卡跳转
        :param d:
        :return:
        """
        card_button_text = "银行卡(" + str(cards_number) + ")"
        with pytest.allure.step("点击银行卡跳转"):
            d(description=card_button_text).click()
            time.sleep(2)

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "银行卡")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("37.点击II类户跳转")
    @pytest.allure.severity('critical')
    def test_click_type_two_accounts_37(self, d):
        """
        点击二类户跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击II类户（图片）跳转"):
            d(description=u"A37H3tXWoJVwAAAAAASUVORK5CYII=").click()
            time.sleep(1)

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "II类户")
            type_two_accounts_number = (d(resourceId="com.bs.finance:id/bg_bank_item")).__len__()
            print("已绑定二类户数量为:"+str(type_two_accounts_number))

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("点击II类户按钮跳转并校验已经绑定二类户数量"):
            type_two_accounts_text = "Ⅱ类户(" + str(type_two_accounts_number) + ")"
            d(description=str(type_two_accounts_text)).click()
            time.sleep(2)

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "II类户")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("38.点击未开户")
    @pytest.allure.severity('critical')
    def test_click_not_opening_bank_38(self, d):
        """
        点击二类户跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击未开户"):
            action.click_element_with_text(d, "未开户", "未开户")
        with pytest.allure.step("校验是否跳转到未开户"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("查看全部银行")).exists, "查看全部银行按钮显示")

            if d(resourceId=get_value("银行卡展示")).__len__() >= 1:

                if d(resourceId=get_value("银行名称")).get_text() == "晋享财富":
                    test.assert_element_exists_save_picture(d, d(resourceId=get_value("立即开户")).exists, "跳转到未开户")

                    with pytest.allure.step("如果有未开户点击立即开户跳转"):
                        action.click_element(d, "立即开户")
                        # time.sleep(5)
                        # test.assert_title(d, "安全登录")
                        d(resourceId=get_value("晋商弹框")).get_text()
                        test.assert_equal_save_picture(d, d(resourceId=get_value("晋商弹框")).get_text(),
                                                  "晋商银行系统升级中，暂时无法提供服务，敬请期待。", "晋商升级弹窗")
                        action.click_element(d, "晋商弹框确定")
                        test.assert_title(d, "II类户")
                        # action.click_element(d, "返回icon")
                        # test.assert_title(d, "我的钱包")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("39.点击查看全部银行")
    @pytest.allure.severity('critical')
    def test_click_look_all_bank_39(self, d):
        """
        点击查看全部银行
        :param d:
        :return:
        """
        with pytest.allure.step("点击查看全部银行"):
            action.click_element(d, "查看全部银行")

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_element_exists_save_picture(d, d(text="收藏银行").exists, "跳转全部银行收藏银行显示")

        with pytest.allure.step("恢复脚本在侧边栏目我的钱包状态"):
            action.click_element(d, "底部导航栏（比财）")
            action.click_element(d, "首页左上角图标")
            action.click_element_with_text(d, "我的钱包", "我的钱包")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("40.点击卡券跳转到卡券页")
    @pytest.allure.severity('critical')
    def test_click_card_ticket_40(self, d):
        """
        点击卡券跳转到卡券页
        :param d:
        :return:
        """
        with pytest.allure.step("点击卡券"):
            d(description=u"卡券").click()
            time.sleep(2)
            test.assert_title(d, "卡券")

        with pytest.allure.step("点击返回icon返回我的钱包页"):
            action.click_element(d, "返回icon")
            test.assert_title(d, "我的钱包")

        action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("41.点击关于我们")
    @pytest.allure.severity('critical')
    def test_click_understand_bicai_41(self, d):
        """
        点击关于我们
        :param d:
        :return:
        """
        with pytest.allure.step("点击关于我们"):
            action.click_element_with_text(d, "关于我们", "关于我们")

        with pytest.allure.step("校验收否成功跳转关于我们"):
            test.assert_title(d, "关于我们")

        with pytest.allure.step("点击使用帮助"):
            d(description=u"使用帮助").click(timeout=10)

        with pytest.allure.step("点击安全说明"):
            d(description=u"安全说明").click(timeout=10)

        action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')


    @pytest.allure.feature('Personal')
    @pytest.allure.feature("48.点击用户调研")
    @pytest.allure.severity('critical')
    def test_click_user_survey_48(self, d):
        """
        点击用户调研
        :param d:
        :return:
        """

        with pytest.allure.step("点击有奖调研"):
            action.click_element(d, "有奖调研")
            test.assert_title(d, "用户调研")

        with pytest.allure.step("点击左上角关闭"):
            action.click_element(d, "左上角关闭")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @pytest.allure.feature("49.点击设置")
    @pytest.allure.severity('blocker')
    def test_click_set_up_49(self, d):
        """
        点击设置
        :param d:
        :return:
        """

        with pytest.allure.step("点击设置"):

            time.sleep(5)

            action.click_element(d, "侧边栏设置")

        with pytest.allure.step("title校验"):
            test.assert_title(d, "设置")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("50.点击比财支付密码管理")
    @pytest.allure.severity('critical')
    def test_click_bicai_payment_password_management_50(self, d):
        """
        点击比财支付密码管理
        :param d:
        :return:
        """

        with pytest.allure.step("点击比财支付密码管理"):
            d(text=u"比财支付密码管理").click()
            time.sleep(2)

        with pytest.allure.step("title校验"):
            test.assert_title(d, "密码管理")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("51.点击修改密码")
    @pytest.allure.severity('critical')
    def test_click_change_password_51(self, d):
        """
        点击修改密码
        :param d:
        :return:
        """

        with pytest.allure.step("点击修改密码"):
            d(text=u"修改密码").click()
            time.sleep(2)

        with pytest.allure.step("隐藏数字键盘"):
            action.click_element(d, "隐藏数字键盘")

        with pytest.allure.step("title校验"):
            test.assert_title(d, "修改支付密码")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("52.点击忘记密码")
    @pytest.allure.severity('critical')
    def test_click_forget_password_52(self, d):
        """
        点击忘记密码
        :param d:
        :return:
        """

        with pytest.allure.step("点击忘记密码"):
            d(text=u"忘记密码").click()
            time.sleep(2)

        with pytest.allure.step("title校验"):
            test.assert_title(d, "忘记支付密码")

        with pytest.allure.step("控件验证"):
            user_id = d(resourceId=get_value("反显手机号")).get_text()
            test.assert_equal_save_picture(d, user_id, USER_ID.replace((USER_ID[3:7]), "****"), "账号" + USER_ID + "已反显")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("53.点击首页默认")
    @pytest.allure.severity('critical')
    def test_click_home_page_default_53(self, d):
        """
        点击首页默认
        :param d:
        :return:
        """

        with pytest.allure.step("点击首页默认版本"):
            d(text=u"首页默认显示版本").click()

        with pytest.allure.step("title校验"):
            test.assert_title(d, "首页默认版本")

        with pytest.allure.step("控件存在验证"):
            test.assert_element_exists_save_picture(d, "行情版单选", "行情版单选显示")
            test.assert_element_exists_save_picture(d, "对比版单选", "对比版单选显示")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("54.消息推送提醒")
    @pytest.allure.severity('critical')
    def test_click_news_push_54(self, d):
        """
        点击消息推送提醒
        :param d:
        :return:
        """

        with pytest.allure.step("开启消息推送提醒"):
            action.click_element(d, "消息推送提醒")

        with pytest.allure.step("关闭消息推送提醒"):
            action.click_element(d, "消息推送提醒")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("55.默认安全购买渠道设置")
    @pytest.allure.severity('critical')
    def test_default_purchase_channel_55(self, d):
        """
        默认安全购买渠道设置
        :param d:
        :return:
        """

        with pytest.allure.step("点击默认安全购买渠道设置"):
            action.click_element(d, "默认安全购买渠道设置")

        with pytest.allure.step("title跳转验证"):
            test.assert_title(d, "安全购买渠道设置")

        bank_name = d(resourceId=get_value("银行名称"))
        for i in range(bank_name.__len__()):
            print("银行名称为:"+bank_name[i].get_text())

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("56.点击版本更新说明")
    @pytest.allure.severity('critical')
    def test_click_new_version_56(self, d):
        """
        点击版本更新说明
        :param d:
        :return:
        """

        with pytest.allure.step("点击版本更新说明"):
            action.click_element(d, "版本更新说明")
            time.sleep(5)

        with pytest.allure.step("校验title"):
            test.assert_title(d, "版本更新说明")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("57.点击隐私政策")
    @pytest.allure.severity('critical')
    def test_click_privacy_policy_57(self, d):
        """
        点击隐私政策
        :param d:
        :return:
        """

        with pytest.allure.step("点击隐私政策"):
            action.click_element(d, "隐私政策")

        with pytest.allure.step("校验title"):
            test.assert_title(d, "隐私政策")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("58.点击联系我们")
    @pytest.allure.severity('critical')
    def test_click_call_me_58(self, d):
        """
        点击联系我们
        :param d:
        :return:
        """

        with pytest.allure.step("点击联系我们"):
            action.click_element(d, "联系我们")

        with pytest.allure.step("校验title"):
            test.assert_title(d, "联系我们")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Personal')
    @pytest.allure.feature("59.点击意见反馈")
    @pytest.allure.severity('critical')
    def test_click_give_feedback_59(self, d):
        """
        点击意见反馈
        :param d:
        :return:
        """

        with pytest.allure.step("点击意见反馈"):
            action.click_element(d, "意见反馈")

        with pytest.allure.step("校验title"):
            test.assert_title(d, "建议与反馈")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Home')
    @pytest.allure.feature("60.app退出")
    @pytest.allure.severity('blocker')
    def test_sign_out_app_60(self, d):
        """
        退出app
        :param d:
        :return:
        """

        with pytest.allure.step("点击安全退出"):

            action.click_element(d, "安全退出")

        with pytest.allure.step("点击确认退出_是"):

            action.click_element(d, "确认退出_是")

        with pytest.allure.step("验证app已成功退出"):

            assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

        action.display_picture(d, "app退出")
        Consts.RESULT_LIST.append('True')











