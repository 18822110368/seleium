from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_link_text('优惠券').click()
#a标签，超链接标签，href属性，属性值是一个可跳转的链接地址
#a标签中间夹的文本信息

