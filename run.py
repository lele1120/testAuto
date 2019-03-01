# -*- coding: utf-8 -*-
# @Author  : XuChen

from Common import Email, Log, Consts, Shell
from Conf import Config
import pytest

if __name__ == '__main__':
    """
    执行所有case并生成报告
    """
    conf = Config.Config()
    shell = Shell.Shell()
    log = Log.MyLog()
    log.info('初始化配置文件, path=' + conf.conf_path)
    test_run_path = conf.run_path
    xml_report_path = conf.xml_report_path
    html_report_path = conf.html_report_path

    # 定义测试集
    allure_list = '--allure_features=Home,sigin,Personal,homepage,Regression,notloggedin,bank_page,know_page'
    # allure_list = '--allure_features=know_page'
    args = ['-q', '--maxfail=3', '--alluredir', xml_report_path, allure_list]
    pytest.main(args)
    cmd = 'allure generate %s -o %s  --clean' % (xml_report_path, html_report_path)

    try:
        shell.invoke(cmd)
    except Exception:
        log.error('执行用例失败，请检查环境配置')
        raise

    test_body = Consts.TEST_LIST
    result_body = Consts.RESULT_LIST
    error_number = test_body.__len__() - result_body.__len__()

    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("运行"+str(test_body.__len__()) + "个测试用例")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("成功"+str(result_body.__len__()) + "个测试用例")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
    print("失败" + str(error_number) + "个测试用例")
    print("*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")

    if error_number > 0:
        try:
            mail = Email.SendMail()
            mail.sendMail()
        except:
            log.error('发送邮件失败，请检查邮件配置')
            raise

    elif test_body.__len__() is not 0 and error_number == 0:

        print("全部通过")

    else:

        print("小兄弟去看看代码吧")



