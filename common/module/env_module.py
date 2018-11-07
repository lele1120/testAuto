# coding:utf-8
import sys
from usage.setting import ENVIRONMENT_CONFIG


class Env_Module():

    def __init__(self):
        """
        初始化
        """
        pass

    def get_phone_ip(self, env):
        """
        :return:返回命令行环境映射测试机ip
        """
        env_phone_ip = ENVIRONMENT_CONFIG[env]
        return env_phone_ip


if __name__ == '__main__':
    print(Env_Module().get_phone_ip("all"))

