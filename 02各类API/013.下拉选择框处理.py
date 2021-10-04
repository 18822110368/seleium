from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys                 ####键盘操作
from selenium.webdriver.support.select import Select            ###下拉选择框

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


#房间数，一右击就消失，下拉选择框，没办法直接定位
#用select类定义它
# 类的（参数），参数会传到类的--init--方法

s=driver.find_element_by_xpath('//*[@id="J_roomCountList"]')
# Select(s).select_by_visible_text('2间')    ##可见的文本信息，标签中间夹的文本信息

Select(s).select_by_index(3)             ###索引，是从0开始，，和xpath不一样，不要搞混
#
# Select(s).select_by_value('5')             ###值

# 对于不是select标签的，表格形式的，不能使用select类
