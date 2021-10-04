from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

# 输入内容，要先定位
driver.find_element_by_name("key").send_keys(123)
time.sleep(3)

# 清空
driver.find_element_by_name("key").clear()

# 点击，click()

