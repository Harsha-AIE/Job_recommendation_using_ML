# scrape_jobs.py
import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_jobs(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, 'html.parser')

    jobs = []

    for job_card in soup.find_all('div', class_='jobContainer'):
        job_title = job_card.find('a', class_='jobTitle').text.strip()
        company_name = job_card.find('div', class_='companyName').text.strip()
        location = job_card.find('span', class_='location').text.strip()
        job_description = job_card.find('div', class_='jobDescription').text.strip()

        jobs.append({
            'Job Title': job_title,
            'Company Name': company_name,
            'Location': location,
            'Job Description': job_description
        })

    df = pd.DataFrame(jobs)
    df.to_csv("scraped_jobs.csv", index=False)
    return df
