import time

import allure
from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotInteractableException,ElementNotSelectableException)

@pytest.mark.negative_test_case
@allure.title("Automating the CURL app")
@allure.description("checking the CURL login url page with invalid credentials.")
def test_automate_make_appointment():
    driver = webdriver.Chrome()

    # first navigate to the url
    driver.get("https://katalon-demo-cura.herokuapp.com/")

    # we have to find the element.we need to know the locators (id from the html page).
    make_appointment_element=driver.find_element(By.ID,"btn-make-appointment")
         # < a
        # id = "btn-make-appointment"
        # href = "./profile.php#login"
        #
        # class ="btn btn-dark btn-lg"
        # >
        #
        # Make Appointment
        #
        # < / a >
    # to click on the button.
    make_appointment_element.click()


    # verify the current Url on the next page
    assert driver.current_url=="https://katalon-demo-cura.herokuapp.com/profile.php#login"

    (WebDriverWait(driver=driver,timeout= 55).until(EC.visibility_of_element_located((By.XPATH,"//input[@id='txt-username']"))))

# Find and Enter the details of the username and password ( web_element.send_keys()
#     in the below one we used xpath to find the element.


#
    enter_username=driver.find_element(By.XPATH,"//input[@id='txt-username']")
    enter_username.send_keys("abc@gmail.com")

    # < label
    # for ="txt-username"
    # class ="col-sm-4 control-label"
    # > Username < / label >
    # < label
    ignore_list = [ElementNotInteractableException,ElementNotSelectableException]
    (WebDriverWait(driver=driver, poll_frequency=1, timeout=5, ignored_exceptions=ignore_list).until(
        EC.visibility_of_element_located((By.XPATH,"//input[@id='txt-password']"))))
 # for ="txt-password" class ="col-sm-4 control-label" > Password < / label >
    enter_password = driver.find_element(By.XPATH,"//input[@id='txt-password']")
    enter_password.send_keys("abc123456")



# Click on the submit button (click()
    click_button=driver.find_element(By.ID,"btn-login")
    click_button.click()
    # < button
    # id = "btn-login"
    # type = "submit"
    #
    # class ="btn btn-default"
    # data-nlok-ref-guid="f1ffe280-64bd-4957-80d6-b3c163b5b800" >
    # Login
    # < / button >
    # time.sleep(10)
    (WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,"//p[contains(text(),'Login failed! Please ensure the username and password are valid')]"))))
# verify the error message after login.
    error_message=driver.find_element(By.XPATH,"//p[contains(text(),'Login failed! Please ensure the username and password are valid')]")
    assert error_message.text=="Login failed! Please ensure the username and password are valid."
    #< p
    #
    #class ="lead text-danger"
    # > Login failed! Please ensure the username and password are valid.
    #
    # < / p >
    #


    driver.quit()



