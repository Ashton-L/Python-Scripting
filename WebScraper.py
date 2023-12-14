import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "http://catalog.data.gov/dataset"
r = requests.get(url)
html = r.text
soup = BeautifulSoup(html, "html.parser")

title_lines = soup.find_all('h3', class_="dataset-heading")
titles = []
for line in title_lines:
    title = line.find('a')
    if title:
        titles.append(title.text.strip())

org_type_lines = soup.find_all('div', class_="organization-type-wrap")
org_type = []
for line in org_type_lines:
    org = line.find('span')
    if org:
        org_type.append(org.text.strip())

organizations_and_description_lines = soup.find_all('div', class_="notes")
organizations = []
descriptions = []
for line in organizations_and_description_lines:
    organization = line.find('p')
    description = line.find('div')
    if organization and description:
        organizations.append(organization.text.strip(' —'))
        descriptions.append(description.text.strip())

data = {
    'Title': titles,
    'Data Jurisdiction Type': org_type,
    'Organization': organizations,
    'Description': descriptions,
}

df = pd.DataFrame(data)
df.to_csv('Data.gov data.csv', index=False)
