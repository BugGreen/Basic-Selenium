from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/nicolasrojasbernal/selenium_drivers/chromedriver 2')

url = "https://testpages.herokuapp.com/styled/basic-html-form-test.html"
driver.get(url)
driver.implicitly_wait(3)  # Amount of seconds to wait to upload this website successfully

user_name = driver.find_element_by_name('username')
password = driver.find_element_by_name('password')

user_name.send_keys('BugGreen')
password.send_keys('12345')

submit_btn = driver.find_element_by_css_selector('input[value="submit"]')  # Filter using css.
submit_btn.click()
