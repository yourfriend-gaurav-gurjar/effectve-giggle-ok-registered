import csv
import time
from selenium import webdriver
import requests
from selenium.webdriver.common.action_chains import ActionChains
import pandas as pd

# driver = webdriver.Chrome()
# actions = ActionChains(driver)

options = webdriver.ChromeOptions()
options.add_argument("headless")
options.add_argument('no-sandbox')
#specify the path to chromedriver (download and save on your computer)
driver = webdriver.Chrome('./chromedriver', chrome_options=options)

df = pd.read_csv('oklahoma/119637c1-13ee-479a-88e4-e5f786039402.csv')
company_name = df['company_name']
print(company_name)

with open('omma_registered_agent.csv', 'a', newline='',encoding='utf-8') as fd:
    wr = csv.writer(fd, dialect='excel')
    wr.writerow(['filing_number', 'name', 'entity_type','registered_agent','type_n_status'])

for name in company_name:
    driver.get('https://www.sos.ok.gov/corp/corpInquiryFind.aspx')
    time.sleep(3)
    try:
        entity_name = name
        driver.find_element_by_id('ctl00_DefaultContent_CorpNameSearch1__singlename').clear()
        driver.find_element_by_id('ctl00_DefaultContent_CorpNameSearch1__singlename').send_keys(entity_name)
        time.sleep(4)
        search_btn= driver.find_element_by_id('ctl00_DefaultContent_CorpNameSearch1_SearchButton')
        search_btn.click()
        time.sleep(2)
