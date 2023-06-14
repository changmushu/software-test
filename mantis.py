from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome() # 启动浏览器
driver.get("http://localhost/mantis/login_page.php") # 1
time.sleep(3)
el = driver.find_element(By.ID,"username") # 4
el.send_keys("administrator") # 5
time.sleep(3)
el = driver.find_element(By.XPATH,"/html/body/div/div/div/div/div/div[4]/div/div/div[1]/form/fieldset/input[2]")
el.click() # 3
time.sleep(3)
el = driver.find_element(By.ID,"password")
el.send_keys("root") # 7
time.sleep(3)
el = driver.find_element(By.XPATH, "/html/body/div/div/div/div/div/div[4]/div/div/div/form/fieldset/input[3]") #
el.click() # 3
time.sleep(3)
driver.quit() # 关闭浏览器