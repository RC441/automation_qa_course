from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("user-data-dir=C:\\profile")
driver = webdriver.Chrome(options)
driver.get("https://google.com")
time.sleep(120)