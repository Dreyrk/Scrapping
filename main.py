from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Set Up Client

PATH = "C:\\Users\\darkd\\Documents\\Driver\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
driver = webdriver.Chrome(PATH, options=options)
navigator = "Google Chrome/105.0.5195.102"

# Start Client

driver.start_client()
driver.get('https://www.ultrajeux.com/genre-4-cartes-a-lunite-yu-gi-oh-francais.html')
cookie_id = "tarteaucitronPersonalize2"
time.sleep(5)
cookie = driver.find_element(By.ID, cookie_id)
if cookie.is_displayed():
    print('cookieclicked')
    cookie.click()

all_a = driver.find_elements(By.TAG_NAME, 'a')
#
for a in all_a:
    print(a.get_attribute('href'))


# filter on 1995 to 2005
# from this list
# go to every link
# scrap

