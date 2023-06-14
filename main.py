from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# 使用headless无界面浏览器模式
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')

# 启动浏览器，获取网页源代码
browser = webdriver.Chrome(options=chrome_options)
mainUrl = "https://www.taobao.com/"
browser.get(mainUrl)
print(f"browser text = {browser.page_source}")
browser.quit()
