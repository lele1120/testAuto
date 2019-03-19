#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import random
from os import path
from Params.params import get_value
from Common import Consts, Log
from Common import Operate
from Common import Consts
from Common import Assert
import time
import pytest


import sys

test = Assert.Assertions()
action = Operate.Operation()
logging = Log.MyLog()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
USER_ID = Operate.Operation().USER_ID


class TestRankingList:
    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("01.点击首页排行榜")
    @pytest.allure.severity('critical')
    def test_click_ranking_list_01(self, d):
        """
        点击首页排行榜
        :param d:
        """
        action.login_in(d)  # 登录
        time.sleep(5)
        with pytest.allure.step("点击首页排行榜按钮"):
            action.click_element(d, "排行榜按钮")
        with pytest.allure.step("切换验证"):
            test.assert_title(d, "货币基金")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第二项下划线"), "七日年化下划线显示")
            global prd_name
            prd_name = action.element_gettext(d, "货币基金产品名称")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("02.七日年化排行对比")
    @pytest.allure.severity('critical')
    def test_seven_day_anniversary_profit_02(self, d):
        """
        七日年化排行对比
        :param d:
        :return:
        """
        with pytest.allure.step("获取七日年化排行"):
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("03.点击万份收益")
    @pytest.allure.severity('critical')
    def test_click_ten_thousand_profit_03(self, d):
        """
        点击万份收益 验证排行是否正确
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜万年收益"):
            action.click_element(d, "排行榜万年收益")
        with pytest.allure.step("获取万份收益排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第一项下划线"), "万份收益下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("04.点击销量")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_04(self, d):
        """
        点击销量 验证销量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜销量"):
            action.click_element(d, "排行榜销量")
        with pytest.allure.step("获取销量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第三项下划线"), "销量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("05.点击关注量")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_05(self, d):
        """
        点击关注量 验证关注量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜关注量"):
            action.click_element(d, "排行榜关注量")
        with pytest.allure.step("获取关注量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第四项下划线"), "关注量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("06.货币基金页点击搜索")
    @pytest.allure.severity('critical')
    def test_click_search_06(self, d):
        """
        货币基金页搜索，标题对比
        :param d:
        :return:
        """
        with pytest.allure.step("点击右上角搜索"):
            action.click_element(d, "右上角搜索")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "货币基金")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("07.搜索货币基金产品")
    @pytest.allure.severity('critical')
    def test_search_monetary_fund_07(self, d):
        """
        搜索货币基金产品
        :param d:
        :return:
        """
        with pytest.allure.step("搜索输入产品查询"):
            action.input_element(d, "产品输入框", prd_name)
        with pytest.allure.step("点击搜索"):
            action.click_element(d, "搜索箭头")
        with pytest.allure.step("查询是否搜索结果正确"):
            time.sleep(2)
            # test.assert_equal_save_picture(d, prd_name, action.element_gettext(d, "货币基金产品名称"), "查询是否搜索结果正确")
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_"+str(i)).click()
                test.assert_equal_save_picture(d, prd_name, action.element_gettext(d, "货币基金产品名称"), "查询是否搜索结果正确")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("08.向右侧滑动切换理财产品标签")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_08(self, d):
        """
        向右侧滑动切换理财产品标签验证标题
        :param d:
        :return:
        """
        with pytest.allure.step("向右侧滑动切换理财产品标签"):
            d(scrollable=True).scroll.horiz.forward(steps=30)
        with pytest.allure.step("切换验证"):
            test.assert_title(d, "理财产品")
        Consts.RESULT_LIST.append('True')
        global prd_name_lc
        prd_name_lc = action.element_gettext(d, "理财产品产品名称")

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("09.预期年化收益对比")
    @pytest.allure.severity('critical')
    def test_annual_income_09(self, d):
        """
        预期年化收益对比，收益排行验证
        :param d:
        :return:
        """
        with pytest.allure.step("获取预期年化收益"):
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("10.点击理财期限")
    @pytest.allure.severity('critical')
    def test_click_financing_term_10(self, d):
        """
        点击理财期限，期限排行验证
        :param d:
        :return:
        """
        with pytest.allure.step("点击理财期限"):
            action.click_element(d, "排行榜万年收益")
        with pytest.allure.step("获取理财期限排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第一项下划线"), "万份收益下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list_no_reverse(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("11.点击销量")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_11(self, d):
        """
        点击排行榜销量，验证销量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜销量"):
            action.click_element(d, "排行榜销量")
        with pytest.allure.step("获取销量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第三项下划线"), "销量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("12.点击关注量")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_12(self, d):
        """
        点击关注量，验证关注量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜关注量"):
            action.click_element(d, "排行榜关注量")
        with pytest.allure.step("获取关注量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第四项下划线"), "关注量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("13.理财产品页点击搜索")
    @pytest.allure.severity('critical')
    def test_click_search_13(self, d):
        """
        理财产品页点击搜索标题对比哦
        :param d:
        :return:
        """
        with pytest.allure.step("点击右上角搜索"):
            action.click_element(d, "右上角搜索")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "理财产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("14.搜索理财产品")
    @pytest.allure.severity('critical')
    def test_search_financing_14(self, d):
        """
        搜索理财产品，验证搜索结果
        :param d:
        :return:
        """
        with pytest.allure.step("搜索输入产品查询"):
            action.input_element(d, "产品输入框", prd_name_lc)
        with pytest.allure.step("点击搜索页确定"):
            action.click_element(d, "搜索页确定")
        with pytest.allure.step("查询是否搜索结果正确"):
            time.sleep(2)
            # test.assert_equal_save_picture(d, prd_name, action.element_gettext(d, "货币基金产品名称"), "查询是否搜索结果正确")
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_"+str(i)).click()
                test.assert_equal_save_picture(d, prd_name_lc, action.element_gettext(d, "理财产品产品名称"), "查询是否搜索结果正确")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("15.向右侧滑动切换纯债基金标签")
    @pytest.allure.severity('critical')
    def test_change_pure_debt_15(self, d):
        """
        向右侧滑动切换纯债基金标签
        :param d:
        :return:
        """
        with pytest.allure.step("向右侧滑动切换纯债基金标签"):
            d(scrollable=True).scroll.horiz.forward(steps=30)
        with pytest.allure.step("切换验证"):
            test.assert_title(d, "纯债基金")
        Consts.RESULT_LIST.append('True')
        global prd_name_cz
        prd_name_cz = action.element_gettext(d, "纯债基金产品名称")

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("16.近三个月涨幅对比")
    @pytest.allure.severity('critical')
    def test_increases_in_three_months_16(self, d):
        """
        近三个月涨幅对比
        :param d:
        :return:
        """
        with pytest.allure.step("获取近三个月涨幅"):
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("17.点击累计净值")
    @pytest.allure.severity('critical')
    def test_click_cumulative_net_worth_17(self, d):
        """
        点击累计净值 净值对比
        :param d:
        :return:
        """
        with pytest.allure.step("点击累计净值"):
            action.click_element(d, "排行榜万年收益")
        with pytest.allure.step("获取累计净值排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第一项下划线"), "万份收益下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("18.点击销量")
    @pytest.allure.severity('critical')
    def test_click_sales_volume_18(self, d):
        """
        点击销量 销量对比
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜销量"):
            action.click_element(d, "排行榜销量")
        with pytest.allure.step("获取销量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第三项下划线"), "销量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("19.点击单位净值")
    @pytest.allure.severity('critical')
    def test_click_company_net_worth_19(self, d):
        """
        点击单位净值
        :param d:
        :return:
        """
        with pytest.allure.step("点击排行榜关注量"):
            action.click_element(d, "排行榜关注量")
        with pytest.allure.step("获取关注量排行"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "第四项下划线"), "关注量下划线显示")
            tv_temp = d(resourceId=get_value("排行榜数值"))
            test.assert_list(d, tv_temp)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("20.纯债基金页点击搜索")
    @pytest.allure.severity('critical')
    def test_click_search_20(self, d):
        """
        纯债基金页点击搜索
        :param d:
        :return:
        """
        with pytest.allure.step("点击右上角搜索"):
            action.click_element(d, "右上角搜索")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "纯债基金")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('ranking_list_page')
    @pytest.allure.feature("21.搜索纯债基金")
    @pytest.allure.severity('critical')
    def test_search_financing_21(self, d):
        """
        搜索纯债基金搜索产品
        :param d:
        :return:
        """
        with pytest.allure.step("搜索输入产品查询"):
            action.input_element(d, "产品输入框", prd_name_cz)
        with pytest.allure.step("点击搜索"):
            action.click_element(d, "搜索箭头")
        with pytest.allure.step("查询是否搜索结果正确"):
            time.sleep(2)
            # test.assert_equal_save_picture(d, prd_name, action.element_gettext(d, "货币基金产品名称"), "查询是否搜索结果正确")
            for i in range(0, 4):
                d(resourceId="com.bs.finance:id/tab_"+str(i)).click()
                test.assert_equal_save_picture(d, prd_name_cz, action.element_gettext(d, "纯债基金产品名称"), "查询是否搜索结果正确")
        Consts.RESULT_LIST.append('True')
        action.click_element(d, "返回icon")
        time.sleep(2)
        action.login_out(d)  # 登出


