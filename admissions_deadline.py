# -*- coding: utf-8 -*-
"""
Created on Wed Dec  1 23:56:06 2021

@author: shreya
"""

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import pandas as pd
from selenium.webdriver.chrome.options import Options
import time
from csv import writer
import re

def admission_deadlines():
    list_Admissions = []
    Admissions_Data = []

    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    
    driver2 = webdriver.Chrome(options=options)
    URL2 = 'https://www.collegetransitions.com/dataverse/admission-deadlines'
    driver2.get(URL2)
    
    i = 1
    
    while True:
        rows = WebDriverWait(driver2,10) .until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="footable_10131"]/tbody')))
        for row in rows:
            Admissions_Data.append(row.text)
            
        next_page = WebDriverWait(driver2, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#" and contains(text(),"›")]')))
        next_clickable = next_page.find_element_by_xpath("..").get_attribute("class")
        i+=1
        if i == 10:
            break
        #print("Go to next page ...")
        next_page.click()
        time.sleep(3)
    driver2.quit()
    
    df1 = pd.DataFrame(columns=['College Name'])
    #df = pd.DataFrame(columns=['Early Action Deadlines','Early Decision Deadline', 'Early Decision 2 Deadline', 'Priority Deadline', 'Regular Deadline'])
    df = pd.DataFrame(columns=['Admissions Deadline'])
    #i are the page numbers:
    for i in range(len(Admissions_Data)):
        d1 = str(Admissions_Data[i]).split("\n")
        list_Admissions = list_Admissions +d1
        for chr in d1:
            s = re.findall('([a-zA-Z ]*)\d*.*', chr)
            df1 = df1.append({'College Name': (str(s[0]))}, ignore_index=True)
    
            dates = re.findall(r"(?:January|February|March|April|May|June|July|August|September|October|November|December) \d{1,2}",chr)
            if(dates==[]):
                df = df.append({"Admissions Deadline": " "}, ignore_index=True)
            else:
                df = df.append({"Admissions Deadline": (str(dates[0]))}, ignore_index=True)
    
    
    
    df1['College Name'] = df1['College Name'].str.strip()
    df1['College Name'] = df1['College Name'].str.rsplit(' ',1).str[0]
    
    
    df2 = df1.join(df)
    df2
    df2.drop_duplicates(subset ="College Name",
                         keep = False, inplace = True)
    
    df2.to_csv("Admissions_deadline.csv", index=False)
        