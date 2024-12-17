import allure
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

import time

@allure.title("Automating the awesome QA")
@allure.description("automating the html elements")
def test_html_elements():
    driver = webdriver.Chrome()
    # first navigate to the url
    driver.get("https://awesomeqa.com/practice.html")

    first_name = driver.find_element(By.XPATH,"//input[@name='firstname']")
    first_name.send_keys("Minion")

    last_name = driver.find_element(By.XPATH,"//input[@name='lastname']")
    last_name.send_keys("Bow")

    gender = driver.find_element(By.ID,"sex-0")
    gender.click()

    experience = driver.find_element(By.ID,"exp-2")
    experience.click()

    date = driver.find_element(By.ID, "datepicker")
    date.send_keys("12/14/2024")

    profession = driver.find_element(By.XPATH,"//input[@id = 'profession-1']")
    profession.click()

    tools = driver.find_element(By.XPATH,"//input[@id = 'tool-2']")
    tools.click()


    time.sleep(3)

