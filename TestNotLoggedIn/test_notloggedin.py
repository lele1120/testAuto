#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
import time
import pytest
from os import path
from Params.params import get_value
from Common import Operate
from Common import Consts
from Common import Assert

import sys

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestNotLoginIn:
    @pytest.allure.feature('notloggedin')
    @pytest.allure.feature("01.启动app后进入比财")
    @pytest.allure.severity('critical')
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
            if d(resourceId=get_value("广告页")).exists:  # 如果弹出广告页

                action.click_element(d, "广告页关闭")  # 点击x关闭

        with pytest.allure.step("验证启动app点击进入比财是否进入首页"):
            test.assert_element_exists_save_picture(d, d(text="一键登录").exists, "验证是否有文本为一键登录的控件")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('notloggedin')
    @pytest.allure.feature("02.点击一键登录弹登录页")
    @pytest.allure.severity('critical')
    def test_click_login_02(self, d):
        """
        比财账号登录

        """

        with pytest.allure.step("点击app首页一键登录"):
            action.click_element(d, "首页一键登录")

        with pytest.allure.step("验证是否弹出登录页"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("立即登录按钮")).exists, "弹出登录页")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('notloggedin')
    @pytest.allure.feature("03.点击资产弹登录页")
    @pytest.allure.severity('critical')
    def test_click_assets_03(self, d):
        """
        点击资产弹登录页
        :param d:
        :return:
        """
        if d(resourceId=get_value("登录页关闭")).exists:
            with pytest.allure.step("数据回收关闭登录页"):
                action.click_element(d, "登录页关闭")

        with pytest.allure.step("点击资产"):
            action.click_element(d, "资产按钮")

        with pytest.allure.step("验证是否弹出登录页"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("立即登录按钮")).exists, "弹出登录页")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('notloggedin')
    @pytest.allure.feature("04.未登录购买产品弹登录页")
    @pytest.allure.severity('critical')
    def test_click_buy_product_04(self, d):
        """
        未登录购买产品弹登录页
        :param d:
        :return:
        """
        if d(resourceId=get_value("登录页关闭")).exists:
            with pytest.allure.step("数据回收关闭登录页"):
                action.click_element(d, "登录页关闭")

        with pytest.allure.step("点击首页推荐银行名称"):
            time.sleep(2)
            action.click_element(d, "首页银行名称")

        with pytest.allure.step("点击购买"):
            action.click_element(d, "安全购买")

        with pytest.allure.step("验证是否弹出登录页"):
            test.assert_title(d, "安全提醒")
            time.sleep(5)
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("立即登录按钮")).exists, "弹出登录页")

        Consts.RESULT_LIST.append('True')







