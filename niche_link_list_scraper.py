"""
Group Project: Group 5
Author       : Antara Saha               
Specification: As part of the project requirement, one of our datasource is "niche.com".
               This script is the 1st step in performing web scraping on niche. From this code
               we are fetching the college link url for more than 1900 colleges. In our next step
               we will scrap the data for all those 1900 urls. At the end of this script execution it 
               will generate a niche_url_list.txt file which will contain all the urls for 1900 colleges.
"""

# Import Libraraies

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome import service
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup as soup

def niche_link_list():
# create filename containing college urls
    filename = "niche_url_list.txt" 
    name_list = []

    # fetch college url from below mentioned link
    for x in range(1,79):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches",["enable-logging"])
        s = Service(r'chromedriver.exe')
        driver = webdriver.Chrome(options = options ,service = s)
        print ("Go to next page...")
        my_url = 'https://www.niche.com/colleges/search/best-colleges/?page=' + str(x)

        driver.get(my_url)
        html = driver.page_source
        driver.quit()

        soup = BeautifulSoup(html,'lxml')
        rankings = soup.findAll("div", {"class":"card"})
        
        for y in range(0, len(rankings)):
            link_name = rankings[y].findAll("a", {"class":"search-result__link"})
            for z in link_name:
                if z['href'] not in name_list:
                    name_list.append(z['href'])

    # write file for college urls
    with open(filename,"w") as file_text:
        file_text.write(",".join(name_list))

if __name__ == "__main__":
    niche_link_list()