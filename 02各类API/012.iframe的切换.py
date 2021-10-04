from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys                 ####键盘操作

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://mail.163.com/')
time.sleep(3)
driver.maximize_window()
time.sleep(3)



# 切换iframe
# 第一种方式
# driver.switch_to.frame('x-URS-iframe')      #有id，name，直接输入id或者name属性值，不为空，不动态变化的
# 对于属性值是变化的，后边跟一堆数字，是时间戳


# 第二种方式
# 先定位到iframe，切进去，
# dd=driver.find_element_by_xpath('//div[@id="loginDiv"]/iframe')
dd=driver.find_element_by_xpath('//iframe[contains(@id,"x-URS-iframe")]')
driver.switch_to.frame(dd)



# driver.find_element_by_xpath('//*[@data-placeholder="邮箱帐号或手机号码"]').send_keys('17472803454')


#contains用法
driver.find_element_by_xpath('//input[contains(@id,"auto-id")]').send_keys('17472803454')

#多层iframe，一层一层往里面切,搞清楚层级

# 怎么从下往上切换
driver.switch_to.parent_frame()####从子frame，切换到parent frame
driver.switch_to.default_content()###切回主文档