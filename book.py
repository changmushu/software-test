#打开清华大学出版社官网，搜索关键字python，将首页的书本名和价格提取出来，并形成一个表格
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
driver = webdriver.Chrome()     # 生成一个浏览器对象
url = "http://www.tup.tsinghua.edu.cn/index.html"      # 设置url
driver.get(url)    # 将url传给driver对象

input_tag = driver.find_element(By.CSS_SELECTOR, '#input_key')  # 使用selector来定位输入框
input_tag.send_keys("python")   # 往输入框中传递值
time.sleep(1)
input_tag.send_keys(Keys.ENTER)     # 模拟键盘的回车键

windows = driver.window_handles     # 将目前已经打开的两个网页地址保存在windows列表中
driver.switch_to.window(windows[1])     # 将driver关联的网页切换到刚刚新打开的页面
time.sleep(5)
html = driver.page_source       # 获取driver当前页面的网页源码，存储在html变量中
soup = BeautifulSoup(html, 'lxml')      # 新建一个BeautifulSoup对象，以lxml的形式解析html源码，并存到soup变量中
book_name = [i.text for i in soup.select('#csproduct a span')]  # 从soup中提取书名
editor = [i.text for i in soup.select('#csproduct a p')[::3]]   # 从soup中提取作者姓名
p = [i.text for i in soup.select('#csproduct a p')[2::3]]   # 从soup中提取书本价格
price = []  # 书本价格列表
for i in p: # 对于每一个在i，i的格式都形如“价格：83”，“价格：90“。为了后面方便生成表格，要去除数字以外的字符
    i = i.replace('定价：', '')    # 将每个元素中的‘定价：’删除
    price.append(i)     # 将每一个修改过的i，加入提前准备的price列表中

table = pd.DataFrame({'书名': book_name, '价格': price})    # 生成两列的表格，列名为书名和价格
print(table)
