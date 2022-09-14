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
    cookie.click()  # <- cookie pass here

all_a = driver.find_elements(By.TAG_NAME, 'a')  # <- get all html tag <a>
links = []
for a in all_a:
    links.append(a.get_attribute('href')) # <- make a list of all attribute of all a tag

# remove useless links
clean_links = []

for link in links:
    pattern = "ultrajeux.com/edition"
    if pattern in link:
        clean_links.append(link)

table_elem = driver.find_element(By.TAG_NAME, 'table')  # <- get html tag <table>
table = table_elem.text

# str -> list
table = table.split('\n')

# filter on 1995 to 2005
date_filters = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005']
all_names = []
for filtr in date_filters:
    for name in table:
        if filtr in name:
            all_names.append(name)

print(clean_links)
print('\n###\n')
print(all_names)


#TODO: faire matcher les all_names avec les clean_links pour n'avoir que les links qu'on veut



# from this list
# go to every link
# scrap

