# -*- coding: utf-8 -*-
# @Author  : XuChen
import os
from pathlib import Path

from Common import Log
from Conf import Config
from Common import Shell
import pytest


if __name__ == '__main__':
    """
    执行所有case并生成报告
    """
    conf = Config.Config()
    shell = Shell.Shell()
    log = Log.MyLog()
    # xml_report_path = "${WORKSPACE}/Report"
    # html_report_path = "${WORKSPACE}/Report/xml -o ${WORKSPACE}/Report/html"

    # xml_report_path = str(Path(os.path.abspath('.') + "/Report/xml"))
    # html_report_path = str(Path(os.path.abspath('.') + "/Report/xml -o " + os.path.abspath('.') +
    #                             "/Report/html --clean"))
    #
    # html_report_path = conf.xml_report_path + " -o " + conf.html_report_path + " --clean"

    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    args = ['-q', '--maxfail=3', '--alluredir', xml_report_path]
    pytest.main(args)
    cmd = 'allure generate %s -o %s  --clean' % (xml_report_path, html_report_path)

    print("-------------------------")
    print(xml_report_path)
    print("-------------------------")
    print(html_report_path)
    print("-------------------------")

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    # args = ['-q', '--maxfail=1', '--alluredir', xml_report_path]
    #
    # pytest.main(args)
    # os.system("allure generate " + html_report_path)
