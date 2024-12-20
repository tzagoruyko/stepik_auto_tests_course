import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/find_link_text"

browser = webdriver.Chrome()
browser.get(link)

continue_link = browser.find_element(By.LINK_TEXT, '224592')
continue_link.click()

textarea = browser.find_element(By.NAME, "first_name")
textarea.send_keys("Tatyana")

textarea = browser.find_element(By.NAME, "last_name")
textarea.send_keys("Zagoruyko")

textarea = browser.find_element(By.NAME, "firstname")
textarea.send_keys("Volgograd")

textarea = browser.find_element(By.ID, "country")
textarea.send_keys("Russia")

submit_button = browser.find_element(By.CSS_SELECTOR, ".btn")
submit_button.click()
time.sleep(10)
browser.quit()