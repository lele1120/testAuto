from biz.get_value_by_yaml import Get_Value_By_Yaml
import uiautomator2 as u2

# wifi = Get_Value_By_Yaml().get_value("Y66手机ip")
# driver = u2.connect_wifi(wifi)
driver = u2.connect_usb("d5ddd4f7")
print(driver.info)