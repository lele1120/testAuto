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
    @pytest.allure.feature("01.点击首页搜索")
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
            d(scrollable=True).scroll(steps=30)  # 向下滑动
            time.sleep(2)
            bank_name_list = d(resourceId=get_value("银行名称"))
            i_bank = random.randint(0, bank_name_list.__len__())
            global i_bank_name
            i_bank_name = d(resourceId=get_value("银行名称"))[i_bank].get_text()
            print(i_bank_name)

        with pytest.allure.step("点击" + i_bank_name + "跳转"):
            try:
                d(resourceId=get_value("银行名称"))[i_bank].click(timeout=10)
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

        with pytest.allure.step("点击返回icon返回银行页"):
            action.click_element(d, "返回icon")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("07.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_07(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("返回首页"):
            action.click_element(d, "首页比财按钮")

        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')
        action.login_out(d)  # 登出









