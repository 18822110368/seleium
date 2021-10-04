from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://www.baidu.com/')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


#弹窗，，鼠标右击弹不出元素
# 三种形态

# 输入内容
driver.switch_to.alert.send_keys('dffd')

# 接收，正面的
driver.switch_to.alert.accept()

#取消，负面的
driver.switch_to.alert.dismiss()


#打印alert_文本
print(driver.switch_to.alert.text)