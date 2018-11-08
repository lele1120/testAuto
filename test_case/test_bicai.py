# -*- coding: utf-8 -*-
import os
import time
import pytest
import allure

from biz.get_value_by_yaml import Get_Value_By_Yaml


@pytest.fixture(scope='module')
def driver():
    driver = Get_Value_By_Yaml().get_driver_by_key("Y66手机ip")
    driver.set_fastinput_ime(True)
    driver.session("com.bs.finance")
    yield driver
    driver.app_stop("com.bs.finance")


@allure.story('测试点击头像弹出侧边栏')
def test_one(driver):
    driver(resourceId="com.bs.finance:id/iv_user").click()
    with allure.step("点击头像"):
        allure.attach('商品1', '刘春明')  # attach可以打印一些附加信息
        assert 1 == 1


def test_two(driver):
    assert 1 == 1


if __name__ == '__main__':
    # 执行所有case并生成报告
    pytest.main("--alluredir ../report/xml")
    os.system('allure generate ../report/xml -o ../report/html --clean')
    # time.sleep(5)
    # os.system('allure open -h 127.0.0.1 -p 8083 /Users/xuchen/PycharmProjects/testAuto/report/html')
