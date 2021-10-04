from selenium import webdriver#导入
import time
driver = webdriver.Chrome()#初始化对象，调用webdriver里面的方法

driver.get('http://101.133.169.100/yuns/index.php')
time.sleep(3)
driver.maximize_window()
time.sleep(3)

# driver.find_element_by_css_selector()
# css_selector就是css选择器，和xpath思想一致

# 绝对路径
# driver.find_element_by_css_selector('hmtl>body>div>div>div>div>form>input')


# 相对路径
# 特殊类型，，，有id属性值，直接标签+#+属性值    i#cart_num    #cart_num
# driver.find_element_by_css_selector('i#cart_num')

# 特殊类型，class，直接标签+.+属性值     input.but1


# 通用写法
# input[placeholder='请输入你要查找的关键字'],,,,,,也可以不写标签类型，，，，，与xpath区别，，无//，无@
# input[class='but1'][name='key']

# 父级定位input
# div.schbox>form>input:nth-child(1)
# div.schbox>form>input:first-child
# div.schbox>form>input:last-child
# div.schbox>form>input:nth-last-child(2)倒数第二个


# 子级找父级，找不了

#xpath是把相同标签类型一起排序
#css是把不同标签一起排序

# 也可以定位
