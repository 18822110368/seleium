from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)


# 窗体最大化
driver.maximize_window()
time.sleep(3)


#设置分辨率
driver.set_window_size(1200,800)

