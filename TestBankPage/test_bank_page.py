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


class TestBankPage:
    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("01.首页银行按钮")
    @pytest.allure.severity('critical')
    def test_click_bank_page_01(self, d):
        """
        点击首页银行按钮
        :param d:
        """
        action.login_in(d)  # 登录
        with pytest.allure.step("点击首页银行按钮"):
            action.click_element(d, "首页银行按钮")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "收藏银行"), "收藏银行显示")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "全部银行"), "全部银行显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("02.全部银行页点击银行跳转")
    @pytest.allure.severity('critical')
    def test_click_all_bank_02(self, d):
        """
        点击全部银行
        :param d:
        """

        with pytest.allure.step("点击全部银行按钮"):
            action.click_element(d, "全部银行")
            d(scrollable=True).scroll(steps=10)  # 向下滑动
            time.sleep(2)
            d(scrollable=True).scroll(steps=20)  # 向下滑动
            time.sleep(2)
            bank_name_list = d(resourceId=get_value("产品名称"))
            print(bank_name_list)
            i_bank = random.randint(0+1, bank_name_list.__len__()-1)
            global i_bank_name
            i_bank_name = bank_name_list[i_bank].get_text()
            print(i_bank_name)

        with pytest.allure.step("点击" + i_bank_name + "跳转"):
            try:
                d(resourceId=get_value("产品名称"))[i_bank].click(timeout=10)
            except:
                action.display_picture(d, "控件未获取到")
                logging.error("点击银行名称失败 ")
                raise
            global s_bank_name
            s_bank_name = d(resourceId=get_value("收藏页银行名称")).get_text()
            test.assert_title(d, "银行")
            test.assert_equal_save_picture(d, i_bank_name, s_bank_name, "银行名称对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("03.收藏银行")
    @pytest.allure.severity('critical')
    def test_click_all_bank_03(self, d):
        with pytest.allure.step("点击" + i_bank_name + "跳转"):
            sc_text = d(resourceId=get_value("收藏按钮")).get_text()
            action.click_element(d, "收藏按钮")
            click_sc_text = d(resourceId=get_value("收藏按钮")).get_text()
            test.assert_equal_save_picture(d, sc_text, "+收藏", "未点击收藏按钮显示")
            test.assert_equal_save_picture(d, click_sc_text, "已收藏", "未点击收藏按钮显示")

        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("04.查看已收藏银行")
    @pytest.allure.severity('critical')
    def test_look_collection_bank_04(self, d):
        with pytest.allure.step("点击收藏银行"):
            action.click_element(d, "收藏银行")
        with pytest.allure.step("对比收藏银行是否在收藏页展示"):
            sc_bank_name = action.element_gettext(d, "收藏页银行名称")
            test.assert_equal_save_picture(d, s_bank_name,sc_bank_name,"收藏页银行名称对比")
        with pytest.allure.step("点击" + i_bank_name + "跳转"):
            pass
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("05.查看已收藏银行")
    @pytest.allure.severity('critical')
    def test_click_scbank_name_05(self, d):
        with pytest.allure.step("点击收藏银行"):
            action.click_element(d, "收藏页银行名称")
        with pytest.allure.step("点击收藏银行"):
            scy_bank_name = action.element_gettext(d, "收藏页银行名称")
            test.assert_equal_save_picture(d, s_bank_name, scy_bank_name, "收藏页银行名称对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("06.取消收藏银行")
    @pytest.allure.severity('critical')
    def test_cancel_bank_collection_06(self, d):
        with pytest.allure.step("点击取消收藏"):
            sc_text = d(resourceId=get_value("收藏按钮")).get_text()
            action.click_element(d, "收藏按钮")
            click_sc_text = d(resourceId=get_value("收藏按钮")).get_text()
            test.assert_equal_save_picture(d, sc_text, "已收藏", "未点击收藏按钮显示")
            test.assert_equal_save_picture(d, click_sc_text, "+收藏", "未点击收藏按钮显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("07.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_07(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("验证是否返回成功"):
            test.assert_element_exists_save_picture(d, "收藏银行", "收藏银行按钮显示")
            test.assert_element_exists_save_picture(d, "全部银行", "全部银行按钮显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("08.全部银行页点击m搜索梅州客商银行")
    @pytest.allure.severity('critical')
    def test_click_ks_bank_08(self, d):
        """
        点击全部银行
        :param d:
        """
        with pytest.allure.step("点击全部银行按钮"):
            action.click_element(d, "全部银行")
        with pytest.allure.step("点击右侧m搜索"):
            d(text=u"M").click()
        with pytest.allure.step("点击梅州客商银行"):
            d(resourceId="com.bs.finance:id/tv_name", text=u"梅州客商银行").click()
        with pytest.allure.step("验证银行名称标题跳转"):
            test.assert_title(d, "银行")
        Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("09.点击周周利1号产品")
    # @pytest.allure.severity('critical')
    # def test_click_zzl1_product_09(self, d):
    #     with pytest.allure.step("点击周周利1号产品"):
    #         d(resourceId="com.bs.finance:id/tv_name", text=u"周周利1号").click()
    #     with pytest.allure.step("验证产品标题跳转"):
    #         test.assert_title(d, "周周利1号")
    #     with pytest.allure.step("验证产品展示内容"):
    #         product_details = ["4.1250%", "28天-3年", "1,000.00元", "1.00元", "锁定期后随时支取", "定期存款", "28天"]
    #         product_details_real = [action.element_gettext(d, "产品页利率"),
    #                                 action.element_gettext(d, "产品页期限"),
    #                                 action.element_gettext(d, "产品页起存金额"),
    #                                 action.element_gettext(d, "产品页递增金额"),
    #                                 action.element_gettext(d, "产品页支取时间"),
    #                                 action.element_gettext(d, "产品页产品类型"),
    #                                 action.element_gettext(d, "产品页锁定期")]
    #     for i in range(product_details.__len__()):
    #         test.assert_equal_save_picture(d, product_details[i], product_details_real[i], product_details[i]+"对比" + product_details_real[i])
    #
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("10.点击保护条款")
    # @pytest.allure.severity('critical')
    # def test_click_protection_lause_10(self, d):
    #     with pytest.allure.step("点击受保护条款"):
    #         d(text=u"受存款保险保护 >").click()
    #     with pytest.allure.step("验证是否弹出"):
    #         time.sleep(5)
    #         test.assert_element_exists_save_picture(d, action.element_exists(d, "关闭按钮"), "验证保护条款是否展示")
    #     with pytest.allure.step("点击关闭"):
    #         action.click_element(d, "关闭按钮")
    #     with pytest.allure.step("验证产品标题跳转"):
    #         test.assert_title(d, "周周利1号")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("11.点击活动入口")
    # @pytest.allure.severity('critical')
    # def test_click_actity_button_11(self, d):
    #     with pytest.allure.step("活动按钮"):
    #         action.click_element(d, "产品活动入口")
    #         time.sleep(5)
    #     with pytest.allure.step("验证跳转成功"):
    #         test.assert_title(d, "拼团")
    #         time.sleep(5)
    #         test.assert_element_exists_save_picture(d, d(description=u"活动规则").exists, "活动规则按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "往期拼团按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"拼团", className="android.view.View", instance=1).exists, "拼团按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "活动投资按钮")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("12.返回产品页")
    # @pytest.allure.severity('critical')
    # def test_return_home_page_12(self, d):
    #     """
    #     返回产品页
    #     :param d:
    #     """
    #     with pytest.allure.step("返回首页"):
    #         action.click_element(d, "返回icon")
    #
    #     with pytest.allure.step("验证返回成功"):
    #         test.assert_title(d, "周周利1号")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("13.点击计算器")
    # @pytest.allure.severity('critical')
    # def test_click_calculator_13(self, d):
    #     """
    #     点击计算器
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("点击计算器"):
    #         action.click_element(d, "计算器按钮")
    #
    #     with pytest.allure.step("计算器内容对比"):
    #         global calculator_details
    #         calculator_details = ["10000", "3年", "1,254.68", "106.45"]
    #         calculator_details_real = [action.element_gettext(d, "计算器买入金额"),
    #                                    action.element_gettext(d, "计算器期限"),
    #                                    action.element_gettext(d, "计算器本产品收益"),
    #                                    action.element_gettext(d, "计算器银行定期收益")]
    #     with pytest.allure.step("计算器内容对比"):
    #         for i in range(calculator_details.__len__()):
    #             test.assert_equal_save_picture(d, calculator_details[i], calculator_details_real[i], calculator_details[i]+"对比" + calculator_details_real[i])
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("14.点击按此金额购买")
    # @pytest.allure.severity('critical')
    # def test_click_this_money_14(self, d):
    #     """
    #     点击计算器
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("按此金额购买"):
    #         action.click_element(d, "按此金额购买")
    #         time.sleep(5)
    #     with pytest.allure.step("进入存入页标题对比"):
    #         test.assert_title(d, "存入")
    #     with pytest.allure.step("金额对比"):
    #         test.assert_equal_save_picture(d,calculator_details[0],action.element_gettext(d, "存入页输入框金额"), "存入页金额对比")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("15.返回产品页")
    # @pytest.allure.severity('critical')
    # def test_return_home_page_15(self, d):
    #     """
    #     返回产品页
    #     :param d:
    #     """
    #     with pytest.allure.step("返回首页"):
    #         action.click_element(d, "返回icon")
    #
    #     with pytest.allure.step("验证返回成功"):
    #         test.assert_title(d, "周周利1号")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("16.点击安全购买")
    # @pytest.allure.severity('critical')
    # def test_click_safe_buy_16(self, d):
    #     """
    #     点击安全购买
    #     :param d:
    #     """
    #     with pytest.allure.step("点击安全购买"):
    #         action.click_element(d, "安全购买")
    #     with pytest.allure.step("标题对比"):
    #         test.assert_title(d, "存入")
    #     with pytest.allure.step("验证产品展示内容"):
    #         product_details = ["周周利1号", "起购金额1000.00元", "定期存款", "最小递增1.00元", "《产品服务协议》"]
    #         product_details_real = [action.element_gettext(d, "存入页产品名称"),
    #                                 action.element_gettext(d, "存入页起购金额"),
    #                                 action.element_gettext(d, "存入页产品类型"),
    #                                 action.element_gettext(d, "存入页最小递增金额"),
    #                                 action.element_gettext(d, "存入页协议名称")]
    #     for i in range(product_details.__len__()):
    #         test.assert_equal_save_picture(d, product_details[i], product_details_real[i],
    #                                        product_details[i]+"对比" + product_details_real[i])
    #
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("17.点击协议")
    # @pytest.allure.severity('critical')
    # def test_click_agreement_17(self, d):
    #     with pytest.allure.step("点击协议"):
    #         action.click_element(d, "存入页协议名称")
    #     with pytest.allure.step("标题对比"):
    #         test.assert_title(d, "产品服务协议")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("18.返回存入页")
    # @pytest.allure.severity('critical')
    # def test_return_home_page_18(self, d):
    #     """
    #     返回产品页
    #     :param d:
    #     """
    #     with pytest.allure.step("返回首页"):
    #         action.click_element(d, "返回icon")
    #     with pytest.allure.step("标题对比"):
    #         test.assert_title(d, "存入")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("19.点击充值")
    # @pytest.allure.severity('critical')
    # def test_click_recharge_19(self, d):
    #     """
    #     点击充值
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("点击充值"):
    #         action.click_element(d, "存入页充值按钮")
    #     with pytest.allure.step("标题对比"):
    #         test.assert_title(d, "充值")
    #     Consts.RESULT_LIST.append('True')
    #
    # @pytest.allure.feature('bank_page1')
    # @pytest.allure.feature("20.点击更多银行卡")
    # @pytest.allure.severity('critical')
    # def test_more_bank_card_20(self, d):
    #     """
    #     点击更多银行卡
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("点击选择银行卡"):
    #         action.click_element(d, "存入页选择银行卡")
    #     with pytest.allure.step("点击充值页关闭按钮"):
    #         test.assert_element_exists_save_picture(d, "充值页关闭按钮", "验证充值页关闭")
    #     Consts.RESULT_LIST.append('True')
    #
    # @pytest.allure.feature('bank_page')
    # @pytest.allure.feature("21.点击农业银行卡")
    # @pytest.allure.severity('critical')
    # def test_click_agricultural_bank_21(self, d):
    #     """
    #     点击农业银行
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("选择农业银行银行卡"):
    #         d(resourceId="com.bs.finance:id/tv_bank_name", text=u"农业银行(8272)").click()
    #     with pytest.allure.step("校验银行是否切换成功"):
    #         test.assert_equal_save_picture(d, action.element_gettext(d, "充值页银行卡名称"), "农业银行", "切换为农业银行")
    #     with pytest.allure.step("每日限额校验"):
    #         test.assert_equal_save_picture(d, action.element_gettext(d, "充值页每日限额").strip(), "每日限额:  10,000.00元", "每日限额校验")
    #     with pytest.allure.step("单笔限额校验"):
    #         test.assert_equal_save_picture(d, action.element_gettext(d, "充值页单笔限额").strip(), "单笔限额:  2,000.00元", "单笔限额校验")
    #     Consts.RESULT_LIST.append('True')
    #
    # @pytest.allure.feature('bank_page')
    # @pytest.allure.feature("22.返回银行页")
    # @pytest.allure.severity('critical')
    # def test_return_home_bank_page_22(self, d):
    #     """
    #     返回客商银行页
    #     :param d:
    #     """
    #
    #     with pytest.allure.step("返回银行页"):
    #         for i in range(5):
    #             if action.element_gettext(d, "标题") == "银行":
    #                 break
    #             else:
    #                 action.click_element(d, "返回icon")
    #
    #     with pytest.allure.step("验证返回成功"):
    #         test.assert_title(d, "银行")
    #     Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("23.点击查看资产")
    @pytest.allure.severity('critical')
    def test_click_look_assets_23(self, d):
        """
        点击查看资产
        :param d:
        :return:
        """
        with pytest.allure.step("点击查看资产"):
            action.click_element(d, "查看资产")
        with pytest.allure.step("梅州客商银行"):
            test.assert_title(d, "梅州客商银行")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("24.隐藏显示页金额")
    @pytest.allure.severity('critical')
    def test_open_or_see_24(self, d):
        """
        获取隐藏显示金额状态，切换状态
        :param d:
        :return:
        """
        with pytest.allure.step("获取显示状态1为显示0为隐藏"):
            global type_see
            global type_see_click
            if action.element_gettext(d, "资产页总资产") == "*****":
                type_see = 0
            else:
                type_see = 1
        with pytest.allure.step("点击显示/隐藏按钮"):
            action.click_element(d, "资产页金额隐藏显示")
            if action.element_gettext(d, "资产页总资产") == "*****":
                type_see_click = 0
            else:
                type_see_click = 1

        test.assert_equal_save_picture(d, type_see, not type_see_click, "金额隐藏切换")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("25.隐藏显示页金额")
    @pytest.allure.severity('critical')
    def test_return_open_or_see_25(self, d):
        """
        点击返回icon后再进入查看金额显示隐藏状态
        :param self:
        :param d:
        :return:
        """
        with pytest.allure.step("点击返回icon"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击查看资产"):
            action.click_element(d, "查看资产")
            if action.element_gettext(d, "资产页总资产") == "*****":
                type_see_return = 0
            else:
                type_see_return = 1

        test.assert_equal_save_picture(d, type_see_return, type_see_click, "金额隐藏切换与点击前对比")
        test.assert_equal_save_picture(d, type_see, not type_see_return, "金额隐藏切换与点击后对比")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("26.点击余额明细")
    @pytest.allure.severity('critical')
    def test_cilck_balance_detailed_26(self, d):
        """
        点击余额明细
        :param d:
        :return:
        """
        with pytest.allure.step("点击资产页余额明细"):
            action.click_element(d, "资产页余额明细")
        with pytest.allure.step("标题对比"):
            test.assert_element_exists_save_picture(d, d(text=u"可用余额").exists, "可用余额标题显示")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("27.点击充值")
    @pytest.allure.severity('critical')
    def test_cilck_recharge_27(self, d):
        """
        点击可用余额页充值跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击充值跳转"):
            action.click_element(d, "可用余额页充值")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "充值")
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("28.点击提现")
    @pytest.allure.severity('critical')
    def test_click_withdraw_cash_28(self, d):
        """
        点击可用余额页充值跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击充值跳转"):
            action.click_element(d, "可用余额页提现")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "提现")
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("29.点击明细查询")
    @pytest.allure.severity('critical')
    def test_click_detailed_query_29(self, d):
        """
        点击可用余额页充值跳转
        :param d:
        :return:
        """
        with pytest.allure.step("点击充值跳转"):
            action.click_element(d, "可用余额页明细查询")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "交易明细")
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "可用余额页返回")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("30.点击存款产品明细页")
    @pytest.allure.severity('critical')
    def test_click_deposit_product_query_30(self, d):
        """
        点击存款产品明细页
        :param d:
        :return:
        """
        with pytest.allure.step("点击存款产品明细"):
            action.click_element(d, "资产页存款产品明细查询")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "存款产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("31.点击已支取")
    @pytest.allure.severity('critical')
    def test_click_already_taken_31(self, d):
        """
        点击存款产已支取
        :param d:
        :return:
        """
        with pytest.allure.step("点击存款产品明细"):
            action.click_element(d, "存款产品页已支取")
        with pytest.allure.step("切换已支取标签"):
            test.assert_element_exists_save_picture(d, d(className="android.view.View", instance=4).exists, "已支取标签显示")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("32.点击明细")
    @pytest.allure.severity('critical')
    def test_click_already_taken_32(self, d):
        """
        点击存款产已支取
        :param d:
        :return:
        """
        with pytest.allure.step("点击存款产品页明细"):
            action.click_element(d, "存款产品页明细")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "交易明细")
        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("33.点击再次存入")
    @pytest.allure.severity('critical')
    def test_click_already_deposit_in_33(self, d):
        """
        点击再次存入
        :param d:
        :return:
        """
        with pytest.allure.step("点击再次存入"):
            action.click_element(d, "存款产品页再次存入")
        with pytest.allure.step("点击再次存入"):
            test.assert_element_exists_save_picture(d, action.element_exists(d, "更多产品"), "产品下架")
            time.sleep(2)
        with pytest.allure.step("点击更多产品"):
            action.click_element(d, "更多产品")
            time.sleep(2)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("34.点击资产页更多服务")
    @pytest.allure.severity('critical')
    def test_click_more_services_34(self, d):
        """
        点击资产页面
        :param d:
        :return:
        """
        with pytest.allure.step("进入梅州客商银行"):
            action.click_element(d, "首页银行按钮")
            time.sleep(2)
            d(resourceId="com.bs.finance:id/tv_name", text=u"梅州客商银行").click()
            time.sleep(2)
            action.click_element(d, "查看资产")
        with pytest.allure.step("点击更多服务"):
            action.click_element(d, "资产页更多服务")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "更多服务")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("35.点击绑定银行卡管理")
    @pytest.allure.severity('critical')
    def test_click_more_card_manage_35(self, d):
        """
        点击绑定银行卡管理
        :param d:
        :return:
        """
        with pytest.allure.step("点击绑定银行卡管理"):
            action.click_element(d, "更多服务页绑定银行卡管理")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "绑定银行卡")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("36.点击添加新银行卡")
    @pytest.allure.severity('critical')
    def test_click_more_card_manage_36(self, d):
        """
        点击绑定银行卡管理
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加新银行卡"):
            action.click_element(d, "添加新银行卡")
        with pytest.allure.step("标题验证"):
            test.assert_title(d, "添加新银行卡")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("37.返回首页")
    @pytest.allure.severity('critical')
    def test_click_more_card_manage_37(self, d):
        """
        返回首页
        :param d:
        :return:
        """
        with pytest.allure.step("返回银行页"):

            for i in range(5):
                action.click_element(d, "返回icon")
                time.sleep(2)

        with pytest.allure.step("点击比财按钮"):
            action.click_element(d, "首页比财按钮")
        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
            action.login_out(d)  # 登出
        Consts.RESULT_LIST.append('True')













