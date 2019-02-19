import os
import re
import time
import allure
from Conf.Config import Config
from Params.params import get_value,change_param_for_json


class Operation:
    def __init__(self):
        self.config = Config()
        self.run_path = Config.path_dir
        self.USER_ID = str(get_value("xc手机号"))
        self.picture_verification_code = str(get_value("四位图片验证码"))
        self.login_verification_code = str(get_value("登录验证码"))

    def login_in(self, d):
        """
        比财登录
        :param d:
        :return:
        """
        self.click_element(d, "启动页进入比财")
        if d(resourceId=get_value("广告页")).exists:  # 如果弹出广告页
            self.click_element(d, "广告页关闭")  # 点击x关闭
        self.click_element(d, "首页一键登录")
        self.input_element(d, "登录页账号输入框", self.USER_ID)
        self.click_element(d, "登录页获取验证码按钮")  # 点击获取验证码
        time.sleep(2)
        if d(text=u"请填写图像验证码").exists:
            self.input_element(d, "图片验证码输入框", self.picture_verification_code)
            self.click_element(d, "图片验证码确定按钮")
        self.input_element(d, "登录验证码输入框", self.login_verification_code)
        self.click_element(d, "立即登录按钮")

    def login_out(self, d):
        """
        比财退出
        :param d:
        :return:
        """
        self.click_element(d, "首页左上角图标")
        self.click_element(d, "侧边栏设置")
        self.click_element(d, "安全退出")
        self.click_element(d, "确认退出_是")

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
        element_text = get_value(element_name)

        if element_text.find('className=') == 0:
            element_name_change = change_param_for_json(element_name)
            d(**element_name_change).wait(timeout=10.0)
            if not d(**element_name_change).exists:
                self.display_picture(d, "控件未获取到")
            d(**element_name_change).click(timeout=10.0)
            time.sleep(1)
        elif element_text.find('className=') == -1:
            d(resourceId=element_text).wait(timeout=10.0)
            if not d(resourceId=element_text).exists:
                self.display_picture(d, "控件未获取到")
            d(resourceId=element_text).click(timeout=10.0)
            time.sleep(1)


