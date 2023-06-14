from selenium.webdriver.common.by import By
from selenium import webdriver
import time
driver = webdriver.Chrome() # 启动浏览器
driver.get("http://101.34.221.219:8010/") # 1
el = driver.find_element(By.LINK_TEXT, "登录") #
el.click() # 3

el = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[1]/input") # 4
el.send_keys("stone") # 5
el = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[2]/div/input")
el.send_keys("123456") # 7
el = driver.find_element(By.XPATH,"/html/body/div[4]/div/div[2]/div[2]/div/div/div[1]/form/div[3]/button")
el.click()
time.sleep(10)
el = driver.find_element(By.ID,"search-input")
el.send_keys("连衣裙")

el = driver.find_element(By.ID,"ai-topsearch")
el.click()
time.sleep(10)
driver.quit() # 关闭浏览器
