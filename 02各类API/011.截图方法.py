from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys                 ####键盘操作

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://www.baidu.com/')
time.sleep(3)
driver.maximize_window()
time.sleep(3)



# 截图,路径+名称+后缀
driver.get_screenshot_as_file(r'G:\001.文件夹\002.机密机密机密\seleium自动化\02.相关文件及包\65456456.png')###r转译符