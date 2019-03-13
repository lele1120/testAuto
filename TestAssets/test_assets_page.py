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


class TestAssetsPage:
    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("01.首页资产按钮")
    @pytest.allure.severity('critical')
    def test_click_assets_page_01(self, d):
        """
        点击首页资产按钮
        :param d:
        """
        action.login_in(d)  # 登录
        with pytest.allure.step("点击首页银行按钮"):
            action.click_element(d, "首页资产按钮")
        with pytest.allure.step("标题判断是否跳转成功"):
            test.assert_title(d, "资产")
        with pytest.allure.step("获取资产视角"):
            global angle_of_view
            if action.element_exists(d, "资产页存款"):
                angle_of_view = 0  # 产品视角
            elif action.element_exists(d, "资产页银行显示"):
                angle_of_view = 1  # 银行视角

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("02.点击资产金额显示/隐藏")
    @pytest.allure.severity('critical')
    def test_click_money_see_or_hide_02(self, d):
        """
        点击金额显示隐藏
        :param d:
        :return:
        """
        with pytest.allure.step("获取金额显示隐藏状态"):
            global assets_type_see
            if action.element_gettext(d, "资产页金额") == "****":
                assets_type_see = 0
            else:
                assets_type_see = 1

        with pytest.allure.step("点击显示隐藏按钮"):
            if assets_type_see == 0:
                test.assert_equal_save_picture(d, action.element_gettext(d, "资产页昨日收益"), "****", "昨日收益金额显示")
                test.assert_equal_save_picture(d, action.element_gettext(d, "资产页累计收益"), "****", "累计收益金额显示")
            elif assets_type_see == 1:
                action.click_element(d, "资产页隐藏显示按钮")
                test.assert_equal_save_picture(d, action.element_gettext(d, "资产页昨日收益"), "****", "昨日收益金额显示")
                test.assert_equal_save_picture(d, action.element_gettext(d, "资产页累计收益"), "****", "累计收益金额显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("03.点击产页收益明细")
    @pytest.allure.severity('critical')
    def test_click_profit_detailed_03(self, d):
        with pytest.allure.step("点击资产页收益明细"):
            action.click_element(d, "资产页收益明细")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "收益明细")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("04.点击交易记录")
    @pytest.allure.severity('critical')
    def test_click_transaction_record_04(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击资产页交易记录"):
            action.click_element(d, "资产页交易记录")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "交易记录")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("05.点击右上角更多按钮")
    @pytest.allure.severity('critical')
    def test_click_more_05(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("资产页更多"):
            action.click_element(d, "资产页更多")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "切换视图"), "弹出下拉框")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("06.点击切换视图")
    @pytest.allure.severity('critical')
    def test_change_view_06(self, d):
        with pytest.allure.step("点击切换视图"):
            action.click_element(d, "切换视图")
            time.sleep(2)
        with pytest.allure.step("获取切换结果"):
            if angle_of_view == 0:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "资产页银行显示"), "视角切换")
            elif angle_of_view ==1:
                test.assert_element_exists_save_picture(d, action.element_exists(d, "资产页存款"),"视角切换")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("07.点击添加记账")
    @pytest.allure.severity('critical')
    def test_click_bookkeeping_07(self, d):
        with pytest.allure.step("点击右上角更多"):
            action.click_element(d, "资产页更多")
        with pytest.allure.step("点击添加记账"):
            action.click_element(d, "添加记账")
        with pytest.allure.step("点击百合银行"):
            if not d(resourceId="com.bs.finance:id/tv_name", text=u"百合直销银行").exists:
                d(text=u"B").click(timeout=10)
            d(resourceId="com.bs.finance:id/tv_name", text=u"百合直销银行").click(timeout=10)
        with pytest.allure.step("添加产品"):
            action.click_element(d, "银行内产品名称")
        with pytest.allure.step("输入存入金额"):
            action.input_element(d, "产品金额存入输入框", "1000")
        with pytest.allure.step("点击日期选择"):
            action.click_element(d, "产品日期选择")
        with pytest.allure.step("点击日期选择"):
            action.click_element(d, "日期选择确定")
            time.sleep(2)
        with pytest.allure.step("点击确认记账"):
            action.click_element(d, "确认记账")
        with pytest.allure.step("点击查看记账"):
            action.click_element(d, "查看记账")
        with pytest.allure.step("查看是否记账成功"):
            test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "1,000.00", "添加记账成功")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("08.点击返回icon")
    @pytest.allure.severity('critical')
    def test_click_return_08(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
            if assets_type_see == 0:
                action.click_element(d, "资产页隐藏显示按钮")
            time.sleep(2)
            if angle_of_view == 0:
                test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/tv_org_name", text=u"百合直销银行-隶属于兰州银行").exists, "添加记账")
                d(resourceId="com.bs.finance:id/tv_org_name", text=u"百合直销银行-隶属于兰州银行").click(timeout=10)
                with pytest.allure.step("查看是否记账成功"):

                    d(resourceId="com.bs.finance:id/tv_name").click(timeout=10)
                    test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "1,000.00", "添加记账")
            elif angle_of_view == 1:
                action.click_element(d, "资产页存款")
                time.sleep(1)
                action.click_element(d, "资产页智能存款")
                with pytest.allure.step("查看是否记账成功"):
                    test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "1,000.00", "添加记账")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("09.点击添加记账")
    @pytest.allure.severity('critical')
    def test_click_bookkeeping_manage_09(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击右上角更多"):
            action.click_element(d, "资产页更多")
        with pytest.allure.step("点击记账管理"):
            action.click_element(d, "记账管理")
        with pytest.allure.step("点击修改"):
            d(text=u"修改").click()
            time.sleep(2)
        with pytest.allure.step("输入修改金额"):
            action.input_element(d, "修改页面金额输入框", "2000")
        with pytest.allure.step("点击确认修改按钮"):
            action.click_element(d, "修改页面确认修改按钮")
        with pytest.allure.step("验证是否修改成功"):
            test.assert_equal_save_picture(d, action.element_gettext(d, "记账管理金额展示"), "￥2,000.00", "修改金额")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("10.修改记账金额")
    @pytest.allure.severity('critical')
    def test_modify_bookkeeping_10(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
            time.sleep(2)
            if angle_of_view == 0:
                test.assert_element_exists_save_picture(d, d(resourceId="com.bs.finance:id/tv_org_name", text=u"百合直销银行-隶属于兰州银行").exists, "添加记账")
                # d(resourceId="com.bs.finance:id/tv_org_name", text=u"百合直销银行-隶属于兰州银行").click()
                time.sleep(1)
                with pytest.allure.step("查看是否记账成功"):
                    action.click_element(d, "产品名称")
                    test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "2,000.00", "添加记账")
                    # test.assert_equal_save_picture(d, d(resourceId="com.bs.finance:id/tv_money", text=u"2,000.00",className="android.widget.TextView", instance=1).exists,"2,000.00", "添加记账")
            elif angle_of_view == 1:
                time.sleep(2)
                action.click_element(d, "资产页智能存款")
                with pytest.allure.step("查看是否记账成功"):
                    test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "2,000.00", "添加记账")
            Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("11.点击更多-修改")
    @pytest.allure.severity('critical')
    def test_click_more_and_more_modify_11(self, d):
        with pytest.allure.step("点击更多"):
            action.click_element(d, "智能存款页更多")
        with pytest.allure.step("点击修改"):
            action.click_element(d, "智能存款页修改")
        with pytest.allure.step("输入修改金额"):
            action.input_element(d, "修改页面金额输入框", "3000")
        with pytest.allure.step("点击确认修改按钮"):
            action.click_element(d, "修改页面确认修改按钮")
        with pytest.allure.step("验证是否修改成功"):
            test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "3,000.00", "添加记账")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("12.点击更多-删除后取消")
    @pytest.allure.severity('critical')
    def test_click_more_and_more_modify_qx_12(self, d):
        with pytest.allure.step("点击更多"):
            action.click_element(d, "智能存款页更多")
        with pytest.allure.step("点击修改"):
            action.click_element(d, "智能存款页删除")
        with pytest.allure.step("点击取消"):
            action.click_element(d, "删除弹框取消按钮")
        with pytest.allure.step("验证取消删除成功"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "手工记账标示"), "删除手工记账")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("13.点击更多-删除后确定")
    @pytest.allure.severity('critical')
    def test_click_more_and_more_modify_qd_13(self, d):
        with pytest.allure.step("点击更多"):
            action.click_element(d, "智能存款页更多")
        with pytest.allure.step("点击修改"):
            action.click_element(d, "智能存款页删除")
        with pytest.allure.step("点击确定"):
            action.click_element(d, "删除弹框确定按钮")
        with pytest.allure.step("验证取消删除成功"):
            test.assert_element_exists_save_picture(d, not action.element_exists(d, "手工记账标示"), "删除手工记账")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "缺省页文本"), "删除手工记账1")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("14.点击常见问题")
    @pytest.allure.severity('critical')
    def test_click_common_problem_14(self, d):
        with pytest.allure.step("点击常见问题"):
            action.click_element(d, "智能存款页常见问题")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "常见问题")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("15.点击更多内常见问题")
    @pytest.allure.severity('critical')
    def test_click_more_common_problem_15(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击右上角更多"):
            action.click_element(d, "资产页更多")
        with pytest.allure.step("点击右上角更多"):
            action.click_element(d, "更多内常见问题")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "常见问题")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('assets_page')
    @pytest.allure.feature("16.删除记账记录")
    @pytest.allure.severity('critical')
    def test_del_record_keeping_16(self, d):
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("添加记账数据"):
            with pytest.allure.step("点击资产更多"):
                action.click_element(d, "资产页更多")
            with pytest.allure.step("点击添加记账"):
                action.click_element(d, "添加记账")
            with pytest.allure.step("点击百合银行"):
                if not d(resourceId="com.bs.finance:id/tv_name", text=u"百合直销银行").exists:
                    d(text=u"B").click(timeout=10)
                d(resourceId="com.bs.finance:id/tv_name", text=u"百合直销银行").click(timeout=10)
            with pytest.allure.step("添加产品"):
                action.click_element(d, "银行内产品名称")
            with pytest.allure.step("输入存入金额"):
                action.input_element(d, "产品金额存入输入框", "1000")
            with pytest.allure.step("点击日期选择"):
                action.click_element(d, "产品日期选择")
            with pytest.allure.step("点击日期选择"):
                action.click_element(d, "日期选择确定")
                time.sleep(2)
            with pytest.allure.step("点击确认记账"):
                action.click_element(d, "确认记账")
            with pytest.allure.step("点击查看记账"):
                action.click_element(d, "查看记账")
            with pytest.allure.step("查看是否记账成功"):
                test.assert_equal_save_picture(d, action.element_gettext(d, "添加记账金额"), "1,000.00", "添加记账成功")
            with pytest.allure.step("点击返回icon"):
                action.click_element(d, "返回icon")
            with pytest.allure.step("点击资产更多"):
                action.click_element(d, "资产页更多")
            with pytest.allure.step("点击记账管理"):
                action.click_element(d, "记账管理")
            with pytest.allure.step("点击全选按钮"):
                action.click_element(d, "记账管理页全选按钮")
            with pytest.allure.step("点击删除按钮"):
                action.click_element(d, "记账管理页删除按钮")
            with pytest.allure.step("点击删除取消按钮"):
                action.click_element(d, "记账管理页删除取消按钮")
                test.assert_element_exists_save_picture(d,action.element_exists(d, "资产页银行名称"), "取消成功")
            with pytest.allure.step("点击删除按钮"):
                action.click_element(d, "记账管理页删除按钮")
            with pytest.allure.step("点击删除确定按钮"):
                action.click_element(d, "记账管理页删除确定按钮")
                test.assert_element_exists_save_picture(d, not action.element_exists(d, "资产页银行名称"), "删除成功")
                test.assert_element_exists_save_picture(d, action.element_exists(d, "缺省页文本"), "删除成功1")
            Consts.RESULT_LIST.append('True')
            with pytest.allure.step("点击返回icon"):
                action.click_element(d, "返回icon")
            with pytest.allure.step("点击比财按钮"):
                action.click_element(d, "首页比财按钮")
            with pytest.allure.step("验证返回成功"):
                test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
                action.login_out(d)  # 登出
