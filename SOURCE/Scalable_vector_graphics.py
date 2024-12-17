import allure
import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@allure.title("SVG")
@allure.description("checking the simple SVG and complex SVG ")

def test_find_SVG():
    drivers = webdriver.Chrome()
    drivers.get("https://www.flipkart.com/")
    element = drivers.find_element(By.NAME,"q")
    element.send_keys("macmini")

    list_svg = drivers.find_elements(By.XPATH,"//*[name()='svg']")
    list_svg[0].click()



def test_verify_svg():
    drivers = webdriver.Chrome()
    drivers.get("https://www.amcharts.com/svg-maps/?map=india")

    #time.sleep(5) // * [name() = 'svg'] / *[name() = 'g'][7] / * [name() = 'g'] / *[name() = 'g'] / *[name() = 'path']

    list_states = drivers.find_elements(By.XPATH,"//*[name()='svg']/*[name()='g'][7]/*[name()='g']/*[name()='g']/*[name()='path']")
    for state in list_states:
        print(state.get_attribute("aria-label"))
        if "Andhra Pradesh" in state.get_attribute("aria-label"):
            state.click()
            break

    time.sleep(5)