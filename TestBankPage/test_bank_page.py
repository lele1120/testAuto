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


class TestBankPage:
    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("01.点击首页搜索")
    @pytest.allure.severity('critical')
    def test_click_bank_bank_01(self, d):
        """
        点击首页银行按钮
        :param d:
        """
        action.login_in(d)  # 登录
        time.sleep(10)
        with pytest.allure.step("点击首页银行按钮"):
            action.click_element(d, "首页银行按钮")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "收藏银行"), "收藏银行显示")
            test.assert_element_exists_save_picture(d, action.element_exists(d, "全部银行"), "全部银行显示")
            Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('bank_page')
    @pytest.allure.feature("21.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_21(self, d):
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









