# 对于H5 无法定位的元素 获取android.view.View内文本
import random
import re
import time
import allure


from TestCase.get_test_value_by_yaml import get_driver_by_key
from TestCase.test_sidebar import click_element, assert_title, assert_equal_save_picture

d = get_driver_by_key("Y66手机udid")   # 输入手机udid启动  调试 在侧边栏进行各种操作

# for i in range(d(className="android.view.View").__len__()):
#     print(d(className="android.view.View")[i].info)
#     if d(className="android.view.View")[i].info['contentDescription'] == '今日已签到':
#         print("==================================")
#         print("此刻i的值为：" + str(i))
#         print("==================================")
#     print("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-")
#
#
# for i in range(d(className="android.widget.Image").__len__()):
#     print(d(className="android.widget.Image")[i].info['contentDescription'])
#
#     print("------------------")
# print(d(className="android.widget.Image").__len__())
# for i in range(d(className="android.widget.Image").__len__()):
#     print(d(className="android.widget.Image")[i].info['contentDescription'])
#     print("------------------")
# time.sleep(2)
# print(d(className="android.widget.Image").__len__())
# for i in range(d(className="android.widget.Image").__len__()):
#     print(d(className="android.widget.Image")[i].info['contentDescription'])
#     print("------------------")

# d(className="android.widget.Image")[6].click()

# print(d(className="android.widget.Image")[6].info)
#
# if d(className="android.widget.Image")[6].info['contentDescription'] == "5@2x":
#     print("+++++++++++++++++++++++++++++++++++++++++")

# print(random.randint(2, 10))

with allure.step("点击签到"):
    click_element(d, "签到")

with allure.step("校验是否跳转成功"):
    assert_title(d, "签到")
    time.sleep(10)
    sign_in_state = d(className="android.view.View")[29].info['contentDescription']
    assert_equal_save_picture(d, sign_in_state, "今日已签到", "签到")

with allure.step("签到校验"):

    for i in range(d(className="android.widget.Image").__len__()):
        if d(className="android.widget.Image")[i].info['contentDescription'] == "5@2x":
            print("今日未抽奖")
            with allure.step("点击抽奖"):
                d(className="android.widget.Image")[i].click()
                time.sleep(5)
                d(className="android.widget.Image")[i].click()
                for j in range(d(className="android.view.View").__len__()):
                    if "获得" in str(d(className="android.view.View")[j].info['contentDescription']):
                        red_envelope_money_text = (d(className="android.view.View")[j]).info['contentDescription']
                        print(red_envelope_money_text)
                        red_envelope_money = re.findall(r'-?\d+\.?\d*e?-?\d*?', red_envelope_money_text)
                        print("抽中金额:" + str(red_envelope_money) + "元")
                        break

            with allure.step("点击查看中奖记录"):

                d(description=u"查看我的中奖记录").click()
                red_envelope_money_record_text = (d(className="android.view.View")[0]).info['contentDescription']
                red_envelope_record_money = re.findall(r'-?\d+\.?\d*e?-?\d*?', red_envelope_money_record_text)

                assert_equal_save_picture(d, red_envelope_money, red_envelope_record_money, "抽到红包与最新记录金额对比")

                record_date = (d(className="android.view.View")[2]).info['contentDescription']

                now_date = time.strftime('%Y-%m-%d', time.localtime(time.time()))

                assert_equal_save_picture(d, record_date, now_date, "抽奖日期对比")

                click_element(d, "左上角关闭")
