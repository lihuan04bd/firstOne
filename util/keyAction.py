from selenium import webdriver
# 元素等待
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
#下拉框专门处理
from selenium.webdriver.support.ui import Select
#键盘操作
from selenium.webdriver.common.keys import Keys
import time

# 获取和webdriver 的会话
driver = webdriver.Chrome()

driver.get("https://www.baidu.com/")

ele = "//input[@class='s_ipt']"
# driver.find_element_by_xpath(ele).send_keys("京东")
# driver.find_element_by_xpath(ele).send_keys(Keys.ENTER)
driver.find_element_by_xpath(ele).send_keys("京东",Keys.ENTER)
windows = driver.window_handles

#元素操作带来的页面元素变化 一定要等
ele_jd = '//a[@ourl="http://www.jd.com/"]'

WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,ele_jd)))

# time.sleep(10)
# EC.presence_of_element_located


driver.find_element_by_xpath(ele_jd).click()
time.sleep(5)
windows = driver.window_handles

# print(driver.current_window_handle)
driver.switch_to.window(windows[-1])
login_a = '//a[@class="link-login"]'

WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,login_a)))
driver.find_element_by_xpath(login_a).click()


log = "//span[text()='QQ']"

WebDriverWait(driver,10,0.5).until(EC.visibility_of_element_located((By.XPATH,log)))
driver.find_element_by_xpath(log).click()

qq_log = '//a[text()="帐号密码登录"]'


driver.maximize_window()

ifram_id = "ptlogin_iframe"

driver.switch_to.frame("ptlogin_iframe")


try:
  WebDriverWait(driver,10, 0.5).until(EC.visibility_of_element_located((By.XPATH, qq_log)))
  ele  = driver.find_element_by_xpath(qq_log).click()
except Exception as e:
    file_path = "aa.png"
    driver.save_screenshot(file_path)
    raise e

logname = '//input[@name="u"]'
logpw = '//input[@name="p"]'
logbtn = '//input[@class="btn"]'

WebDriverWait(driver,10, 0.5).until(EC.visibility_of_element_located((By.XPATH, logname)))
driver.find_element_by_xpath(logname).send_keys("763117428")
driver.find_element_by_xpath(logpw).send_keys("lihuan850208")
driver.find_element_by_xpath(logbtn).click()

jdLoginName = '//input[@name="loginname"]'
jdLoginPwd = '//input[@name="loginpwd"]'
button_l = '//button[@id="form-register"]'
WebDriverWait(driver,10, 0.5).until(EC.visibility_of_element_located((By.XPATH, jdLoginName)))
driver.find_element_by_xpath(jdLoginName).send_keys("18513900971")
driver.find_element_by_xpath(jdLoginPwd).send_keys("lihuan763117428")
driver.find_element_by_xpath(button_l).click()