"""
Group Project: Group 5
Author     :   Ziyou Li
Updated By :
Specification: This script is to web-scrape the data from UniRank. The intended output are college name
and its corresponding ranking.
"""
from bs4 import BeautifulSoup
import requests
import pandas as pd
import re
import unidecode

# Method to be called by main to scrap uniRank data
def scrap_uniRank():
    URL = "https://www.4icu.org/us/"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    ranking = soup.find("table", attrs={"class": "table table-hover"})
    body = ranking.find_all('tr')

    rankContent = body[2:]

    all_rows = []
    for i in range(len(rankContent)):
        row = []
        for row_item in rankContent[i].find_all('td'):
            cleaned = re.sub("<[a-z][A-Z]+>", "", row_item.text)
            row.append(cleaned)
        all_rows.append(row)

    for i in range(len(all_rows)):
        all_rows[i][1] = all_rows[i][1].replace('\"', "")
    for i in range(len(all_rows)):
        all_rows[i][1] = unidecode.unidecode(all_rows[i][1])
        if len(all_rows[i]) > 2:
            all_rows[i][2] = unidecode.unidecode(all_rows[i][2])
            all_rows[i][2] = all_rows[i][2].replace("...", "")

    headings = ['rank', 'College Name', 'Location']

    df = pd.DataFrame(data=all_rows, columns=headings)
    df.head()
    df.to_csv("US_Ranking_Data.csv", index=False)
