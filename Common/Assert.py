# -*- coding: utf-8 -*-
# @File    : Assert.py


"""
封装Assert方法

"""
import time

import pytest

from Common import Log, Operate
from Common import Consts
from Params.params import get_value


class Assertions:
    def __init__(self):
        self.log = Log.MyLog()
        self.operation = Operate.Operation()

    def assert_equal_save_picture(self, d, first, second, picture_name):
        """
        字符串断言，成功截图展示图片，失败截图展示图片
        :param d:d
        :param str_a:字符串a
        :param str_b:字符串b
        :param picture_name:图片名称
        :return:
        """
        try:
            assert first == second
            # self.operation.display_picture(d, picture_name + "_成功")
            print(picture_name + "_成功")
            return True
        except:
            print(picture_name + "_失败")
            self.operation.display_picture(d, picture_name + "_失败")
            self.log.error("断言失败 %s 不等于 %s " % (first, second))
            Consts.RESULT_FAIL_LIST.append('fail')
            raise

    def assert_element_exists_save_picture(self, d, bool_a, picture_name):
        """

        :param d:d
        :param bool_a: 控件.exists 存在返回ture，不存在返回Flase
        :param picture_name: 图片名称
        :return:
        """
        try:
            assert bool_a
            # self.operation.display_picture(d, picture_name + "_成功")
            print(picture_name + "_成功")
        except:
            print(picture_name + "_失败")
            self.operation.display_picture(d, picture_name + "_失败")
            self.log.error("断言失败控件不存在 ")
            Consts.RESULT_FAIL_LIST.append('fail')
            raise

    def assert_title(self, d, title):
        """
        :param d: 控件默认为d
        :param title: 页面标题
        :return: 无
        验证页面是否跳转成功

        """
        if not d(resourceId=get_value("标题")).exists:
            time.sleep(2)
        try:
            self.assert_equal_save_picture(d, title, d(resourceId=get_value("标题")).get_text(), "标题对比")
            print("页面title为:" + str(d(resourceId=get_value("标题")).get_text()))
            print("预期页面的title为:" + str(title))
            time.sleep(1)
        except:
            self.operation.display_picture(d, "控件未获取到")
            self.log.error("对比" + title + "控件")
            raise

    def assert_list(self, d, tv_temp):
        tv_temp_list = []
        tv_temp_list_c = []
        for i in range(tv_temp.__len__()):
            # print("排行榜数值:" + (tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip())
            tv_temp_list.append(float((tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip()))
            tv_temp_list_c.append(float((tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip()))

        tv_temp_list.sort()
        tv_temp_list.reverse()
        print(tv_temp_list)
        print(tv_temp_list_c)
        for i in range(tv_temp_list.__len__()):
            self.assert_equal_save_picture(d, tv_temp_list[i], tv_temp_list_c[i], "排序后对比")

    def assert_list_no_reverse(self, d, tv_temp):
        tv_temp_list = []
        tv_temp_list_c = []
        for i in range(tv_temp.__len__()):
            # print("排行榜数值:" + (tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip())
            tv_temp_list.append(float((tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip()))
            tv_temp_list_c.append(float((tv_temp[i].get_text()).translate(str.maketrans('%', ' ')).strip()))

        tv_temp_list.sort()
        # tv_temp_list.reverse()
        print(tv_temp_list)
        print(tv_temp_list_c)
        for i in range(tv_temp_list.__len__()):
            self.assert_equal_save_picture(d, tv_temp_list[i], tv_temp_list_c[i], "排序后对比")

    def assert_profit(self, d, prd_key, prd_value, prd_many):
        dict_prd = {}
        prd_key_list = []
        prd_value_list = []
        prd_many_list = []

        for i in range(prd_key.__len__()):
            dict_prd[prd_key[i].get_text()] = float(prd_value[i].get_text())
        print(dict_prd)

        for key in dict_prd:
            prd_key_list.append(key)
        print(prd_key_list)

        for key in dict_prd:
            prd_value_list.append(dict_prd[key])
        print(prd_value_list)

        for i in range(prd_many.__len__()):
            prd_many_list.append(float((prd_many[i].get_text()).translate(str.maketrans('+', ' ')).strip()))
        print(prd_many_list)

        for i in range(prd_many_list.__len__()):
            many_num = prd_value_list[i] - prd_many_list[i]
            with pytest.allure.step("验证收益计算\n" + str(prd_value_list[i]) + "减" + str(prd_many_list[i])+"等于"+str(many_num)):
                self.assert_equal_save_picture(d, many_num, prd_value_list[-1], "产品收益对比")


