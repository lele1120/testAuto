
# @Author  : XuChen
# encoding=utf8

from Common import Log
from Conf import Config
from Common import Shell
import pytest
from Common import Email


if __name__ == '__main__':
    """
    执行所有case并生成报告
    """
    conf = Config.Config()
    shell = Shell.Shell()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)

    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    allure_list = '--allure_features=Home'

    args = ['-q', '--maxfail=3', '--alluredir', xml_report_path, allure_list]
    pytest.main(args)
    cmd = 'allure generate %s -o %s  --clean' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    try:
        mail = Email.SendMail()
        mail.sendMail()
    except:
        log.error('发送邮件失败，请检查邮件配置')
        raise


