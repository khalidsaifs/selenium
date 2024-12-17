from selenium import webdriver
from selenium.webdriver.common.by import By


def test_exercise():

    drivers = webdriver.Chrome()
    drivers.get("https://demoqa.com/webtables")
    # CodingChallenges
    # 1.Print All Data from a Web Table
    # Question: Write a Selenium script to print all rows and columns of a web table to the console.
    # print_data = drivers.find_elements(By.XPATH, "//div[@class='rt-table']")
    # for data in print_data:
    #     print(data.text)
    #
    # #     2. Extract Data from a Specific Row and Column
    # #       Question: Given a web table, write a script to extract the value from the 3rd row and 2nd column.
    #         extra_data = drivers.find_element(By.XPATH,"//div[@class='rt-tr-group'][3]//div[@class='rt-td'][2] ")
    #         print(extra_data.text)

    # 3.3. Find Data Based on Header Name
    # Question: Write a script to extract the email address of a person whose first name is "Cierra" from a web table.

    # email = drivers.find_element(By.XPATH, "//div[@class='rt-tr-group'][1]//div[@class='rt-td'][4]")
    # details = drivers.find_elements(By.XPATH, "//div[@class = 'rt-tr-group'][1]")
    # for i in details:
    #     print(i.text)
    #     if "Cierra" in i.text:
    #      print(f"{email.text}")
    #     else:
    #      print("no")

#    4. Count Rows and Columns
# Question: Write a script to count the number of rows and columns in a web table.
#     row= drivers.find_elements(By.XPATH, "//div[@class ='rt-tr-group']")
#     r = len(row)
#     print(r)
#
#     co = drivers.find_elements(By.XPATH, "//div[@class ='rt-td']")
#     c = len(co)
#     print(c)

    # 5. Verify Data in a Table
    # Question: Write a script to verify if a particular value (e.g., "Insurance") exists in the "Department" column.

    department = drivers.find_elements(By.XPATH, " //div[@class = 'rt-td'][6]")

    for i in department:


        if "Insurance" in i.text:
            print("Insurance")
        else:
            print("no")