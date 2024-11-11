from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.edge.options import Options
from selenium.webdriver.firefox.options import Options
import time
# chromeoptions


def test_open_cura():
    # chrome_options = Options()
    # chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--start-maximized")
    driver = webdriver.Chrome()

    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"

    time.sleep(5)
def test_edge_open_cura():
    # edge_options = Options()
    # edge_options.add_argument("--incognito")
    # edge_options.add_argument("--start-maximized")
    driver = webdriver.Edge()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"

    time.sleep(5)
def test_firefox_open_cura():
    # firefox_options = Options()
    # firefox_options.add_argument("--incognito")
    # firefox_options.add_argument("--start-maximized")
    driver = webdriver.Firefox()
    driver.get("https://katalon-demo-cura.herokuapp.com/")
    assert driver.title == "CURA Healthcare Service"

    time.sleep(5)