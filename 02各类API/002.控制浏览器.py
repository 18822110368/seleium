from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_partial_link_text('联系客服').click()
time.sleep(3)

# 刷新
driver.refresh()
time.sleep(3)

# 回退
driver.back()
time.sleep(3)

# 前进
driver.forward()

