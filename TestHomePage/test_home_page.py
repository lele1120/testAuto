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


class TestHomePage:
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

        Consts.RESULT_LIST.append('True')

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
            test.assert_title(d, "拼团")
            # time.sleep(5)
            # test.assert_element_exists_save_picture(d, d(description=u"活动规则").exists, "活动规则按钮")
            # test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "往期拼团按钮")
            # test.assert_element_exists_save_picture(d, d(description=u"拼团", className="android.view.View", instance=1).exists, "拼团按钮")
            # test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "活动投资按钮")
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

    # @pytest.allure.feature('homepage')
    # @pytest.allure.feature("12.点击首页banner")
    # @pytest.allure.severity('critical')
    # def test_click_banner_12(self, d):
    #     """
    #     点击排行榜
    #     :param d:
    #     :return:
    #     """
    #     with pytest.allure.step("点击首页banner"):
    #         action.click_element(d, "首页banner")
    #
    #     with pytest.allure.step("验证跳转成功"):
    #         test.assert_title(d, "拼团阖家欢")
    #         time.sleep(10)
    #         test.assert_element_exists_save_picture(d, d(description=u"活动规则").exists, "活动规则按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "往期拼团按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"拼团", className="android.view.View", instance=1).exists, "拼团按钮")
    #         test.assert_element_exists_save_picture(d, d(description=u"往期拼团").exists, "活动投资按钮")
    #     Consts.RESULT_LIST.append('True')

    # @pytest.allure.feature('homepage')
    # @pytest.allure.feature("13.返回首页")
    # @pytest.allure.severity('critical')
    # def test_return_home_page_13(self, d):
    #     """
    #     返回首页
    #     :param d:
    #     """
    #     with pytest.allure.step("返回首页"):
    #         action.click_element(d, "返回icon")
    #
    #     with pytest.allure.step("验证返回成功"):
    #         test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
    #     Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("14.银行存款和直销银行理财切换")
    @pytest.allure.severity('critical')
    def test_choose_bank_deposit_14(self, d):
        """
        银行存款和直销银行理财切换
        :param d:
        :return:
        """
        global choose_type
        time.sleep(2)
        with pytest.allure.step("获取默认选项"):
            if action.element_exists(d, "银行存款选中下划线"):
                choose_type = 0
            elif action.element_exists(d, "直销银行理财选中下划线"):
                choose_type = 1
            else:
                choose_type = -1

            recommend_content = d(resourceId=get_value("推荐内容"))
            recommend_content_real_bank = ['推荐', '1天', '1个月内', '1-3个月', '3-6个月', '6个月以上']
            recommend_content_real_financing = ['推荐', '1天', '3-6个月', '6个月以上']
            recommend_content_test = []
            if choose_type == 0:
                for i in range(recommend_content.__len__()):
                    recommend_content_test.append(recommend_content[i].get_text())

                test.assert_equal_save_picture(d, recommend_content_test, recommend_content_real_bank, "获取推荐列表")
            elif choose_type == 1:
                for i in range(recommend_content.__len__()):
                    recommend_content_test.append(recommend_content[i].get_text())
                # test.assert_equal_save_picture(d, recommend_content_test, recommend_content_real_financing, "获取推荐列表")
            print(choose_type)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("15.直销银行理财和银行存款切换")
    @pytest.allure.severity('critical')
    def test_choose_financing_15(self, d):
        """
        直销银行理财和银行存款切换
        :param d:
        :return:
        """
        with pytest.allure.step("点击直销银行理财选项"):
            recommend_content = d(resourceId=get_value("推荐内容"))
            recommend_content_real_bank = ['推荐', '1天', '1个月内', '1-3个月', '3-6个月', '6个月以上']
            recommend_content_real_financing = ['推荐', '1天', '3-6个月', '6个月以上']
            recommend_content_test = []
            if choose_type == 0:
                action.click_element(d, "直销银行理财选项")
                test.assert_element_exists_save_picture(d, action.element_exists(d, "直销银行理财选中下划线"), "直销银行理财选中下划线显示")
                time.sleep(1)
                for i in range(recommend_content.__len__()):
                    recommend_content_test.append(recommend_content[i].get_text())
                    test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "可查询出产品")
                # test.assert_equal_save_picture(d, recommend_content_test, recommend_content_real_financing, "获取推荐列表")
            elif choose_type == 1:
                action.click_element(d, "银行存款选项")
                test.assert_element_exists_save_picture(d, action.element_exists(d, "银行存款选中下划线"), "银行存款选中下划线显示")
                time.sleep(1)
                for i in range(recommend_content.__len__()):
                    recommend_content_test.append(recommend_content[i].get_text())
                test.assert_equal_save_picture(d, recommend_content_test, recommend_content_real_bank, "获取推荐列表")
            print(choose_type)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("16.点击银行存款推荐时间选项")
    @pytest.allure.severity('critical')
    def test_click_recommend_bank_date_16(self, d):
        """
        点击银行存款推荐时间选项
        :param d:
        :return:
        """
        with pytest.allure.step("点击银行存款选项"):
            action.click_element(d, "银行存款选项")
            recommend_content = d(resourceId=get_value("推荐内容"))
            recommend_content_real_bank = ['推荐', '1天', '1个月内', '1-3个月', '3-6个月', '6个月以上']
        time.sleep(2)
        for i in range(recommend_content.__len__()):
            d(resourceId=get_value("推荐内容"))[i].click()
            time.sleep(1)
            if d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == str(recommend_content_real_bank[i]):
                with pytest.allure.step("选择"+d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text()+"选项"):
                    print("选择"+d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text()+"选项")
                    if d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "推荐":
                        # test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐排名"), "推荐排名显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
                    elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "1天":
                        test.assert_element_exists_save_picture(d, not action.element_exists(d, "推荐周期显示"), "推荐周期1天显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
                    elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "1个月内":
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"), "推荐周期1个月内显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
                    elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "1-3个月":
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"), "推荐周期1-3个月显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
                    elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "3-6个月":
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"), "推荐周期3-6个月显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
                    elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "6个月以上":
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"), "推荐周期6个月以上显示")
                        test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
        d(resourceId=get_value("推荐内容"))[0].click()
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("17.点击直销银行理财选项")
    @pytest.allure.severity('critical')
    def test_click_recommend_financing_date_17(self, d):
        """
        点击银行存款推荐时间选项
        :param d:
        :return:
        """
        with pytest.allure.step("点击直销银行理财选项"):
            action.click_element(d, "直销银行理财选项")
            recommend_content = d(resourceId=get_value("推荐内容"))
            recommend_content_real_financing = ['推荐', '1天',  '3-6个月', '6个月以上']
        time.sleep(2)
        for i in range(recommend_content.__len__()):
            d(resourceId=get_value("推荐内容"))[i].click()
            time.sleep(1)
            # if d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == str(recommend_content_real_financing[i]):
            #     with pytest.allure.step("选择" + d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() + "选项"):
            #         print("选择" + d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() + "选项")
            #         if d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "推荐":
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐排名"), "推荐排名显示")
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
            #         elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "1天":
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"),
            #                                                     "推荐周期1天显示")
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
            #         elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "3-6个月":
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"),
            #                                                     "推荐周期3-6个月显示")
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
            #         elif d(resourceId="com.bs.finance:id/tv_tab_title")[i].get_text() == "6个月以上":
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "推荐周期显示"),
            #                                                     "推荐周期6个月以上显示")
            #             test.assert_element_exists_save_picture(d, action.element_exists(d, "首页银行名称"), "推荐数据查询")
        d(resourceId=get_value("推荐内容"))[0].click()
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("18.点击银行存款推荐时间选项")
    @pytest.allure.severity('critical')
    def test_click_deposit_name_18(self, d):
        """
        点击银行存款推荐时间选项
        :param d:
        :return:
        """
        with pytest.allure.step("点击银行存款选项"):
            action.click_element(d, "银行存款选项")
        time.sleep(10)
        product_name = d(resourceId=get_value("首页产品名称")).get_text()
        bank_name = d(resourceId=get_value("首页银行名称")).get_text()
        print(product_name)
        with pytest.allure.step("点击首条产品跳转产品购买页"):
            action.click_element(d, "首页银行名称")
            test.assert_title(d, product_name)
            d(scrollable=True).scroll(steps=30)  # 向下滑动
            time.sleep(2)
            belong_to_bank = d(resourceId=get_value("产品购买页产品隶属于")).get_text().split('隶属于 ')[1]
            test.assert_equal_save_picture(d, bank_name, belong_to_bank.strip(), "银行名称对比")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("19.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_19(self, d):
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
    @pytest.allure.feature("20.点击银行理财推荐时间选项")
    @pytest.allure.severity('critical')
    def test_click_financing_name_20(self, d):
        """
        点击直销银行理财选项
        点击直销银行理财选项
        :param d:
        :return:
        """
        with pytest.allure.step("点击直销银行理财选项"):
            action.click_element(d, "直销银行理财选项")
        time.sleep(5)
        product_name = d(resourceId=get_value("首页产品名称")).get_text()
        bank_name = d(resourceId=get_value("首页银行名称")).get_text()
        print(product_name)
        with pytest.allure.step("点击首条产品跳转产品购买页"):
            action.click_element(d, "首页银行名称")
            test.assert_title(d, product_name)
            d(scrollable=True).scroll(steps=30)  # 向下滑动
            time.sleep(2)
            belong_to_bank = d(resourceId=get_value("产品购买页产品隶属于")).get_text().split('隶属于 ')[1]
            test.assert_equal_save_picture(d, bank_name, belong_to_bank.strip(), "银行名称对比")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('homepage')
    @pytest.allure.feature("21.返回首页")
    @pytest.allure.severity('critical')
    def test_return_home_page_21(self, d):
        """
        返回首页
        :param d:
        """
        with pytest.allure.step("返回首页"):
            action.click_element(d, "返回icon")

        with pytest.allure.step("验证返回成功"):
            test.assert_element_exists_save_picture(d, d(resourceId=get_value("首页左上角图标")).exists, "点击查看榜单返回首页")
        Consts.RESULT_LIST.append('True')
        action.login_out(d)  # 登出









