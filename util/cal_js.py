from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()

driver.get("https://www.12306.cn/")
driver.maximize_window()
time.sleep(2)
driver.find_element_by_id("fromStationText").clear()
time.sleep(2)
driver.find_element_by_id("fromStationText").send_keys("北京",Keys.ENTER)
time.sleep(2)
driver.find_element_by_id("toStationText").clear()
time.sleep(2)
driver.find_element_by_id("toStationText").send_keys("沙河市",Keys.ENTER)
time.sleep(2)
driver.execute_script('var mm = document.getElementById("train_date");mm.readOnly = false;mm.value="2020-03-30"')
time.sleep(2)
driver.find_element_by_id("search_one").click()