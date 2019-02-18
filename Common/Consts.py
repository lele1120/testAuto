# -*- coding: utf-8 -*-
# @File    : Consts.py

"""
UI全局变量

"""

# UI全局配置
import sys

UI_ENVIRONMENT_DEBUG = 'debug'
UI_ENVIRONMENT_RELEASE = 'release'
UI_ENVIRONMENT_MOBILE_PHONE_MODEL = sys.argv[1]
# UI_ENVIRONMENT_MOBILE_PHONE_MODEL = '360手机udid'


# UI响应时间list，单位毫秒
STRESS_LIST = []

# UI执行list
TEST_LIST = []

# UI执行结果list
RESULT_LIST = []

# UI 执行失败list
RESULT_FAIL_LIST = []

