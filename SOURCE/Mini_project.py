from selenium import webdriver
import pytest
import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import (ElementNotInteractableException,ElementNotSelectableException)


@pytest.mark.positive
@allure.title("opening ebay")
@allure.description("print the titles and prices")

def test_open_ebay():
    driver = webdriver.Chrome()
    driver.get("https://www.ebay.ie/")

    (WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,"//input[@class='gh-tb ui-autocomplete-input']"))))
    input_box = driver.find_element(By.XPATH,"//input[@class='gh-tb ui-autocomplete-input']")
    input_box.send_keys("Mac mini")

    (WebDriverWait(driver=driver, timeout=5).until(
        EC.visibility_of_element_located((By.XPATH,"//input[@id='gh-btn']"))))

    search_click = driver.find_element(By.XPATH,"//input[@id='gh-btn']")
    search_click.click()

    # (WebDriverWait(driver = driver, timeout=30).until(EC.visibility_of_all_elements_located((By.XPATH,"//div[@class='s-item__title']"))))

    all_headings = driver.find_elements(By.XPATH,"//div[@class='s-item__title']")

    # (WebDriverWait(driver=driver, timeout=30).until(
    #     EC.visibility_of_all_elements_located((By.XPATH,"//span[@class='s-item__price']"))))

    all_prices = driver.find_elements(By.XPATH,"//span[@class='s-item__price']")







    # for i in all_headings:
    #     print(i.text)
    # for j in all_prices:
    #     print(j.text)
    # for i,j in all_headings,all_prices:
    #     print(i.text + "-" + j.text)
    # print(len(all_prices) + len(all_headings))
    # assert len(all_headings) > 0
    # assert len(all_prices) > 0
    # print(len(all_headings))
    # print (len(all_prices))
    for headings, prices in zip(all_headings,all_prices):
         print(headings.text + " - " + prices.text)

    prices = []
    for element in all_prices:
        price_text = element.text
        price_number = float(price_text.replace(',', '').strip())
        prices.append(price_number)

    max_price = max(prices)
    print(f"The max price is: euro{max_price}")


    # zipped_list=list(zip(all_prices,all_headings))
    #
    # # Use max with the lambda function to convert the price to float for comparison
    # max_item = max(zipped_list, key=lambda x: float(x[0].text.replace('€', '').replace(',', '').strip()))
    #
    # # max_item = max(zipped_list, key= lambda x: float(x[1].text.replace('€', '').replace(',','').strip()))
    # print(f" the highest price of mac mini is : {max_item[0].text} at {max_item[1].text}")

    driver.quit()
