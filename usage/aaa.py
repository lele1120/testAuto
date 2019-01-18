# -*- coding: utf-8 -*-
#!/usr/bin/env python
import os
import smtplib
import sys
import time
from email.mime.multipart import MIMEMultipart

from Common import Log
from Common import Consts, Email

# path_dir = str(os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir)))
# print(path_dir)
# Consts.RESULT_LIST.append('True')
# result_body = Consts.RESULT_LIST
# print(result_body.__len__())

import sys



from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from Common import Consts
from Common import Log
from Conf.Config import Config


print(sys.getdefaultencoding())
print("-----------------")


config = Config()
log = Log.MyLog()
msg = MIMEMultipart()
# result_body = Consts.RESULT_LIST
body = 'Hi，all\n本次安卓UI自动化测试报告如下：\n  运行结果通过：' + str(999) + \
       "个测试用例"
mail_body = MIMEText(body.encode('utf-8'), _subtype='plain', _charset='utf-8')
tm = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
msg['Subject'] = Header("安卓UI自动化测试报告" + "_" + tm, 'utf-8').encode('utf-8')
msg['From'] = config.sender
receivers = config.receiver
toclause = receivers.split(',')
msg['To'] = ",".join(toclause)

# msg.attach(mail_body)

try:
    smtp = smtplib.SMTP()
    smtp.connect(config.smtpserver)
    smtp.login(config.username, config.password)
    smtp.sendmail(config.sender, toclause, msg.as_string())
except Exception as e:
    print(e)
    log.error("邮件发送失败，请检查邮件配置")

else:
    print("发送成功")
    log.info("邮件发送成功")
finally:
    smtp.quit()
