from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)


#根据document树，dom树，家谱图，找关系


# 绝对路劲，找根节点
# ctrl+f,调出框框，绝对路径，左斜杠开始/,看箭头，看显示，看缩进，倒着写
# driver.find_element_by_xpath("/html/body/div/div/div/div/form/input[1]").send_keys(123)#xpath下标从1开始，列表从0开始，div也可以加下标



# 相对路径，从中间具有特殊属性的人定位到这个人，双单引号，记得岔开，
#双左斜杠//开始

#父级找子级
# driver.find_element_by_xpath("//div[@class='schbox']/form/input[1]").send_keys(123)#xpath下标从1开始，列表从0开始，div也可以加下标

# 自己找自己
# driver.find_element_by_xpath("//input[@class='but1']").send_keys(123)

# 自己找自己，一个属性不行，可以用两个属性，三个，，，，，
# driver.find_element_by_xpath("//input[@name='key'and@class='but1']").send_keys(123)

# 通配，模糊搜索
# driver.find_element_by_xpath("//*[@name='key'and@class='but1']").send_keys(123)

#contains用法，包含关系，部分匹配，对于后边有一串数字是变化的
# driver.find_element_by_xpath("//input[contains(@placeholder,'关键字')]").send_keys(123)

# text用法
# driver.find_element_by_xpath("//a[text()='家装节']").send_keys(123)

# 儿子找爸爸
# //input[@class='but1']/../..


# 直接拷贝xpath





