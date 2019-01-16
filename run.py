# -*- coding: utf-8 -*-
# @Author  : XuChen
import os
from pathlib import Path

import pytest

if __name__ == '__main__':
    """
    执行所有case并生成报告
    """

    xml_report_path = "${WORKSPACE}/report"
    html_report_path = "${WORKSPACE}/report/xml -o ${WORKSPACE}/report/html"

    # xml_report_path = str(Path(os.path.abspath('.') + "/report/xml"))
    # html_report_path = str(Path(os.path.abspath('.') + "/report/xml -o " + os.path.abspath('.') +
    #                             "/report/html --clean"))

    args = ['-q', '--maxfail=1', '--alluredir', xml_report_path]

    pytest.main(args)
    os.system("allure generate " + html_report_path)
