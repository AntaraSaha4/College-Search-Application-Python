# -*- coding: utf-8 -*-
"""

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
import re

def SAT_data():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches",["enable-logging"])
    
    driver = webdriver.Chrome(options=options)
    URL = 'https://www.collegetransitions.com/dataverse/entering-class-statistics'
    driver.get(URL)
    
    SAT_Data = []
    Employment_Data = []
    Admissions_Data = []
    list_SAT=[]
    
    i = 1
    
    
    while True:
        rows = WebDriverWait(driver,10) .until(EC.visibility_of_all_elements_located((By.XPATH, '//*[@id="footable_10227"]/tbody')))
        
        for row in rows:
            SAT_Data.append(row.text)
            
        next_page = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//a[@href="#" and contains(text(),"›")]')))
        next_clickable = next_page.find_element_by_xpath("..").get_attribute("class")
        
        i+=1
        if i == 11:
            break
        # print("Go to next page ...")
        next_page.click()
        time.sleep(3)
    driver.quit()
    
    df = pd.DataFrame(columns=['College Name'])
    df2 = pd.DataFrame(columns=['SAT Math','SAT R/W'])
    df3 = pd.DataFrame(columns=['Admission Rate'])
    
    for i in range(len(SAT_Data)):
        d1 = str(SAT_Data[i]).split("\n")
        for chr in d1:
            s = re.findall('([a-zA-Z ]*)\d*.*', chr)
            df = df.append({'College Name': (str(s[0]))}, ignore_index=True)  
            
            s2 = re.findall('[0-9][0-9][0-9]-[0-9][0-9][0-9]',chr)
            df2 = df2.fillna('')
            if(s2==[]):
                df2 = df2.append({"SAT Math": " ", 'SAT R/W' : " "}, ignore_index=True)
                
            else:
                df2 = df2.append({"SAT Math": (str(s2[0])), "SAT R/W": (str(s2[1]))}, ignore_index=True)
                
            s3 = re.findall('[0-9][0-9]%',chr)
            if(s3==[]):
                df3 = df3.append({'Admission Rate': " "}, ignore_index=True)
            else:
                df3 = df3.append({'Admission Rate': (str(s3[0]))}, ignore_index=True)
                
    #One common Dataframe: 
    df['College Name'] = df['College Name'].str.strip()
    df_final = df.join(df2)
    df_final.join(df3).to_csv('SAT_data.csv',index=False)
    
    
      
