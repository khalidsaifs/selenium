from selenium import webdriver
import allure


@allure.title("verify the demo cura app")
def test_open_cura():
    driver = webdriver.Chrome()
#     it is post request which opens the new chrome page
    driver.get("https://katalon-demo-cura.herokuapp.com/")
#     it is get request which opens the url

    print(driver.title)
    # Get request
    assert driver.title == "CURA Healthcare Service"
