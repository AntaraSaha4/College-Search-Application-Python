"""
Group Project: Group 5
Author       : Antara Saha               
Specification: This script is part of web scraping process. We have define a function in this
               script which is responsible to scrap and clean data from niche.com. The function
               defined here will get called by another python script "niche_main_scraper.py".
"""

# Import Libraries
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# function to scrap and clean the data from niche.com
def web_scrap(url):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    s = Service(r'chromedriver.exe')
    driver = webdriver.Chrome(options = options ,service = s)

    driver.get(url)
    html = driver.page_source
    driver.quit()

    soup = BeautifulSoup(html,'lxml')
    
    # Create a temp dictionary to store all the extracted details
    temp_dict = {}

    # To fetch College Name
    college_name = soup.find("h1",{"class":"postcard__title"})
    college_name = str(college_name)
    l1 = college_name.find(">")+1
    college_name = college_name[l1:].replace("</h1>","")
    college_name = college_name.encode("ascii", "ignore")
    college_name = college_name.decode().replace('&amp;', 'and')
    temp_dict["College Name"] = college_name
    
    # To fetch Niche Overall Grade
    if soup.find("section", {"id":"report-card"}):
        overall_grade = soup.find("section", {"id":"report-card"})
        o_grade = overall_grade.find("div", {"class":"overall-grade__niche-grade"})
        o_grade = o_grade.text
        temp_dict["Overall Grade"] = o_grade[6:].replace(" minus","-")
    else:
        temp_dict["Overall Grade"] = "Data Not Available"

    # To get the report card from niche
    if soup.find("div", {"class":"report-card"}):
        report_card = soup.find("div", {"class":"report-card"})
        grades = report_card.findAll("li", {"class":"ordered__list__bucket__item"})
        temp_grade = []
        for grade in grades:
            g = grade.div.select('div')[0].text+" : "+grade.div.select('div')[1].text.title()[6:]
            temp_grade.append(str(g.replace(" Minus","-")))
        temp_dict["College Grade Card"] = ",".join(temp_grade)
    else:
        temp_dict["College Grade Card"] = "Data Not Available"

        
    # To get list of all Majors
    if soup.find("section", {"id":"majors"}):
        majors = soup.find("section", {"id":"majors"}).find_all("div", {"class":"popular-entity__name"})
        temp_majors = []
        for major in majors:
            temp_majors.append(major.text)
        temp_dict["Popular Majors"] = ",".join(temp_majors)
    else:
        temp_dict["Popular Majors"] = "Data Not Available"

    # To get college description
    if soup.find("section", {"id":"editorial"}):
        description = soup.find("section", {"id":"editorial"}).find("span", {"class":"bare-value"})
        desc = description.text.encode("ascii", "ignore")if description != None else "Data Not Available".encode("ascii", "ignore")
        desc_decode = desc.decode()
        temp_dict["College Description"] = desc_decode
    elif soup.find("section", {"id":"from-the-school"}):
        description = soup.find("section", {"id":"from-the-school"}).find("p", {"class":"premium-paragraph__text"})
        desc = description.text.encode("ascii", "ignore") if description != None else "Data Not Available".encode("ascii", "ignore")
        desc_decode = desc.decode()
        temp_dict["College Description"] = desc_decode
    else:
        temp_dict["College Description"] = "No Description Available"

    # After College Details:
    if soup.find("section", {"id":"after"}).find("div", {"class":"profile__bucket--1"}).find("div",{"class":"scalar__value"}):
        after_college = soup.find("section", {"id":"after"})
        salary = after_college.find("div", {"class":"profile__bucket--1"}).find("div",{"class":"scalar__value"})
        salary = salary.text.encode("ascii", "ignore")
        salary_decode = salary.decode()
        len_salary = salary_decode.find("year")+4
        student_salary = salary_decode[:len_salary]
        len_national = len("National")
        national_salary = salary_decode[len_salary:len_salary+len_national]+" avg salary is "+salary_decode[(len_salary+len_national):]
        temp_dict["Avg Salary"] = student_salary+"\n"+national_salary
    else:
        temp_dict["Avg Salary"] = "Data Not Available"

    if soup.find("section", {"id":"after"}).find("div", {"class":"profile__bucket--2"}).find_all_next("div",{"class":"scalar--three"}):
        after_college = soup.find("section", {"id":"after"})
        employment_rate = after_college.find("div", {"class":"profile__bucket--2"}).find_all_next("div",{"class":"scalar--three"})
        employment_rate = employment_rate[1].text
        l1 = len("Employed 2 Years After Graduation")
        l2 = employment_rate.find("National")
        len_national = len("National")
        employment_rate = employment_rate[l1:l2]+"\n"+employment_rate[l2:(l2+len_national)]+" is "+employment_rate[(l2+len_national):]
        temp_dict["Employment Rate"] = employment_rate
    else:
        temp_dict["Employment Rate"] = "Data Not Available"

    # College Ranking
    if soup.find("section", {"id":"rankings"}).find("div", {"class":"profile__bucket--1"}):
        ranking = soup.find("section", {"id":"rankings"})
        rank_desc = ranking.find("div", {"class":"profile__bucket--1"}).find_all("div",{"class":"rankings__collection__name"})
        rank_ls = []
        for r in rank_desc:
            rank_ls.append(r.text)
        rank_details = ranking.find("div", {"class":"profile__bucket--1"}).find_all("div",{"class":"rankings__collection__ranking"})
        rank_d_ls = []
        for d in rank_details:
            rank_d_ls.append(d.text)

        temp_highlights = []
        for i in range(len(rank_ls)):
            temp_highlights.append(rank_ls[i]+":"+rank_d_ls[i])
        temp_dict["College Highlights"] = ",".join(temp_highlights)
    else:
        temp_dict["College Highlights"] = "Data Not Available"
    
    return temp_dict
