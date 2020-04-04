from selenium import webdriver
# 元素等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

from selenium.webdriver.common.action_chains import ActionChains
#下拉框专门处理
from selenium.webdriver.support.ui import Select
#键盘操作
from selenium.webdriver.common.keys import Keys
import time

# 获取和webdriver 的会话
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")
driver.maximize_window()
actionChains = ActionChains(driver)

shezhi = driver.find_element_by_xpath('//div[@id="u1"]//a[@name="tj_settingicon"]')
time.sleep(3)
actionChains.move_to_element(shezhi).perform()
time.sleep(3)
ele = '//a[text()="高级搜索"]'
driver.find_element_by_xpath(ele).click()
select_name = driver.find_element_by_name('ft')
time.sleep(2)
# Select(select_name).all_selected_options
Select(select_name).select_by_index(2)
time.sleep(2)
Select(select_name).select_by_value("rtf")
time.sleep(2)
Select(select_name).select_by_visible_text("所有网页和文件")
