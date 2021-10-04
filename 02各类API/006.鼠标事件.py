from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

# driver.get('http://101.133.169.100/yuns/index.php')
# time.sleep(3)
# driver.maximize_window()
# time.sleep(3)
#
# # 移到这里，执行动作
# ele=driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[2]/dt/div/span/a')
# time.sleep(3)
#
# ActionChains(driver).move_to_element(ele).perform()
# #这里的driver会传到--init--类的初始化方法，，
# # ，self，类的实例化对象，做成全部变量，局部变量只能该方法用
# time.sleep(3)
#
# # 点击
# driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/dl[2]/div/div[2]/div/a').click()
#
#
# ActionChains(driver).context_click(ele).perform()#右击
# ActionChains(driver).double_click().perform()#双击





# 拖拽

driver.get('https://www.huodongxing.com/')
time.sleep(3)
driver.maximize_window()
time.sleep(3)
driver.find_element_by_xpath('/html/body/section/header/div/ul/li[1]/a[1]').click()
time.sleep(3)

driver.find_element_by_xpath('//*[@id="geetest_captcha"]/div/div[2]/div[1]/div[3]/span[1]').click()
time.sleep(3)

source=driver.find_element_by_xpath('/html/body/div[5]/div[2]/div[1]/div/div[1]/div[2]/div[2]')
ActionChains(driver).drag_and_drop_by_offset(source,62,0).perform()#source形参，可以随便起名字,拖多少，猜，要么看占比，
















