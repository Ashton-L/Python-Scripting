#This is a basic web scraper script that scrapes the first page of the top 20 trending data sets from Data.gov.
#The scraper will pull the title, organization type, organization, and description of the data set.
#The data is exported into a csv file named "Data.gov scrape.csv"

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_soup(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, "html.parser")
    else:
        raise exception(f'Failed to retrieve page; status code {response.status_code}')

def scrape_titles(soup):
    title_lines = soup.find_all('h3', class_="dataset-heading")
    titles = [line.find('a').text.strip() for line in title_lines]
    return titles

def scrape_org_type(soup):
    org_type_lines = soup.find_all('div', class_="organization-type-wrap")
    org_type = [line.find('span').text.strip() for line in org_type_lines]
    return org_type

def scrape_organizations_and_descriptions(soup):
    lines = soup.find_all('div', class_="notes")
    organizations = [line.find('p').text.strip(' —') for line in lines]
    descriptions = [line.find('div').text.strip() for line in lines]
    return organizations, descriptions

def main():
    url = "http://catalog.data.gov/dataset"
    soup = get_soup(url)

    titles = scrape_titles(soup)
    org_type = scrape_org_type(soup)
    organizations, descriptions = scrape_organizations_and_descriptions(soup)

    data = {
        'Title': titles,
        'Data Jurisdiction Type': org_type,
        'Organization': organizations,
        'Description': descriptions,
    }

    df = pd.DataFrame(data)
    df.to_csv('Data.gov_scrape.csv', index=False)

if __name__ == "__main__":
    main()
