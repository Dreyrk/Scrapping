from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import time

def gotoTD(table):
    all_td = []
    all_tr = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
    for tr in all_tr:
        all_td.append(tr.find_elements(By.TAG_NAME, 'td'))
    return all_td

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

all_links=[]
all_underlinks = []
date_filters = ['1995', '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003', '2004', '2005']
all_tr = driver.find_elements(By.TAG_NAME, 'tr')
all_tr = all_tr[340:]
for tr in all_tr:
    all_td = tr.find_elements(By.TAG_NAME, 'td')
    for td in all_td:
        for filter in date_filters:
            if filter in td.text:
                a = all_td[1].find_element(By.TAG_NAME, 'a')
                all_links.append(a.get_attribute('href'))
                print("link", len(all_links), "added")


for link_id, link in enumerate(all_links):
    print('Page', link_id)
    driver.get(link)
    all_td2 = driver.find_elements(By.TAG_NAME, 'td')
    for td2 in all_td2:
        try:
            a = td2.find_element(By.TAG_NAME, 'a')
            if 'carte' in a.get_attribute('href'):
                all_underlinks.append(a.get_attribute('href'))
                print("underlink", len(all_underlinks), "added")
        except:
            continue

# TODO: Envelvé les doublons
print("NB de carte: ", len(all_underlinks))

for underlink_id, underlink in enumerate(all_underlinks):
    print("Carte N°", underlink_id)
    driver.get(underlink)
    #scrap
