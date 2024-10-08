import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 指定 ChromeDriver 的路径
service = ChromeService(executable_path="/Users/zhanggong/devTools/chromedriver-mac-arm64/chromedriver")

# 创建 Chrome WebDriver 实例
driver = webdriver.Chrome(service=service)

# 访问百度首页
driver.get("http://www.google.com")

# 等待页面加载完成
wait = WebDriverWait(driver, 10)  # 设置最长等待时间为 10 秒
wait.until(EC.presence_of_element_located((By.ID, 'APjFqb')))

# 接下来可以执行其他操作
# 例如查找元素并输入文本
input = driver.find_element(By.ID, 'APjFqb')
input.send_keys("canglaoshi")

# 查找搜索按钮并点击
button = driver.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[4]/center/input[1]')
button.click()

# 等待
time.sleep(1000)
# 你可以在这里添加更多操作，例如等待页面加载完成、获取搜索结果等
