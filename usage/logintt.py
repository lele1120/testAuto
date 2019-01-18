# 登录
import time

from TestCase.test_sidebar import get_driver_by_key

d = get_driver_by_key("Y66手机udid")   # 输入手机udid启动  调试 在侧边栏进行各种操作
d(resourceId="com.bs.finance:id/tv_gologin").click()
d(resourceId="com.bs.finance:id/et_phone").set_text("13911645993")
d(resourceId="com.bs.finance:id/get_msg_code").click()
time.sleep(2)
d(resourceId="com.bs.finance:id/et_msg_code").set_text("1234")
d(resourceId="com.bs.finance:id/btn_submit").click()
d(resourceId="com.bs.finance:id/et_msg_code").set_text("123456")
d(resourceId="com.bs.finance:id/btn_login").click()
# time.sleep(2)