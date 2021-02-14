
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

# select women catergory
driver.find_element_by_link_text('Women').click()
time.sleep(2.0)
# add to cart
driver.get('http://automationpractice.com/index.php?controller=cart&add=1&id_product=1')
# checkout order
driver.find_element_by_link_text('Proceed to checkout').click()
# insert email
driver.find_element(By.ID, 'email').send_keys('test_2@mail.com')
driver.find_element(By.ID, 'passwd').send_keys('tester_2')
# time.thread_time_ns(2)
driver.find_element(By.ID , "SubmitLogin").click()
# checkout order
driver.find_element(By.NAME, "processAddress").click()
# untick the check box and proceed to nextpage 
# expected unable to perform nextpage
driver.find_element(By.NAME, "processCarrier").click()

driver.quit()
