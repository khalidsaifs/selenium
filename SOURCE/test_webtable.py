import allure
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# def test_webtable():
#     drivers = webdriver.Chrome()
#     drivers.get("https://demoqa.com/webtables")
#     drivers.maximize_window()
#
#     # # row[@class="rt-tr-group"]
#     # # ss = "rt-tbod
#     # elements = drivers.find_elements(By.XPATH,"//div[@class='rt-tr-group']")
#     #
#     # ele = len(elements)
#     # print(ele)
#     #
#     row_elements = drivers.find_elements(By.XPATH,"//div[@class ='rt-tbody']")
#     for e in row_elements:
#         print(e.text)
#     # # column or cell  class="rt-tr-group"][2]//div[@class="rt-td"][2]
#     # cell_elements = drivers.find_elements(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-tr -even']")
#     # cell = len(cell_elements)
#     # print(cell_elements.text)
#     # if "alden" in cell_elements:
#     #     print ('yes')
#     #
#     # else:
#     #     print ('no')
#     # # expup'
#
#     first_name = drivers.find_element(By.XPATH,"//div[@class='rt-tr-group'][2]//div[@class='rt-td'][1]")
#     second_name = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-td'][2]")
#     age = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-td'][3]")
#     email = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-td'][4]")
#     salary = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-td'][5]")
#     department = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][2]//div[@class='rt-td'][6]")
#     details = f"{first_name.text} {second_name.text} {age.text} {email.text} {salary.text} {department.text}"
#     print(details)
#
#     if "alden" in details:
#         print (f"alden {second_name.text} is earning {salary.text} at {age.text} in {department.text}")
#
#     else:
#         print ('no')
#
#     time.sleep(0)

# def test_dynamic_tables():
#     drivers = webdriver.Chrome()
#     drivers.get("https://awesomeqa.com/webtable1.html")
#
#     table = drivers.find_elements(By.XPATH,"//table[@class='tsc_table_s13']")
#     for t in table:
#         print(t.text)




    # time.sleep(2)