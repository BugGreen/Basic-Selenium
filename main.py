from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome('/Users/nicolasrojasbernal/selenium_drivers/chromedriver 2')

url = "https://testpages.herokuapp.com/styled/index.html"
driver.get(url)
driver.implicitly_wait(3)  # Amount of seconds to wait to upload this website successfully
my_element = driver.find_element_by_id("progressbars")  # This is just an object, to make actions with it
my_element.click()

# Explicit way to wait for some time until one condition is achieved
WebDriverWait(driver, 15).until(
    EC.text_to_be_present_in_element(
        (By.ID, "status"),
        "Stopped"
    )
)
