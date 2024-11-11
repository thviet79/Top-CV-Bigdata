# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from bs4 import BeautifulSoup
# import time

# # Set up Selenium with Chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# def get_titles_with_selenium(list_link):
#     titles = []
#     for link in list_link:
#         driver.get(link)
#         time.sleep(2)  # Wait for the page to load
#         soup = BeautifulSoup(driver.page_source, "html.parser")
#         title = soup.findAll('h3', class_='title')
#         for tit in title:
#             titles.append(tit)
#     return titles

# # After completing, close the browser
# driver.quit()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time

# Set up Selenium with Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

def get_titles_with_selenium(list_link):
    titles = []
    for link in list_link:
        driver.get(link)
        time.sleep(2)  # Wait for the page to load
        soup = BeautifulSoup(driver.page_source, "html.parser")
        title = soup.findAll('h3', class_='title')
        for tit in title:
            titles.append(tit)
    return titles

# After completing, close the browser
driver.quit()
