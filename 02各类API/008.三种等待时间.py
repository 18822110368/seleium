from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


#强制等待时间，，线程休眠，代码停止，只是相邻的
time.sleep(3)


from time import sleep
sleep()


#隐式等待时间，
# 超时时间，最大等待10秒，实际3秒，，效率高,,,全局的，，打破全局性，就终止了，
# 弊端，跳转前后可能通过xpath定位，前后界面有相同xpath，加载慢，还没跳转，直接在原来界面找到控件了。会继续执行

driver.implicitly_wait(10)




# 显式等待时间

from selenium.webdriver.support.ui import WebDriverWait         #用的WebDriverWait 中的方法
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

ele=WebDriverWait(driver,15,0.5).until(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/form/input[1]')))
ele=WebDriverWait(driver,15,0.5).until_not(EC.presence_of_element_located((By.XPATH,'/html/body/div[2]/div/div[2]/div[1]/form/input[1]')))
#场景，新页面没有了旧页面的控件
ele.send_keys('123456')