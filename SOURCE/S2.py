from selenium import webdriver

# chromedriver examples
def test_open_cura():
     driver = webdriver.Firefox() #This will start the session.
     driver.get("https://katalon-demo-cura.herokuapp.com/") #this will navigate to the URL.
     print(driver.title)
     print(driver.page_source)
     driver.quit()