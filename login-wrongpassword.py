
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()
try:
  driver.get('http://automationpractice.com/index.php')
  time.sleep(3.0)
  

except print("cant get link "):
    time.sleep(3.0)
    driver.close()

driver.get("http://automationpractice.com/index.php?controller=authentication&back=my-account")
time.sleep(2.0)
driver.find_element(By.ID, 'email').send_keys('test_1@email.com')
driver.find_element(By.ID, 'passwd').send_keys('tester_2')
time.sleep(2.0)
driver.find_element(By.ID , "SubmitLogin").click()
driver.close()
