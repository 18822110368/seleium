from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

# driver.get('http://101.133.169.100/yuns/index.php')
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
# driver.find_element_by_name("key").send_keys(123)
# time.sleep(3)
# driver.find_element_by_class_name('but2').click()


driver.get('https://www.baidu.com/')
driver.find_element_by_class_name('s_btn').click()
#class中间有空格的，叫复合类，不建议用class定位，会报错：selenium.common.exceptions.NoSuchElementException: Message: Unable to locate element: .bg s_btn
#对于这种可以只传一般，进行定位，但是可能会存在重复

