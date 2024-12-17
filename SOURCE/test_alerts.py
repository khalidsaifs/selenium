import time

import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

@allure.title("checking the JS Alert")
@allure.description("learing the different allerts")
def test_alert():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    (WebDriverWait(driver=drivers,timeout=10).until(EC.visibility_of_element_located((By.XPATH,"//div[@class='example']"))))

    element_alert = drivers.find_element(By.XPATH, "//button[@onclick='jsAlert()']")
    element_alert.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    time.sleep(5)
    alert = drivers.switch_to.alert
    alert.accept()

    time.sleep(5)

    element_result = drivers.find_element(By.ID,'result').text
    assert element_result == "You successfully clicked an alert"

    time.sleep(5)

def test_dismiss_confirm():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    element_confirm = drivers.find_element(By.XPATH, "//button[@onclick ='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    alert=drivers.switch_to.alert
    alert.dismiss()

    element_result = drivers.find_element(By.ID,"result").text
    assert element_result == "You clicked: Cancel"

    time.sleep(5)

def test_ok_confirm():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    element_confirm = drivers.find_element(By.XPATH, "//button[@onclick ='jsConfirm()']")
    element_confirm.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    alert=drivers.switch_to.alert
    alert.accept()

    element_result = drivers.find_element(By.ID,"result").text
    assert element_result == "You clicked: Ok"

    time.sleep(5)

def test_accept_prompt():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    element_confirm = drivers.find_element(By.XPATH, "//button[@onclick ='jsPrompt()']")
    element_confirm.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    alert=drivers.switch_to.alert
    alert.send_keys("saif")
    alert.accept()


    element_result = drivers.find_element(By.ID,"result").text
    assert element_result == "You entered: saif"

    time.sleep(5)

def test_cancel_prompt():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    element_confirm = drivers.find_element(By.XPATH, "//button[@onclick ='jsPrompt()']")
    element_confirm.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    alert=drivers.switch_to.alert
    alert.send_keys("saif")
    alert.accept()


    element_result = drivers.find_element(By.ID,"result").text
    assert element_result == "You entered: null"

    time.sleep(5)

def test_cancel_prompt_neg():
    drivers = webdriver.Chrome()
    drivers.get("https://the-internet.herokuapp.com/javascript_alerts")
    drivers.maximize_window()

    element_confirm = drivers.find_element(By.XPATH, "//button[@onclick ='jsPrompt()']")
    element_confirm.click()

    WebDriverWait(driver=drivers, timeout=10).until(EC.alert_is_present())

    alert=drivers.switch_to.alert
    alert.dismiss()


    element_result = drivers.find_element(By.ID,"result").text
    assert element_result == "You entered: null"

    time.sleep(5)

