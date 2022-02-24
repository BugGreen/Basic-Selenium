from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from resolutions import screen_resolutions
from time import sleep


def define_emulation_settings(size: tuple, os: str) -> dict:
    # user_agent helps identify which browser is being used, what version, and on which operating system
    if os == 'macOS':
        user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) " \
                     "AppleWebKit/537.36 (KHTML, like Gecko) " \
                     "Chrome/98.0.4758.102 Safari/537.36"
    elif os == 'Windows':
        user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' \
                     'AppleWebKit/537.36 (KHTML, like Gecko) ' \
                     'Chrome/98.0.4758.102 Safari/537.36'
    else:
        print('OS not supported')

    screens_emulations = {
        "deviceMetrics": {"width": size[0], "height": size[1]},
        "userAgent": user_agent
    }

    return screens_emulations


def ss_saver(driver, size: tuple, os: str):
    driver.save_screenshot(f"./ss/{os}_{size[0]}x{size[1]}.png".format(os, size))


def create_emulation(size: tuple, os: str, url="https://app.saasmetrix.io/Login"):
    chrome_options = Options()
    screens_emulations = define_emulation_settings(size, os)
    chrome_options.add_experimental_option("mobileEmulation", screens_emulations)
    driver = webdriver.Chrome('chrome_driver/chromedriver 2', options=chrome_options)
    url = url
    driver.get(url)
    driver.implicitly_wait(5)  # Amount of seconds to wait to upload this website successfully

    email = driver.find_element_by_xpath("//input[@id='email']")
    email.send_keys("nicolas@saasmetrix.de")

    email = driver.find_element_by_xpath("//input[@id='password']")
    email.send_keys("Test")

    login_button = driver.find_element_by_xpath("//*[@id='submit_login']")
    login_button.click()
    sleep(3)
    ss_saver(driver, size, os)


for system, resolutions in screen_resolutions.items():
    for resolution in resolutions.values():
        print(f"🖥 Changing Resolutions to {resolution[0]}x{resolution[1]}")
        create_emulation(resolution, system)
