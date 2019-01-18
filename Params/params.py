# -*- coding: utf-8 -*-
# @Author  : XuChen


"""
定义所有测试数据

"""
import os
import re

import yaml
from Common import Log
import uiautomator2 as u2
log = Log.MyLog()
path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))


def get_target_value(key, dic, tmp_list):
    """
    :param key: 目标key
    :param dic: JSON数据
    :param tmp_list: 用于存储获取的数据
    :return: list
    """
    if not isinstance(dic, dict) or not isinstance(tmp_list, list):  # 对传入数据进行格式校验
        return 'argv[1] not an dict or argv[-1] not an list '

    if key in dic.keys():
        tmp_list.append(dic[key])  # 传入数据存在则存入tmp_list
    else:
        for value in dic.values():  # 传入数据不符合则对其value值进行遍历
            if isinstance(value, dict):
                get_target_value(key, value, tmp_list)  # 传入数据的value值是字典，则直接调用自身
            elif isinstance(value, (list, tuple)):
                _get_value(key, value, tmp_list)  # 传入数据的value值是列表或者元组，则调用_get_value
    return tmp_list


def _get_value(key, val, tmp_list):
    for val_ in val:
        if isinstance(val_, dict):
            get_target_value(key, val_, tmp_list)  # 传入数据的value值是字典，则调用get_target_value
        elif isinstance(key, val_, (list, tuple)):
            _get_value(key, val_, tmp_list)  # 传入数据的value值是列表或者元组，则调用自身


def get_value(key):
    """

    :param key: 关键字
    :return:无
    """
    log.info('解析yaml, Path:' + path_dir + '/Params/Param/cfgyaml')
    yamlPath = path_dir+"/Params/Param/cfgyaml"
    f = open(yamlPath, 'r', encoding='utf-8')
    cfg = f.read()
    d = yaml.load(cfg)
    return get_target_value(key, d, [])[0]


def get_driver_by_key(key):
    """
    :param key:使用yaml文件中的设备usb连接名称，或者ip连接名称，自动识别设备，使用ping ip和adb devices的方式判断设备是否可用
    :return: 返回设备driver
    """
    if type(key) == str:
        if key[-1] == "p":
            ip = get_value(key)
            backinfo = os.system("ping -c 5 " + ip)
            if backinfo == 0:
                d = u2.connect_wifi(get_value(key))
                return d
            else:
                print("未发现ip为" + ip + "的移动设备")
        elif key[-1] == "d":
            uuid = get_value(key)
            readDeviceId = list(os.popen('adb devices').readlines())
            deviceId = re.findall(r'^\w*\b', readDeviceId[1])[0]
            if uuid == deviceId:
                d = u2.connect_usb(uuid)
                return d
            else:
                print("未发现udid为" + uuid + "的移动设备")
    else:
        print("请使用yaml文件中的设备连接名称")
