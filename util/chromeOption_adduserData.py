# Chrome() 默认打开一个非常干净的浏览器
#如果想要添加浏览器中的缓存信息中的用户名和密码 可以通过
# ChromeAtion 类中的 add_agrument()函数增加
from selenium import webdriver
# from selenium.webdriver import ChromeOptions
chomeOptions = webdriver.ChromeOptions()
chomeOptions.add_argument("--user--data-dir=")
driver = webdriver.Chrome()