#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import datetime
import random
from _pydecimal import Decimal
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


class TestContrastProfit:
    @pytest.allure.feature('profit')
    @pytest.allure.feature("01.点击首页比收益")
    @pytest.allure.severity('critical')
    def test_click_contrast_profit_01(self, d):
        """
        点击比收益标题对比
        :param d:
        :return:
        """
        action.login_in(d)  # 登录
        time.sleep(5)
        with pytest.allure.step("点击首页比收益"):
            action.click_element(d, "比收益")
        with pytest.allure.step("标题对比"):
            test.assert_title(d, "比收益")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("02.点击右上角知道")
    @pytest.allure.severity('critical')
    def test_click_know_02(self, d):
        """
        点击右上角知道
        :param d:
        :return:
        """
        with pytest.allure.step("点击首页比收益"):
            action.click_element(d, "比收益更多")
        with pytest.allure.step("标题对比"):
            test.assert_element_exists_save_picture(d, d(text=u"说明").exists, "弹出说明")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("03.关闭说明")
    @pytest.allure.severity('critical')
    def test_close_know_03(self, d):
        """
        关闭说明
        :param d:
        :return:
        """
        with pytest.allure.step("关闭说明"):
            action.click_element(d, "说明关闭")
        with pytest.allure.step("标题对比"):
            test.assert_element_exists_save_picture(d, not d(text=u"说明").exists, "关闭说明")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("04.银行存款比收益")
    @pytest.allure.severity('critical')
    def test_contrast_profit_deposit_04(self, d):
        """
        银行存款比收益
        :param d:
        :return:
        """
        prd_key = d(resourceId=get_value("比收益产品名称"))
        prd_value = d(resourceId=get_value("比收益产品收益"))
        prd_many = d(resourceId=get_value("比收益产品收益差额"))
        test.assert_profit(d, prd_key, prd_value, prd_many)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("05.修改投资金额")
    @pytest.allure.severity('critical')
    def test_modify_money_05(self, d):
        """
        修改投资金额
        :param d:
        :return:
        """
        with pytest.allure.step("修改投资金额"):
            action.click_element(d, "比收益金额选项")
            # d.swipe_points([(0.501, 0.515), (0.494, 0.581)], 0.2)   # 切换2万金额
            d.swipe_points([(0.775, 0.543), (0.5, 0.543)], 0.2)   # 切换2万金额
            time.sleep(5)
            d.click(0.514, 0.17)
        with pytest.allure.step("修改金额后对比"):
            prd_key = d(resourceId=get_value("比收益产品名称"))
            prd_value = d(resourceId=get_value("比收益产品收益"))
            prd_many = d(resourceId=get_value("比收益产品收益差额"))
            test.assert_profit(d, prd_key, prd_value, prd_many)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("06.修改年月")
    @pytest.allure.severity('critical')
    def test_modify_month_year_06(self, d):
        """
        修改年月
        :param d:
        :return:
        """
        with pytest.allure.step("点击年月下拉菜单"):
            action.click_element(d, "比收益月年选项")
        with pytest.allure.step("点击3年"):
            d(resourceId="com.bs.finance:id/tv_dayStr", text=u"3年").click()
        with pytest.allure.step("切换后对比"):
            test.assert_equal_save_picture(d, action.element_gettext(d, "比收益月年显示"), "3年", "修改年月后对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("07.查看产品详情")
    @pytest.allure.severity('critical')
    def test_prd_details_07(self, d):
        """
        查看产品详情
        :param d:
        :return:
        """
        with pytest.allure.step("查看产品详情"):
            prd_key = d(resourceId=get_value("比收益产品名称"))
            prd_key_list = []
            for i in range(prd_key.__len__()-1):
                prd_key_list.append(prd_key[i].get_text())
            for i in range(prd_key.__len__()-1):
                prd_key[i].click(timeout=10)
                test.assert_title(d, prd_key_list[i])
                time.sleep(1)
                action.click_element(d, "返回icon")
                time.sleep(1)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("08.点击添加产品")
    @pytest.allure.severity('critical')
    def test_add_prd_08(self, d):
        """
        添加产品
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "比收益添加按钮")
        with pytest.allure.step("跳转后标题对比"):
            test.assert_title(d, "添加产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("09.根据收益率逆序排序产品")
    @pytest.allure.severity('critical')
    def test_reverse_order_prd_by_yield_09(self, d):
        """
        根据收益率逆序排序产品 对比
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "比收益添加产品页收益率选项")
        with pytest.allure.step("点击添加按钮"):
            prd_syl = d(resourceId=get_value("比收益收益率数值显示"))
        with pytest.allure.step("验证收益率排序是否正确"):
            test.assert_list_no_reverse(d, prd_syl)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("10.勾选产品")
    @pytest.allure.severity('critical')
    def test_check_prd_10(self, d):
        """
        勾选产品验证选中产品在比收益展示产品列表中
        :param d:
        :return:
        """
        with pytest.allure.step("勾选全部复选框"):
            prd_name = d(resourceId=get_value("比收益产品名称"))
            prd_check = d(resourceId=get_value("比收益收益率复选框"))
            global prd_name_list
            prd_name_list = []
            time.sleep(2)
            for i in range(prd_name.__len__()):
                prd_name_list.append(prd_name[i].get_text().strip())
                with pytest.allure.step("勾选"+prd_name[i].get_text()+"产品"):
                    prd_check[i].click()
            print(prd_name_list)
            time.sleep(2)
        with pytest.allure.step("点击比收益添加产品页完成按钮"):
            action.click_element(d, "比收益添加产品页完成按钮")
            time.sleep(1)
        with pytest.allure.step("获取添加后的产品名称列表"):
            prd_name_a = []
            prd_name_b = []
            prd_name_return = d(resourceId=get_value("比收益产品名称"))

            for i in range(prd_name_return.__len__()):
                print(prd_name_return[i].get_text())
                prd_name_a.append(prd_name_return[i].get_text())

        with pytest.allure.step("向上划动产品列表"):
            d.swipe_points([(0.578, 0.94), (0.415, 0.507)], 0.2)  # 向上划动产品列表

        with pytest.allure.step("获取滑动后产品列表"):
            for i in range(prd_name_return.__len__()):
                print(prd_name_return[i].get_text())
                prd_name_b.append(prd_name_return[i].get_text())
            prd_name_return_list = list(set(prd_name_a + prd_name_b))
        with pytest.allure.step("验证添加产品在比收益产品列表中"):
            for i in range(prd_name_list.__len__()):
                assert prd_name_list[i] in prd_name_return_list
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("11.验证销量排行")
    @pytest.allure.severity('critical')
    def test_check_prd_11(self, d):
        """
        验证销量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "返回icon")
            action.click_element(d, "比收益")
            action.click_element(d, "比收益添加按钮")
        with pytest.allure.step("跳转后标题对比"):
            test.assert_title(d, "添加产品")
        with pytest.allure.step("点击销量"):
            action.click_element(d, "比收益销量选项")
            prd_sv = d(resourceId=get_value("比收益销量显示"))
            prd_sv_list = []
        for i in range(prd_sv.__len__()):
            prd_sv_list.append(int((prd_sv[i].get_text()).translate(str.maketrans('已售:', '   ')).strip()))
        with pytest.allure.step("销量对比"):
            for i in range(prd_sv_list.__len__()):
                for j in range(prd_sv_list.__len__()-1-i):
                    assert prd_sv_list[j] > prd_sv_list[j+1]
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("12.勾选产品后点击重制")
    @pytest.allure.severity('critical')
    def test_check_prd_refashion_12(self, d):
        """
        勾选产品后点击重制验证产品不在比收益展示产品列表中
        :param d:
        :return:
        """
        with pytest.allure.step("恢复数据"):
            action.click_element(d, "返回icon")
            action.click_element(d, "返回icon")
            time.sleep(1)
            action.click_element(d, "比收益")
            action.click_element(d, "比收益添加按钮")
            action.click_element(d, "比收益添加产品页收益率选项")
        with pytest.allure.step("勾选全部复选框"):
            prd_name = d(resourceId=get_value("比收益产品名称"))
            prd_check = d(resourceId=get_value("比收益收益率复选框"))
            global prd_name_list
            prd_name_list = []
            for i in range(prd_name.__len__()):
                prd_name_list.append(prd_name[i].get_text().strip())
                with pytest.allure.step("勾选"+prd_name[i].get_text()+"产品"):
                    prd_check[i].click()
        with pytest.allure.step("点击比收益添加产品页重制按钮"):
            action.click_element(d, "比收益添加产品页重制按钮")
        with pytest.allure.step("点击比收益添加产品页完成按钮"):
            action.click_element(d, "比收益添加产品页完成按钮")
            time.sleep(1)
        with pytest.allure.step("获取添加后的产品名称列表"):
            prd_name_a = []
            prd_name_b = []
            prd_name_return = d(resourceId=get_value("比收益产品名称"))
            for i in range(prd_name_return.__len__()):
                prd_name_a.append(prd_name_return[i].get_text())

        with pytest.allure.step("向上划动产品列表"):
            d.swipe_points([(0.578, 0.94), (0.415, 0.507)], 0.2)  # 向上划动产品列表

        with pytest.allure.step("获取滑动后产品列表"):
            for i in range(prd_name_return.__len__()):
                prd_name_b.append(prd_name_return[i].get_text())
            prd_name_return_list = list(set(prd_name_a + prd_name_b))
        with pytest.allure.step("验证添加产品在比收益产品列表中"):
            for i in range(prd_name_list.__len__()):
                assert prd_name_list[i] not in prd_name_return_list
        Consts.RESULT_LIST.append('True')
        with pytest.allure.step("恢复数据"):
            action.click_element(d, "返回icon")

    @pytest.allure.feature('profit')
    @pytest.allure.feature("13.点击直销银行理财")
    @pytest.allure.severity('critical')
    def test_click_cp_financing_13(self, d):
        """
        点击直销银行理财
        :param d:
        :return:
        """
        time.sleep(5)
        with pytest.allure.step("点击比收益"):
            action.click_element(d, "比收益")
        with pytest.allure.step("获取存款产品名称"):
            deposit_prd = d(resourceId=get_value("比收益产品名称"))[0].get_text()
            print(deposit_prd)
        with pytest.allure.step("点击直销银行理财"):
            d(resourceId="com.bs.finance:id/tv_tab_title", text=u"直销银行理财").click()
        with pytest.allure.step("获取理财产品名称"):
            financing_prd = d(resourceId=get_value("比收益理财产品名称"))[0].get_text(timeout=10)
        with pytest.allure.step("验证产品是否切换"):
            assert deposit_prd is not financing_prd
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("14.直销银行理财比收益")
    @pytest.allure.severity('critical')
    def test_contrast_profit_deposit_14(self, d):
        """
        理财产品比收益
        :param d:
        :return:
        """
        # prd_key = d(resourceId=get_value("比收益理财产品名称"))
        prd_value = d(resourceId=get_value("比收益理财产品收益"))
        prd_many = d(resourceId=get_value("比收益理财产品收益差额"))
        prd_value_list = []
        prd_many_list = []

        for i in range(prd_value.__len__()):
            prd_value_list.append(Decimal(prd_value[i].get_text()).quantize(Decimal('0.00')))

        print(prd_value_list)

        for i in range(prd_many.__len__()):
            prd_many_value = (prd_many[i].get_text()).translate(str.maketrans('+', ' ')).strip()
            prd_many_list.append(Decimal(prd_many_value).quantize(Decimal('0.00')))

        print(prd_many_list)

        for i in range(prd_value.__len__()-1):
            prd_db = prd_value_list[i] - prd_many_list[i]
            print(prd_value_list[i])
            print("--------------------------")
            print(prd_many_list[i])
            test.assert_equal_save_picture(d, prd_db,  prd_value_list[-1], "收益计算对比")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("15.修改投资金额")
    @pytest.allure.severity('critical')
    def test_modify_money_15(self, d):
        """
        修改投资金额
        :param d:
        :return:
        """
        with pytest.allure.step("修改投资金额"):
            action.click_element(d, "比收益金额选项")
            # d.swipe_points([(0.783, 0.589), (0.494, 0.581)], 0.2)   # 切换2万金额
            d.swipe_points([(0.775, 0.543), (0.5, 0.543)], 0.2)   # 切换2万金额
            time.sleep(1)
            d.click(0.514, 0.17)
        with pytest.allure.step("修改金额后对比"):
            time.sleep(5)
            prd_value = d(resourceId=get_value("比收益理财产品收益"))
            prd_many = d(resourceId=get_value("比收益理财产品收益差额"))
            prd_value_list = []
            prd_many_list = []
            for i in range(prd_value.__len__()):
                prd_value_list.append(Decimal(prd_value[i].get_text()).quantize(Decimal('0.00')))

            print(prd_value_list)

            for i in range(prd_many.__len__()):
                prd_many_value = (prd_many[i].get_text()).translate(str.maketrans('+', ' ')).strip()
                prd_many_list.append(Decimal(prd_many_value).quantize(Decimal('0.00')))

            print(prd_many_list)

            for i in range(prd_value.__len__() - 1):
                prd_db = prd_value_list[i] - prd_many_list[i]
                print(prd_value_list[i])
                print("--------------------------")
                print(prd_many_list[i])
                test.assert_equal_save_picture(d, prd_db, prd_value_list[-1], "收益计算对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("16.修改年月")
    @pytest.allure.severity('critical')
    def test_modify_month_year_16(self, d):
        """
        修改年月
        :param d:
        :return:
        """
        with pytest.allure.step("点击年月下拉菜单"):
            action.click_element(d, "比收益月年选项")
        with pytest.allure.step("点击3年"):
            d(resourceId="com.bs.finance:id/tv_dayStr", text=u"3年").click()
        with pytest.allure.step("切换后对比"):
            test.assert_equal_save_picture(d, action.element_gettext(d, "比收益月年显示"), "3年", "修改年月后对比")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("17.查看产品详情")
    @pytest.allure.severity('critical')
    def test_prd_details_17(self, d):
        """
        查看理财产品详情
        :param d:
        :return:
        """
        with pytest.allure.step("查看产品详情"):
            prd_key = d(resourceId=get_value("比收益理财产品名称"))
            prd_key_list = []
            for i in range(prd_key.__len__()-1):
                prd_key_list.append(prd_key[i].get_text())
            for i in range(prd_key.__len__()-1):
                prd_key[i].click(timeout=10)
                test.assert_title(d, prd_key_list[i])
                time.sleep(1)
                action.click_element(d, "返回icon")
                time.sleep(1)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("18.点击添加产品")
    @pytest.allure.severity('critical')
    def test_add_prd_18(self, d):
        """
        点击添加理财产品
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "比收益添加按钮")
        with pytest.allure.step("跳转后标题对比"):
            test.assert_title(d, "添加产品")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("19.根据收益率逆序排序产品")
    @pytest.allure.severity('critical')
    def test_reverse_order_prd_by_yield_19(self, d):
        """
        根据收益率逆序排序产品
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "比收益添加产品页收益率选项")
        with pytest.allure.step("点击添加按钮"):
            time.sleep(5)
            prd_syl = d(resourceId=get_value("比收益收益率数值显示"))
        with pytest.allure.step("验证收益率排序是否正确"):
            test.assert_list_no_reverse(d, prd_syl)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("20.勾选产品")
    @pytest.allure.severity('critical')
    def test_check_prd_20(self, d):
        """
        勾选产品验证选中产品在比收益展示产品列表中
        :param d:
        :return:
        """
        with pytest.allure.step("勾选全部复选框"):
            prd_name = d(resourceId=get_value("比收益产品名称"))
            prd_check = d(resourceId=get_value("比收益收益率复选框"))
            global prd_name_list
            prd_name_list = []
            time.sleep(2)
            for i in range(prd_name.__len__()):
                prd_name_list.append(prd_name[i].get_text().strip())
                with pytest.allure.step("勾选"+prd_name[i].get_text()+"产品"):
                    prd_check[i].click()
            print(prd_name_list)
            time.sleep(2)
        with pytest.allure.step("点击比收益添加产品页完成按钮"):
            action.click_element(d, "比收益添加产品页完成按钮")
            time.sleep(1)
        with pytest.allure.step("获取添加后的产品名称列表"):
            prd_name_a = []
            prd_name_b = []
            prd_name_return = d(resourceId=get_value("比收益理财产品名称"))

            for i in range(prd_name_return.__len__()):
                print(prd_name_return[i].get_text())
                prd_name_a.append(prd_name_return[i].get_text())

        with pytest.allure.step("向上划动产品列表"):
            d.swipe_points([(0.578, 0.94), (0.415, 0.507)], 0.2)  # 向上划动产品列表

        with pytest.allure.step("获取滑动后产品列表"):
            for i in range(prd_name_return.__len__()):
                print(prd_name_return[i].get_text())
                prd_name_b.append(prd_name_return[i].get_text())
            prd_name_return_list = list(set(prd_name_a + prd_name_b))
        with pytest.allure.step("验证添加产品在比收益产品列表中"):
            for i in range(prd_name_list.__len__()):
                assert prd_name_list[i] in prd_name_return_list
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('profit')
    @pytest.allure.feature("21.验证销量排行")
    @pytest.allure.severity('critical')
    def test_check_prd_21(self, d):
        """
        验证销量排行
        :param d:
        :return:
        """
        with pytest.allure.step("点击添加按钮"):
            action.click_element(d, "返回icon")
            action.click_element(d, "比收益")
            d(resourceId="com.bs.finance:id/tv_tab_title", text=u"直销银行理财").click(timeout=10)
            action.click_element(d, "比收益添加按钮")
        with pytest.allure.step("跳转后标题对比"):
            test.assert_title(d, "添加产品")
        with pytest.allure.step("点击销量"):
            action.click_element(d, "比收益销量选项")
            prd_sv = d(resourceId=get_value("比收益销量显示"))
            prd_sv_list = []
        for i in range(prd_sv.__len__()):
            prd_sv_list.append(int((prd_sv[i].get_text()).translate(str.maketrans('已售:', '   ')).strip()))
        with pytest.allure.step("销量对比"):
            for i in range(prd_sv_list.__len__()):
                for j in range(prd_sv_list.__len__()-1-i):
                    assert prd_sv_list[j] > prd_sv_list[j+1]
        Consts.RESULT_LIST.append('True')
        action.click_element(d, "返回icon")
        action.click_element(d, "返回icon")
        time.sleep(1)

    @pytest.allure.feature('profit')
    @pytest.allure.feature("22.勾选产品后点击重制")
    @pytest.allure.severity('critical')
    def test_check_prd_refashion_22(self, d):
        """
        勾选产品后点击重制验证产品不在比收益展示产品列表中
        :param d:
        :return:
        """
        with pytest.allure.step("恢复数据"):
            action.click_element(d, "比收益")
            d(resourceId="com.bs.finance:id/tv_tab_title", text=u"直销银行理财").click(timeout=10)
            action.click_element(d, "比收益添加按钮")
            action.click_element(d, "比收益添加产品页收益率选项")
        with pytest.allure.step("勾选全部复选框"):
            time.sleep(5)
            prd_name = d(resourceId=get_value("比收益产品名称"))
            prd_check = d(resourceId=get_value("比收益收益率复选框"))
            global prd_name_list
            prd_name_list = []
            for i in range(prd_name.__len__()):
                prd_name_list.append(prd_name[i].get_text().strip())
                with pytest.allure.step("勾选"+prd_name[i].get_text()+"产品"):
                    prd_check[i].click()
        with pytest.allure.step("点击比收益添加产品页重制按钮"):
            action.click_element(d, "比收益添加产品页重制按钮")
        with pytest.allure.step("点击比收益添加产品页完成按钮"):
            action.click_element(d, "比收益添加产品页完成按钮")
            time.sleep(1)
        with pytest.allure.step("获取添加后的产品名称列表"):
            prd_name_a = []
            prd_name_b = []
            prd_name_return = d(resourceId=get_value("比收益理财产品名称"))
            for i in range(prd_name_return.__len__()):
                prd_name_a.append(prd_name_return[i].get_text())

        with pytest.allure.step("向上划动产品列表"):
            d.swipe_points([(0.578, 0.94), (0.415, 0.507)], 0.2)  # 向上划动产品列表

        with pytest.allure.step("获取滑动后产品列表"):
            for i in range(prd_name_return.__len__()):
                prd_name_b.append(prd_name_return[i].get_text())
            prd_name_return_list = list(set(prd_name_a + prd_name_b))
        with pytest.allure.step("验证添加产品在比收益产品列表中"):
            for i in range(prd_name_list.__len__()):
                assert prd_name_list[i] not in prd_name_return_list
        Consts.RESULT_LIST.append('True')
        with pytest.allure.step("恢复数据"):
            action.click_element(d, "返回icon")
            time.sleep(2)
            action.login_out(d)  # 登出












