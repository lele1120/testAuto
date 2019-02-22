# -*- coding: utf-8 -*-
# @File    : Assert.py


"""
封装Assert方法

"""
import time

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


