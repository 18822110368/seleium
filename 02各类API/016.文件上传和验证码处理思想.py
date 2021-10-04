from selenium import webdriver#导入
import time
from selenium.webdriver.common.action_chains import ActionChains   ###移到正中央，鼠标在上边自定弹出的那种
from selenium.webdriver.common.keys import Keys                 ####键盘操作
from selenium.webdriver.support.select import Select            ###下拉选择框

driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

# driver.get('https://www.ctrip.com/?sid=155952&allianceid=4897&ouid=index')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

# 文件上传

# 链接：http://www.bcbxhome.com/bcbxxy/forum.php?mod=viewthread&tid=296&highlight=%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0
# input标签文件上传
# 带有input标签并且type属性的值为file可直接使用send_keys方法上传文件。
driver.get('http://www.bcbxhome.com/bcbxxy/home.php?mod=spacecp&ac=avatar')
driver.find_element_by_name('file').send_keys(r'G:\001.文件夹\002.机密机密机密\seleium自动化\02.相关文件及包\65456456.png')

###非input类型的，用AutoIT3，，，一般不会用到，用到就去看链接




# 验证码处理
# 链接：http://www.bcbxhome.com/bcbxxy/forum.php?mod=viewthread&tid=295&highlight=%E9%AA%8C%E8%AF%81%E7%A0%81%E5%A4%84%E7%90%86

# 像这种滑块和手机验证码的情况下，无法通过正常办法是没有办法进行处理，那么 一般对这种处理有以下几种思路：
# 1、       通过接口请求，拿到对应验证码信息
# 2、       让开发配合把验证码搞成万能验证码
# 3、       注入cookies

