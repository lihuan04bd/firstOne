# 可见区域范围内才能操作
#如果不可见 需要拖动到页面的可见区域范围内
# 页面存在 并且在可见范围区域分为内
#selenium 没有提供拖动到指定区域的范围 用js处理

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
driver.find_element_by_xpath('//input[@name="wd"]').send_keys("京东",Keys.ENTER)
time.sleep(3)
ele = driver.find_element_by_xpath('//a[text()="京东开店流程及费用"]')

driver.execute_script("arguments[0].scrollIntoView();",ele)
# 再对元素进行操作
# driver.execute_async_script()
print(ele.tag_name)
# 元素查找 有id 先用id，缩小查找范围，然后再找里面的元素，提高查找元素的
# 优先使用visibility_of_element_located  visibility_of_element_located不行的时候 使用presence_of_element_located
ele.click()

