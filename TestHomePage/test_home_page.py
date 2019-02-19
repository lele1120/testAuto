#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re
import time
import pytest
from os import path
from Params.params import get_value,change_param_for_json
from Common import Operate
from Common import Consts
from Common import Assert


import sys

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
USER_ID = Operate.Operation().USER_ID


class TestRegression:
    @pytest.allure.feature('homepage')
    @pytest.allure.feature("01.点击首页搜索")
    @pytest.allure.severity('critical')
    def test_click_search_01(self, d):
        """
        点击首页搜索框
        :param d:
        """
        action.login_in(d)  # 登录
        time.sleep(10)
        with pytest.allure.step("点击首页搜索"):
            action.click_element(d, "首页搜索")
        with pytest.allure.step("验证是否跳转成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("搜索按钮")).exists, "跳转搜索页搜索按钮显示")
            type_choose_text = d(resourceId=get_value("选择搜索类型")).get_text()
            if type_choose_text == "机构":
                test.assert_equal_save_picture(d, d(resourceId=get_value("搜索文本框")).get_text(), "搜索相关金融机构", "搜索框文本显示")
            elif type_choose_text == "产品":
                test.assert_equal_save_picture(d, d(resourceId=get_value("搜索文本框")).get_text(), "搜索相关金融产品", "搜索框文本显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("02.点击搜索")
    @pytest.allure.severity('critical')
    def test_click_search_button_02(self, d):
        """
        点击搜索页搜索按钮
        :param d:
        """
        type_choose_text = d(resourceId=get_value("选择搜索类型")).get_text()

        with pytest.allure.step("点击首页搜索"):
            action.click_element(d, "搜索按钮")

        if type_choose_text == "机构":
            test.assert_equal_save_picture(d, d(resourceId=get_value("类型展示")).get_text(), "金融机构", "跳转成功")
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("搜索页展示名称")).exists, "搜索出金融机构")
        elif type_choose_text == "产品":
            test.assert_equal_save_picture(d, d(resourceId=get_value("类型展示")).get_text(), "金融产品", "跳转成功")
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("搜索页展示名称")).exists, "搜索出金融产品")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("03.切换搜索类型")
    @pytest.allure.severity('critical')
    def test_choose_search_type_03(self, d):
        """
        切换搜索类型
        :param d:
        """
        type_choose_text = d(resourceId=get_value("选择搜索类型")).get_text()

        with pytest.allure.step("点击首页搜索"):
            action.click_element(d, "搜索页类型选择")

        with pytest.allure.step("验证弹出类型选择下拉框"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("机构选项")).exists, "类型选择下拉框")

        with pytest.allure.step("切换类型选择"):
            if type_choose_text == "机构":
                action.click_element(d, "产品选项")
                test.assert_equal_save_picture(d, d(resourceId=get_value("选择搜索类型")).get_text(), "产品", "类型切换")
                test.assert_equal_save_picture(d, d(resourceId=get_value("搜索文本框")).get_text(), "搜索相关金融产品", "搜索框文本显示")
            elif type_choose_text == "产品":
                action.click_element(d, "机构选项")
                test.assert_equal_save_picture(d, d(resourceId=get_value("选择搜索类型")).get_text(), "机构", "类型切换")
                test.assert_equal_save_picture(d, d(resourceId=get_value("搜索文本框")).get_text(), "搜索相关金融机构", "搜索框文本显示")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("04.切换类型后点击搜索")
    @pytest.allure.severity('critical')
    def test_switch_click_search_button_04(self, d):
        """
        点击搜索页搜索按钮
        :param d:
        """
        type_choose_text = d(resourceId=get_value("选择搜索类型")).get_text()

        with pytest.allure.step("点击首页搜索"):
            action.click_element(d, "搜索按钮")

        if type_choose_text == "机构":
            test.assert_equal_save_picture(d, d(resourceId=get_value("类型展示")).get_text(), "金融机构", "跳转成功")
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("搜索页展示名称")).exists, "搜索出金融机构")
        elif type_choose_text == "产品":
            test.assert_equal_save_picture(d, d(resourceId=get_value("类型展示")).get_text(), "金融产品", "跳转成功")
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("搜索页展示名称")).exists, "搜索出金融产品")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("05.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_05(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("返回首页"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("06.点击昨日收益")
    @pytest.allure.severity('critical')
    def test_click_home_page_06(self, d):
        """
        点击昨日收益
        :param d:
        :return:
        """
        with pytest.allure.step("点击首页昨日收益"):
            action.click_element(d, "首页昨日收益")
        with pytest.allure.step("验证是否跳转成功"):
            test.assert_title(d, "资产")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("07.点击比财")
    @pytest.allure.severity('critical')
    def test_click_bicai_07(self, d):
        """
        点击昨日收益
        :param d:
        :return:
        """
        with pytest.allure.step("点击导航栏比财"):
            action.click_element(d, "导航栏比财按钮")
        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("08.点击排行榜")
    @pytest.allure.severity('critical')
    def test_click_rankin_list_08(self, d):
        """
        点击排行榜
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜"):
            action.click_element(d, "排行榜按钮")

        with pytest.allure.step("验证跳转成功"):
            test.assert_title(d, "货币基金")
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("排行榜机构名称")).exists, "排行榜机构名称")

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("09.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_09(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("返回首页"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("10.点击活动入口按钮")
    @pytest.allure.severity('critical')
    def test_click_activity_10(self, d):
        """
        点击排行榜
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜"):
            action.click_element(d, "拼团活动入口")

        with pytest.allure.step("验证跳转成功"):
            test.assert_title(d, "拼团阖家欢")
            time.sleep(5)
            test.assert_element_exists_save_picture(d, d(description=u"活动规则").exists, "活动规则按钮")
            test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "往期拼团按钮")
            test.assert_element_exists_save_picture(d, d(description=u"拼团", className="android.view.View", instance=1).exists, "拼团按钮")
            test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "活动投资按钮")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("11.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_11(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("返回首页"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("12.点击首页banner")
    @pytest.allure.severity('critical')
    def test_click_banner_12(self, d):
        """
        点击排行榜
        :param d:
        :return:
        """
        with pytest.allure.step("点击首页banner"):
            action.click_element(d, "首页banner")

        with pytest.allure.step("验证跳转成功"):
            test.assert_title(d, "拼团阖家欢")
            time.sleep(5)
            test.assert_element_exists_save_picture(d, d(description=u"活动规则").exists, "活动规则按钮")
            test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "往期拼团按钮")
            test.assert_element_exists_save_picture(d, d(description=u"拼团", className="android.view.View", instance=1).exists, "拼团按钮")
            test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "活动投资按钮")
        Consts.RESULT_LIST.append('True')

        action.login_out(d) #登出






