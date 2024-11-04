# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestNegativetestcase():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_negativetestcase(self):
    self.driver.get("https://katalon-demo-cura.herokuapp.com/")
    self.driver.set_window_size(1552, 832)
    self.driver.find_element(By.ID, "btn-make-appointment").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-sm-8:nth-child(2) > .input-group > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-sm-8:nth-child(2) > .input-group > .form-control").click()
    self.driver.find_element(By.CSS_SELECTOR, ".col-sm-8:nth-child(2) > .input-group > .form-control").click()
    self.driver.find_element(By.ID, "txt-username").click()
    self.driver.find_element(By.ID, "txt-username").send_keys("abc@gmail.com")
    self.driver.find_element(By.ID, "txt-password").click()
    self.driver.find_element(By.ID, "txt-password").send_keys("12345")
    self.driver.find_element(By.ID, "txt-password").send_keys(Keys.ENTER)
  
