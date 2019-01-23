# testAuto

基于Pytest+uiautomator2+Allure的安卓UI自动化开源框架

模块类的设计

Assert.py封装断言方法

Consts.py全局变量定义

Email.py封装smtplib方法，运行结果发送邮件通知

Operat.py封住app点击，文本框输入文字，截图方法

Config.py读取配置文件，包裹：不同环境的配置，email的相关配置

Param.py 封装yaml数据方法

conftest.py控制pytest.fixture，控制脚本运行逻辑

run.py核心代码。定义并执行测试用例集，生成测试报告发送邮件
