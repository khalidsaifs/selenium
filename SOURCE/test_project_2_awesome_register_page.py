from selenium import webdriver
import time
import allure
import pytest
from selenium.webdriver.common.by import By

@pytest.mark.Positive
@allure.title("Automation for the Registration Page of the AwesomeQA.com/UI")
@allure.description("Automating the registration page using faker and verifying the next page")
def test_automating_awesome_qa():
    # It opens the URL
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # verify the register page.
    register_page = driver.find_element(By.XPATH,"//h1[contains(text(),'Register Account')]")
    assert register_page.text == "Register Account"

    # Fill the form

    # 1. fill the firstname
    enter_username = driver.find_element(By.XPATH,"//input[@name='firstname']")
    enter_username.send_keys("Karly")

    # 2.fill the lastname
    enter_lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    enter_lastname.send_keys("Wells")

    # 3.fill the email
    enter_email = driver.find_element(By.XPATH, "//input[@name='email']")
    enter_email.send_keys("mecoparewi@mailinator.com")
    # 4.fill the telephone
    enter_telephone = driver.find_element(By.XPATH, "//input[@name='telephone']")
    enter_telephone.send_keys("+1 (332) 573-6367")
    # 5.fill the Password
    enter_password = driver.find_element(By.XPATH, "//input[@name='password']")
    enter_password.send_keys("1234567890")
    # 6.fill the confirm_Password
    enter_confirm_password = driver.find_element(By.XPATH, "//input[@name='confirm']")
    enter_confirm_password.send_keys("1234567890")
    time.sleep(10)

    # 7.click the continue_button
    continue_button = driver.find_element(By.XPATH, "//input[@class='btn btn-primary']")
    continue_button.click()

    time.sleep(5)

    # verifying the next page
    created_page = driver.find_element(By.XPATH, "//h1[contains(text(),'Your Account Has Been Created!')]")
    assert created_page.text == "Your Account Has Been Created!"

    time.sleep(5)
    # driver.quit()
@pytest.mark.negative
# @allure.title("Automation for the Registration Page of the AwesomeQA.com/UI")
@allure.description("Automating the registration page using existing id and verifying the error message")
def test_automating_awesome_qa_n():
    # It opens the URL
    driver = webdriver.Chrome()
    driver.get("https://awesomeqa.com/ui/index.php?route=account/register")

    # verify the register page.
    register_page = driver.find_element(By.XPATH,"//h1[contains(text(),'Register Account')]")
    assert register_page.text == "Register Account"

    # Fill the form

    # 1. fill the firstname
    enter_username = driver.find_element(By.XPATH,"//input[@name='firstname']")
    enter_username.send_keys("Karly")

    # 2.fill the lastname
    enter_lastname = driver.find_element(By.XPATH, "//input[@name='lastname']")
    enter_lastname.send_keys("Wells")

    # 3.fill the email
    enter_email = driver.find_element(By.XPATH, "//input[@name='email']")
    enter_email.send_keys("mecoparewi@mailinator.com")
    # 4.fill the telephone
    enter_telephone = driver.find_element(By.XPATH, "//input[@name='telephone']")
    enter_telephone.send_keys("+1 (332) 573-6367")
    # 5.fill the Password
    enter_password = driver.find_element(By.XPATH, "//input[@name='password']")
    enter_password.send_keys("1234567890")
    # 6.fill the confirm_Password
    enter_confirm_password = driver.find_element(By.XPATH, "//input[@name='confirm']")
    enter_confirm_password.send_keys("1234567890")
    time.sleep(10)

    # 7.click the continue_button
    continue_button = driver.find_element(By.XPATH, "//input[@class='btn btn-primary']")
    continue_button.click()

    time.sleep(10)

    # verifying the error page
    error_page = driver.find_element(By.XPATH, "//div[@class='alert alert-danger alert-dismissible']")
    assert error_page.text == "Warning: E-Mail Address is already registered!"

    time.sleep(6)
    driver.quit()

