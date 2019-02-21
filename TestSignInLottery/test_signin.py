#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re
import time
import pytest
from os import path
from Params.params import get_value
from Common import Operate
from Common import Consts
from Common import Assert

import sys

test = Assert.Assertions()
action = Operate.Operation()
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))


class TestSignIn:
    @pytest.allure.feature('sigin')
    @pytest.allure.feature("01.启动app后进入比财")
    @pytest.allure.severity('critical')
    def test_go_main_01(self, d):
        """
        首次启动app点击进入比财,如果有广告页点击x关闭，
        :param d:
        :return:
        """

        time.sleep(5)

        with pytest.allure.step("启动页点击进入比财"):
            action.click_element(d, "启动页进入比财")

        with pytest.allure.step("如果弹出广告页点x关闭"):
            if d(resourceId=get_value("广告页")).exists:  # 如果弹出广告页

                action.click_element(d, "广告页关闭")  # 点击x关闭

        with pytest.allure.step("验证启动app点击进入比财是否进入首页"):
            test.assert_element_exists_save_picture(d, d(text="一键登录").exists, "验证是否有文本为一键登录的控件")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("02.比财登录")
    @pytest.allure.severity('critical')
    def test_login_02(self, d):
        """
        比财账号登录

        """

        global USER_ID  # 使用账号

        USER_ID = str(get_value("xc手机号"))

        picture_verification_code = str(get_value("四位图片验证码"))

        login_verification_code = str(get_value("登录验证码"))

        with pytest.allure.step("点击app首页一键登录"):
            action.click_element(d, "首页一键登录")

        with pytest.allure.step("在登录页账号输入框输入账号"):
            action.input_element(d, "登录页账号输入框", USER_ID)

        with pytest.allure.step("点击获取验证码"):
            action.click_element(d, "登录页获取验证码按钮")  # 点击获取验证码

        #  如果弹出4位数字图片验证码
        with pytest.allure.step("输入4位验证码"):
            time.sleep(2)
            if d(text=u"请填写图像验证码").exists:
                action.input_element(d, "图片验证码输入框", picture_verification_code)
                with pytest.allure.step("点击确认按钮"):
                    action.click_element(d, "图片验证码确定按钮")

        with pytest.allure.step("输入6位验证码"):
            action.input_element(d, "登录验证码输入框", login_verification_code)

        with pytest.allure.step("点击立即登录"):
            action.click_element(d, "立即登录按钮")

        with pytest.allure.step("验证是否登录成功"):
            test.assert_element_exists_save_picture(d, not d(resourceId=get_value("首页一键登录")).exists, "验证是否登录")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("03.弹出侧边栏")
    @pytest.allure.severity('critical')
    def test_sidebar_eject_03(self, d):
        """
         验证点击左上角图标弹出侧边栏功能
        """

        global cebian_button  # 侧边栏按钮

        global realname_status  # 实名认证状态

        cebian_button = ["我的关注", "我的消息", "我的钱包", "关于我们"]

        with pytest.allure.step("点击左上角图标"):
            action.click_element(d, "首页左上角图标")
            time.sleep(10)

        with pytest.allure.step("检验侧边栏控件"):
            for i in range(cebian_button.__len__()):
                test.assert_element_exists_save_picture(d, d(text=cebian_button[i]).exists,
                                                        "验证侧边栏" + cebian_button[i] + "按钮控件存在")

        with pytest.allure.step("验证账号为已登录状态，账号为" + USER_ID):
            user_id = d(resourceId=get_value("侧边栏账号")).get_text()

            test.assert_equal_save_picture(d, user_id, USER_ID.replace((USER_ID[3:7]), "****"),
                                           "账号" + USER_ID + "已登录状态")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("04.点击签到")
    @pytest.allure.severity('critical')
    def test_click_sign_in_04(self, d):
        """
        点击签到
        :param d:
        :return:
        """

        if d(resourceId="com.bs.finance:id/tab3_dot").exists:
            not_sign_in = 1  # 签到上方红点存在，今日还未点击过签到按钮
        else:
            not_sign_in = 0  # 签到上方红点不存在，今日已点击过签到按钮

        time.sleep(5)

        with pytest.allure.step("点击签到"):
            action.click_element(d, "签到")

            time.sleep(5)

        with pytest.allure.step("校验是否跳转成功"):
            test.assert_title(d, "签到")
            # time.sleep(10)
            # 需要添加 查找当天数据 没查到向下滑动 再查 获取当天记录对比
            # sign_in_state = d(className="android.view.View")[29].info['contentDescription']
            # test.assert_equal_save_picture(d, sign_in_state, "今日已签到", "签到")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("05.签到抽奖校验")
    @pytest.allure.severity('critical')
    def test_click_sign_in_luck_draw_05(self, d):
        """
        签到抽奖校验
        :param d:
        :return:
        """

        global red_envelope_money

        with pytest.allure.step("签到抽奖校验"):
            time.sleep(5)
            for i in range(d(className="android.widget.Image").__len__()):
                if d(className="android.widget.Image")[i].exists:
                    if d(className="android.widget.Image")[i].info['contentDescription'] == "5@2x":
                        print("今日未抽奖")
                        with pytest.allure.step("点击抽奖"):
                            d(className="android.widget.Image")[i].click()
                            time.sleep(5)
                            d(className="android.widget.Image")[i].click()
                            time.sleep(5)
                            for j in range(d(className="android.view.View").__len__()):
                                print("----------------------------------------------------------------")
                                print(d(className="android.view.View")[j].info['contentDescription'])
                                print("----------------------------------------------------------------")
                                if "获得" in str(d(className="android.view.View")[j].info['contentDescription']):
                                    print("*-*-*-*-*-*-*")
                                    print(j)
                                    print("*-*-*-*-*-*-*")
                                    red_envelope_money_text = (d(className="android.view.View")[j]).info['contentDescription']
                                    print("*********************************")
                                    print(red_envelope_money_text)
                                    print("*********************************")
                                    red_envelope_money = re.findall(r'-?\d+\.?\d*e?-?\d*?', red_envelope_money_text)
                                    print("抽中金额:" + str(red_envelope_money) + "元")
                                    time.sleep(2)

                                    d(description=u"查看我的中奖记录").click(timeout=10)

                                    time.sleep(2)

                                    d(resourceId="com.bs.finance:id/rl_back").click(timeout=10)

                                    break

            print("该用户已抽奖")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("06.查看活动规则")
    @pytest.allure.severity('critical')
    def test_look_activity_rules_06(self, d):
        """
        查看活动规则
        :param d:
        :return:
        """

        with pytest.allure.step("查看活动规则"):

            d(description=u"活动规则").click(timeout=10)

            time.sleep(2)

            test.assert_element_exists_save_picture(d, d(description=u"签到抽奖规则").exists, "签到规则跳转")

        with pytest.allure.step("点击活动规则关闭"):
            # d(className="android.view.View", instance=1).click(timeout=10)
            d(description=u"yAAAAAElFTkSuQmCC").click(timeout=10)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("07.点击分享")
    @pytest.allure.severity('critical')
    def test_click_share_friend_07(self, d):
        """
        点击分享给朋友
        :param d:
        :return:
        """

        time.sleep(2)
        with pytest.allure.step("点击分享按钮"):
            d(description=u"分享").click(timeout=10)  # 点击分享

        with pytest.allure.step("点击发送给朋友"):

            d(description=u"发送给朋友", className="android.view.View").click(timeout=10)  # 点击发送给朋友

            time.sleep(3)

        with pytest.allure.step("选择要发送的人"):

            d(resourceId="com.tencent.mm:id/pp", text=u"熊出没请您注意").click(timeout=10)

        with pytest.allure.step("点击分享"):

            d(resourceId="com.tencent.mm:id/ayb").click(timeout=10)

        with pytest.allure.step("点击返回比财"):

            d(resourceId="com.tencent.mm:id/aya").click(timeout=10)  # 返回比财
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("08.点击分享圈")
    @pytest.allure.severity('critical')
    def test_click_share_circle_of_friend_08(self, d):
        """
        点击分享给朋友圈
        :param d:
        :return:
        """

        time.sleep(2)

        with pytest.allure.step("点击分享按钮"):
            d(description=u"分享").click(timeout=10)  # 点击分享

        with pytest.allure.step("点击发送到朋友圈"):
            d(description=u"发送到朋友圈").click(timeout=10)  # 点击发送给朋友圈

        with pytest.allure.step("点击发表"):

            d(resourceId="com.tencent.mm:id/jq").click(timeout=10)
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("09.签到页查看我的中奖记录")
    @pytest.allure.severity('critical')
    def test_click_my_winning_record_09(self, d):
        """
        在签到页点击我的中奖记录
        :param d:
        :return:
        """

        with pytest.allure.step("向下滑动"):
            d(scrollable=True).scroll(steps=30)  # 向下滑动
            time.sleep(2)
        with pytest.allure.step("点击我的中奖记录"):
            d(description=u"我的中奖记录").click(timeout=10)
            time.sleep(2)
            test.assert_title(d, "签到")

        with pytest.allure.step("我的中奖记录中含有今日已发放记录"):
            now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))
            test.assert_element_exists_save_picture(d, d(description=str(now_date)).exists, "签到记录中记录今日签到记录")

        with pytest.allure.step("点击我的中奖记录"):
            action.click_element(d, "左上角关闭")
        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("10.点击设置")
    @pytest.allure.severity('Block')
    def test_click_set_up_10(self, d):
        """
        点击设置
        :param d:
        :return:
        """

        with pytest.allure.step("点击设置"):
            time.sleep(5)

            action.click_element(d, "侧边栏设置")

        with pytest.allure.step("title校验"):
            test.assert_title(d, "设置")

        Consts.RESULT_LIST.append('True')

    @pytest.allure.feature('sigin')
    @pytest.allure.feature("09.app退出")
    @pytest.allure.severity('critical')
    def test_sign_out_app_09(self, d):
        """
        退出app
        :param d:
        :return:
        """

        with pytest.allure.step("点击安全退出"):
            action.click_element(d, "安全退出")

        with pytest.allure.step("点击确认退出_是"):
            action.click_element(d, "确认退出_是")

        with pytest.allure.step("验证app已成功退出"):
            assert d(text="一键登录").exists  # 验证是否有文本为一键登录的控件

        action.display_picture(d, "app退出")

        Consts.RESULT_LIST.append('True')











