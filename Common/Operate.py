import os
import re
import time
import allure
from Conf.Config import Config
from Params.params import get_value


class Operation:
    def __init__(self):
        self.config = Config()
        self.run_path = Config.path_dir

    def save_picture(self, d, picture_name):
        """
        保存截图
        :param d: 默认为d
        :param picture_name: 图片名称
        :return:
        """
        picture_url = self.run_path + "/Report/picture/" + picture_name + ".png"
        d.screenshot(picture_url)
        return picture_url

    def display_picture(self, d, picture_name):
        """
        测试报告展示截图
        :param d: 控件名称，默认为d
        :param picture_name: 图片名称
        :return: 无
        """
        pictor_url = self.save_picture(d, picture_name)
        file = open(pictor_url, 'rb').read()
        allure.attach(picture_name, file, allure.attach_type.PNG)  # attach显示图片

    def input_element(self, d, element_name, input_text):
        """

        :param d: 控件默认为d
        :param element_name: 控件名称详见yaml文件
        :param input_text: 需要输入的内容
        :return: 无
        """
        d(resourceId=get_value(element_name)).wait(timeout=10.0)
        d(resourceId=get_value(element_name)).set_text(input_text)
        time.sleep(1)

    def click_element_with_text(self, d, element_name, element_text):
        """

        :param d:控件默认为d
        :param element_name:控件名称详见yaml文件
        :param element_text:控件文本
        :return:
        """
        d(resourceId=get_value(element_name), text=str(element_text)).wait(timeout=10.0)
        d(resourceId=get_value(element_name), text=str(element_text)).click()
        time.sleep(1)

    def click_element(self, d, element_name):
        """
        :param d: 控件默认为d
        :param element_name: 控件名称详见yaml文件
        :return: 无
        封装控件点击操作
        """
        d(resourceId=get_value(element_name)).wait(timeout=10.0)
        if not d(resourceId=get_value(element_name)).exists:
            self.display_picture(d, "控件未获取到")
        d(resourceId=get_value(element_name)).click()
        time.sleep(1)
