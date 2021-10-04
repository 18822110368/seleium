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


# 普通时间控件
ele=driver.find_element_by_xpath('//*[@id="HD_CheckIn"]')
ele.clear()
ele.send_keys('2021-10-02')    ###按时间格式输入




#特殊时间控件，readonly，，，用js移除属性
# 链接：http://www.bcbxhome.com/bcbxxy/forum.php?mod=viewthread&tid=297&highlight=%E6%97%B6%E9%97%B4%E6%8E%A7%E4%BB%B6

js="document.getElementById('noticeEndTime').removeAttribute('readonly')"
js="document.getElementsByName('noticeEndTime')[0].removeAttribute('readonly')"     #在js中，name要用elements
js="document.getElementsByTagName('input')[0].removeAttribute('readonly')"           #在js中，tagname要用elements

driver.execute_script(js)

driver.find_element_by_name("noticeEndTime").send_keys('2021-06-21 10:52:24')