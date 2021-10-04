from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://www.baidu.com/')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="kw"]').send_keys('123')
driver.find_element_by_xpath('//*[@id="su"]').click()

print(driver.window_handles)

time.sleep(3)

driver.find_element_by_xpath('//*[@id="1"]/h3/a[1]').click()
time.sleep(3)


# 窗体的句柄或者说焦点
print(driver.window_handles)
time.sleep(3)
print(driver.current_window_handle)
time.sleep(3)

driver.switch_to.window(driver.window_handles[1])####   从0开始，，这里是window，不是windows
time.sleep(3)

print(driver.current_window_handle)


driver.close()####把当前句柄所在的页面关掉

driver.quit()###关掉所有，退出；浏览器
