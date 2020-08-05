import requests
from bs4 import BeautifulSoup
URL = 'https://www.glassdoor.com/Job/seattle-systems-administrator-jobs-SRCH_IL.0,7_IC1150505_KO8,29.htm'
headers = {'user-agent': 'Mozilla/5.0'}
page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')
results = soup.find(id='MainCol')
job_elems = results.find_all('div', class_='jobContainer')

for job_elem in job_elems:
    title_elem = job_elem.find_all('span')[2]
    company_elem = job_elem.find('div', class_='jobInfoItem jobEmpolyerName')
    location_elem = job_elem.find('div', class_='jobInfoItem empLoc flex-wrap')
    print(company_elem.text)
    print(location_elem.text)
    print (title_elem.text)
    print()
