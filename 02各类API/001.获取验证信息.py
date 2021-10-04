from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()

# @property，装饰器，装饰了某个属性方法，不用加括号，


# 获取表头
title=driver.title
print(title)



# 获取当前URL信息
driver.find_element_by_partial_link_text('联系客服').click()
url=driver.current_url
print(url)


title=driver.title
print(title)








