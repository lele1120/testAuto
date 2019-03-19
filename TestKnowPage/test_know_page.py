#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import
from os import path
from Params.params import get_value
from Common import Operate
from Common import Consts
from Common import Assert
import time
import pytest


import sys

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
USER_ID = Operate.Operation().USER_ID


class TestKnowPage:
    @pytest.allure.feature('know_page')
    @pytest.allure.feature("01.点击首页知道")
    @pytest.allure.severity('critical')
    def test_click_know_01(self, d):
        """
        点击首页知道
        :param d:
        """
        action.login_in(d)  # 登录
        with pytest.allure.step("点击首页知道"):
            action.click_element(d, "首页知道按钮")
        with pytest.allure.step("验证控件是否存在"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "数据知道"), "数据知道控件验证")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("02.点击抢爆款")
    @pytest.allure.severity('critical')
    def test_click_rush_to_explode_money_02(self, d):
        """
        点击抢爆款
        :param d:
        :return:
        """
        with pytest.allure.step("点击抢爆款"):
            d(resourceId="com.bs.finance:id/tv_item", text=u"抢爆款").click(timeout=10)
        with pytest.allure.step("标题对比"):
            time.sleep(2)
            test.assert_title(d, "数据分析优选")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("03.点击新手专享")
    @pytest.allure.severity('critical')
    def test_click_novices_exclusive_03(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新手专享"):
            action.click_element(d, "新手专享")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if not action.element_exists(d, "缺省页文本"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("04.点击爆款")
    @pytest.allure.severity('critical')
    def test_click_sell_well_04(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击爆款"):
            action.click_element(d, "爆款")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("05.点击新品")
    @pytest.allure.severity('critical')
    def test_click_new_products_05(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新品"):
            action.click_element(d, "新品")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("06.点击右上角查询")
    @pytest.allure.severity('critical')
    def test_click_btn_query_06(self, d):
        """
        点击右上角查询
        :param d:
        :return:
        """
        with pytest.allure.step("点击查询按钮"):
            action.click_element(d, "查询按钮")
        with pytest.allure.step("查询出产品"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "全部选项"), "全部选项")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("07.点击全部")
    @pytest.allure.severity('critical')
    def test_click_all_07(self, d):
        """
        点击右上角查询
        :param d:
        :return:
        """
        with pytest.allure.step("点击全部"):
            action.click_element(d, "全部选项")
        with pytest.allure.step("查询出产品"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("08.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_08(self, d):
        """
        点击返回icon
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("09.点击畅销专区")
    @pytest.allure.severity('critical')
    def test_click_best_seller_09(self, d):
        """
        点击畅销专区
        :param d:
        :return:
        """
        with pytest.allure.step("点击畅销专区"):
            d(resourceId="com.bs.finance:id/iv_item", description=u"比财", className="android.widget.ImageView",
              instance=1).click(timeout=10)
            time.sleep(2)
        test.assert_element_exists_save_picture(d, action.element_exists(d, "排行榜机构名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("10.点击货币基金下方四个选项")
    @pytest.allure.severity('critical')
    def test_click_fund_four_option_10(self, d):
        with pytest.allure.step("点击货币基金下方四个选项"):
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_"+str(i)).click(timeout=10)
                test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/line_"+str(i)).exists,
                                                        "验证下划线切换")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("11.右滑动")
    @pytest.allure.severity('critical')
    def test_right_slide_11(self, d):

        with pytest.allure.step("右滑动"):
            d(scrollable=True).scroll.horiz.forward(steps=30)
        with pytest.allure.step(""):
            test.assert_title(d, "理财产品")
            Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("12.点击理财产品下方四个选项")
    @pytest.allure.severity('critical')
    def test_click_financing_four_option_12(self, d):
        with pytest.allure.step("点击理财产品下方四个选项"):
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_"+str(i)).click(timeout=10)
                test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/line_"+str(i)).exists,
                                                        "验证下划线切换")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("13.再次右滑动")
    @pytest.allure.severity('critical')
    def test_right_slider_again_13(self, d):
        with pytest.allure.step("右滑动"):
            d(scrollable=True).scroll.horiz.forward(steps=30)
        with pytest.allure.step(""):
            test.assert_title(d, "纯债基金")
            Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("14.点击纯债基金下方四个选项")
    @pytest.allure.severity('critical')
    def test_click_debt_four_option_14(self, d):
        with pytest.allure.step("点击纯债基金下方四个选项"):
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_" + str(i)).click(timeout=10)
                test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/line_" + str(i)).exists,
                                                        "验证下划线切换")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("15.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_15(self, d):
        """
        点击返回icon
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
            time.sleep(3)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("16.点击新手专享")
    @pytest.allure.severity('critical')
    def test_click_novice_vip_16(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新手专享"):
            d(resourceId="com.bs.finance:id/tv_item", text=u"新手专享").click(timeout=10)
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "数据分析优选")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("17.点击新手专享")
    @pytest.allure.severity('critical')
    def test_click_novices_exclusive_17(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新手专享"):
            action.click_element(d, "新手专享")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if not action.element_exists(d, "缺省页文本"):
                test.assert_element_exists_save_picture(d,action.element_exists(d,"新手专项产品名称"),"查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("18.点击爆款")
    @pytest.allure.severity('critical')
    def test_click_sell_well_18(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击爆款"):
            action.click_element(d, "爆款")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("19.点击新品")
    @pytest.allure.severity('critical')
    def test_click_new_products_19(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新品"):
            action.click_element(d, "新品")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("20.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_20(self, d):
        """
        点击返回icon
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("21.点击新品上架")
    @pytest.allure.severity('critical')
    def test_click_new_arrivals_21(self, d):
        """
        点击抢爆款
        :param d:
        :return:
        """
        with pytest.allure.step("点击抢爆款"):
            d(resourceId="com.bs.finance:id/tv_item", text=u"新品上架").click(timeout=10)
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "数据分析优选")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("22.点击新手专享")
    @pytest.allure.severity('critical')
    def test_click_novices_exclusive_22(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新手专享"):
            action.click_element(d, "新手专享")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if not action.element_exists(d, "缺省页文本"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("23.点击爆款")
    @pytest.allure.severity('critical')
    def test_click_sell_well_23(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击爆款"):
            action.click_element(d, "爆款")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("24.点击新品")
    @pytest.allure.severity('critical')
    def test_click_new_products_24(self, d):
        """
        点击新手专享
        :param d:
        :return:
        """
        with pytest.allure.step("点击新品"):
            action.click_element(d, "新品")
        with pytest.allure.step("查询出产品"):
            time.sleep(5)
            if action.element_exists(d, "无数据"):
                test.assert_element_exists_save_picture(d, action.element_exists(d, "无数据"), "该产品无数据")
            else:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "新手专项产品名称"), "查询出产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("25.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_25(self, d):
        """
        点击返回icon
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("26.点击更多")
    @pytest.allure.severity('critical')
    def test_click_more_and_more_26(self, d):
        """
        点击更多
        :param d:
        :return:
        """
        with pytest.allure.step("点击更多"):
            action.click_element(d, "数据知道页更多")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "比财知道")
        for i in range(0, 4):
            d(resourceId="com.bs.finance:id/tab_" + str(i)).click(timeout=10)
            time.sleep(1)
            test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/line_" + str(i)).exists,
                                                    "验证下划线切换")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('know_page')
    @pytest.allure.feature("27.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_27(self, d):
        """
        点击返回icon
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')
        action.click_element(d, "导航栏比财按钮")
        action.login_out(d)  # 登出









