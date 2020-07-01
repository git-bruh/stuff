from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from bs4 import BeautifulSoup
import json
import re

url = 'https://covid19india.org'
opts = Options()
opts.headless = False


def covid_scraper():
    driver = webdriver.Chrome(options=opts)
    driver.get(url)
    soup_level1 = BeautifulSoup(driver.page_source, 'lxml')
    results = soup_level1.find(class_="Level")
    stats = results.find_all(['h4', 'h1'])
    remove = "<h4>|</h4>|<h1>|</h1|,|>"
    data = (re.sub(remove, "", str(stats)[1:-1])).split()
    covid_data = {
        'add': data[0],
        'confirm': data[1],
        'active': data[2],
        'add_recover': data[3],
        'recovered': data[4],
        'add_deceased': data[5],
        'deceased': data[6]
        }
    with open('covid.json', 'w') as f:
        json.dump(covid_data, f)
    return None
