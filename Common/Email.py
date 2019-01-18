# -*- coding: utf-8 -*-
# @File    : Email.py

"""
封装发送邮件的方法

"""
import smtplib
import sys
import time
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

from Common import Consts
from Common import Log
from Conf.Config import Config


class SendMail:

    def __init__(self):
        self.config = Config()
        self.log = Log.MyLog()

    def sendMail(self):
        msg = MIMEMultipart()
        test_body = Consts.TEST_LIST
        result_body = Consts.RESULT_LIST
        error_number = test_body.__len__()-result_body.__len__()
        body = 'Hi，all\n本次安卓UI自动化测试报告如下：\n本次测试运行：' + str(test_body.__len__()) + '个测试用例 \n运行结果通过：' \
               + str(result_body.__len__()) + '个测试用例 \n未通过的测试用例：' + str(error_number) + '个'
        mail_body = MIMEText(body, _subtype='plain', _charset='utf-8')
        tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
        msg['Subject'] = Header("安卓UI自动化测试报告"+"_未通过用例" + str(error_number) + '个_' + tm, 'utf-8')
        msg['From'] = self.config.sender
        receivers = self.config.receiver
        toclause = receivers.split(',')
        msg['To'] = ",".join(toclause)

        msg.attach(mail_body)

        try:
            smtp = smtplib.SMTP()
            smtp.connect(self.config.smtpserver)
            smtp.login(self.config.username, self.config.password)
            smtp.sendmail(self.config.sender, toclause, msg.as_string())
        except Exception as e:
            print(e)
            print("发送失败")
            self.log.error("邮件发送失败，请检查邮件配置")

        else:
            print("发送成功")
            self.log.info("邮件发送成功")
        finally:
            smtp.quit()

