from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

options = webdriver.ChromeOptions()

driver = webdriver.Chrome(
    service = Service(ChromeDriverManager().install()),
    options = options
)

URL = "https://books.toscrape.com/"
driver.get(URL)

books = driver.find_elements(By.TAG_NAME, "h3")
for element in books:
    print(element.text)

book_titles = []

while True:
    button_next = None

    # Get the books of the current page
    books = driver.find_elements(By.TAG_NAME, "h3")
    for element in books:
        # book_titles.append(element.text)
        book_titles += [element.text]

    # Go to the next page
    a_elements = driver.find_elements(By.TAG_NAME, "a")
    for a_element in a_elements:
        if a_element.text == "next":
            button_next = a_element
    
    if button_next is None:
        break
    else:
        button_next.click()


time.sleep(1000)