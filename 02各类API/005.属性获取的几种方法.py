from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


# 获取控件的宽高,尺寸，字典类型，
size=driver.find_element_by_name("key").size
print(type(size))
print(size)
print(size['height'])
print(size['width'])
time.sleep(3)



#获取控件文本信息,,,,,,@property,装饰成属性方法
# 只能拿到标签夹得信息
text=driver.find_element_by_xpath('/html/body/div[1]/div/span').text
print(text)


# 拿属性对应的属性值，例如那个搜索
inputbutton=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').get_attribute('placeholder')
print(inputbutton)


# 判断控件是否已经加载,布尔类型的，TRUE，FALSE
dis=inputbutton=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').is_displayed()
print((dis))


# 回显
driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').send_keys('6454646')
text=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div[1]/form/input[1]').get_attribute('value')
print(text)