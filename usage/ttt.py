import time

from test_case.get_test_value_by_yaml import get_driver_by_key

d = get_driver_by_key("Y66手机udid")   # 输入手机udid启动
d.set_fastinput_ime(True)
d.session("com.bs.finance")
time.sleep(1)
d(resourceId="com.bs.finance:id/rl_1").click()
d(resourceId="com.bs.finance:id/tv_bank_name", text=u"梅州客商银行").click()
d(resourceId="com.bs.finance:id/tv_name", text=u"周周利1号1030").click()
d(resourceId="com.bs.finance:id/tv_buy").click()

d(resourceId="com.bs.finance:id/btn_doMoney").click()  # 充值
d(resourceId="com.bs.finance:id/et_recharge_money").set_text("10000")
d(resourceId="com.bs.finance:id/btn_get_code").click()  # 获取验证码
time.sleep(2)
d(resourceId="com.bs.finance:id/et_open_code").set_text("666666")
d(resourceId="com.bs.finance:id/btn_recharge").click()

time.sleep(2)
for i in range(2):
    d(resourceId="com.bs.finance:id/btn_ok").click()
    d(resourceId="com.bs.finance:id/tv_banlance_mx").click()
    d(text=u"充值").click()
    d(resourceId="com.bs.finance:id/et_recharge_money").set_text("10000")
    d(resourceId="com.bs.finance:id/btn_get_code").click()  # 获取验证码
    time.sleep(2)
    d(resourceId="com.bs.finance:id/et_open_code").set_text("666666")
    d(resourceId="com.bs.finance:id/btn_recharge").click()
    time.sleep(2)

