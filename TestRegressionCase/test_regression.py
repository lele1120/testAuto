#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import time
import pytest
from os import path
from Params.params import get_value

from Params.params import get_driver_by_key
from Common import Operate
from Common import Consts
from Common import Assert

import sys

from TestCase.conftest import action_env

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


@pytest.fixture(scope='module')
def d():
    running_environment = action_env()
    d = get_driver_by_key(running_environment)  # 输入参数启动
    # d.unlock()
    d.set_fastinput_ime(True)  # 开启快速输入
    d.session("com.bs.finance")
    yield d
    d.app_stop("com.bs.finance")


class TestRegression:
    @pytest.allure.feature('Regression')
    @pytest.allure.feature("01.启动app后进入比财")
    @pytest.allure.severity('critical')
    def test_go_main_01(self, d):
        """
        首次启动app点击进入比财,如果有广告页点击x关闭，
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')

        time.sleep(5)

        with pytest.allure.step("启动页点击进入比财"):

            action.click_element(d, "启动页进入比财")

        with pytest.allure.step("如果弹出广告页点x关闭"):
            if d(resourceId=get_value("广告页")).exists:  # 如果弹出广告页

                action.click_element(d, "广告页关闭")  # 点击x关闭

        with pytest.allure.step("验证启动app点击进入比财是否进入首页"):

            test.assert_element_exists_save_picture(d, d(text="一键登录").exists, "验证是否有文本为一键登录的控件")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("02.比财登录")
    @pytest.allure.severity('critical')
    def test_login_02(self, d):
        """
        比财账号登录

        """
        Consts.TEST_LIST.append('Test')

        global USER_ID   # 使用账号

        USER_ID = str(get_value("xc测试机手机号"))

        picture_verification_code = str(get_value("四位图片验证码"))

        login_verification_code = str(get_value("登录验证码"))

        with pytest.allure.step("点击app首页一键登录"):
            action.click_element(d, "首页一键登录")

        with pytest.allure.step("在登录页账号输入框输入账号"):
            action.input_element(d, "登录页账号输入框", USER_ID)

        with pytest.allure.step("点击获取验证码"):
            action.click_element(d, "登录页获取验证码按钮")  # 点击获取验证码

        #  如果弹出4位数字图片验证码
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

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("03.弹出侧边栏")
    @pytest.allure.severity('critical')
    def test_sidebar_eject_03(self, d):
        """
         验证点击左上角图标弹出侧边栏功能
        """

        Consts.TEST_LIST.append('Test')

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

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("04.点击我的钱包")
    @pytest.allure.severity('critical')
    def test_click_bicai_wallet_04(self, d):
        """
        点击我的钱包跳转
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        global remaining_sum_type  # 首次点击进入账户余额显示/隐藏状态记录
        global change_remaining_sum_type  # 再次进入账户余额显示/隐藏状态记录
        with pytest.allure.step("点击我的钱包"):
            action.click_element_with_text(d, "我的钱包", "我的钱包")
            test.assert_title(d, "我的钱包")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("05.点击II类户跳转")
    @pytest.allure.severity('critical')
    def test_click_type_two_accounts_05(self, d):
        """
        点击二类户跳转
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        with pytest.allure.step("点击II类户（图片）跳转"):
            d(description=u"A37H3tXWoJVwAAAAAASUVORK5CYII=").click()
            time.sleep(1)

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "II类户")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("06.点击立即开户")
    @pytest.allure.severity('blocker')
    def test_click_fast_open_account_06(self, d):
        """
        点击二类户立即开户跳转实名认证页
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        with pytest.allure.step("点击II类户立即开户"):
            action.click_element(d, "立即开户")

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "实名认证")

        with pytest.allure.step("校验实名认证页内容"):
            real_name_tips = d(resourceId=get_value("实名认证提示2")).get_text()
            test.assert_equal_save_picture(d, real_name_tips, "购买理财需实名认证", "验证提示文本")

        with pytest.allure.step("校验去实名认证控件是否存在"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("去实名认证")).exists, "验证去实名认证控件存在")
            Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("07.点击去实名认证")
    @pytest.allure.severity('blocker')
    def test_click_go_real_name_07(self, d):
        """
        点击去实名认证
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        with pytest.allure.step("点击去实名认证"):
            action.click_element(d, "去实名认证")

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "身份证认证")

        action.display_picture(d, "用户未实名")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("08.点击设置")
    @pytest.allure.severity('Block')
    def test_click_set_up_08(self, d):
        """
        点击设置
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        with pytest.allure.step("点击设置"):

            time.sleep(5)

            action.click_element(d, "侧边栏设置")

        with pytest.allure.step("title校验"):
            test.assert_title(d, "设置")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('Regression')
    @pytest.allure.feature("09.app退出")
    @pytest.allure.severity('critical')
    def test_sign_out_app_09(self, d):
        """
        退出app
        :param d:
        :return:
        """
        Consts.TEST_LIST.append('Test')
        with pytest.allure.step("点击安全退出"):

            action.click_element(d, "安全退出")

        with pytest.allure.step("点击确认退出_是"):

            action.click_element(d, "确认退出_是")

        with pytest.allure.step("验证app已成功退出"):

            assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

        action.display_picture(d, "app退出")
        Consts.RESULT_LIST.append('True')











