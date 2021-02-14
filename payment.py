from selenium import webdriver
import time
driver = webdriver.Chrome()
try:
  driver.get('http://automationpractice.com/index.php')
  time.sleep(3.0)
  driver.close()
except print("cant get link "):
    time.sleep(3.0)
    driver.close()

