from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


#输入王麻子，删除一个字，回车，等
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys('女装')
time.sleep(3)


# 回车
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.ENTER)
time.sleep(3)

#空格按键
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.SPACE)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.SPACE)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.SPACE)
time.sleep(3)

#退格
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.BACK_SPACE)
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.BACK_SPACE)
time.sleep(3)


#全选，复制，粘贴
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.CONTROL,'a')
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.CONTROL,'c')
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').click()
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.CONTROL,'v')
time.sleep(3)

driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys(Keys.ENTER)