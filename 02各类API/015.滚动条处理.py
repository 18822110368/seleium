from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains   ###移到正中央，鼠标在上边自定弹出的那种
from selenium.webdriver.common.keys import Keys                 ####键盘操作
from selenium.webdriver.support.select import Select            ###下拉选择框

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

#给一个很大的值，会滚动到底部，可以给一个小值
js='var q=document.documentElement.scrollTop=10000'
driver.execute_script(js)

time.sleep(3)
#窗体的滚动方法,
#移到窗体的几分之一，
driver.execute_script("window.scrollTo(0,document.body.scrollHeight*0.5)")   ###到哪里,,,用得少，尽量减少二次操作
time.sleep(3)

driver.execute_script("window.scrollTo(0,1500)")   ###到哪里,,,用得少，尽量减少二次操作
time.sleep(3)

#相对当前坐标移动，偏移多少
driver.execute_script('window.scrollBy(0,-200)')       ####偏移多少，上下，正负

