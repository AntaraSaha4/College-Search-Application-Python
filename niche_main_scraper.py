"""
Group Project: Group 5
Author      :  Antara Saha               
Specification: This script is to pass college url to function we defined in niche_web_scrap.py to 
               scrap the data. At the end of the script it will generate a temp csv file containing
               all the details we scraped from the url.
               
"""
# Import Libraries
from os import write
import niche_web_scrap as ws
import time
import csv
import traceback

def main_scraper():

    # Read the file we generated in the 1st step containing college web urls
    with open("niche_url_list.txt") as file_obj:
        content = file_obj.readline()

    url_ls = content.split(",")

    # Create list of dictionary to store the data
    college_data_list = []

    # Pass url to the function to perform web scraping
    for url in url_ls:
        try:
            print (url)
            temp_dict = ws.web_scrap(url)
            college_data_list.append(temp_dict)
            time.sleep(2)
        except Exception as e:
            with open("niche_error_log.txt",'a+') as file_obj:
                msg = "Error Url: "+url+"\n"\
                    "Err_Msg: "+str(traceback.format_exc())+"\n"
                file_obj.write("-----Error Message-----"+"\n")
                file_obj.write(msg)
            pass

    # Create csv file
    keys = college_data_list[0].keys()
    with open('temp_niche_college_data.csv', 'w',encoding="utf-8", newline='') as output_file:
        dict_writer = csv.DictWriter(output_file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(college_data_list)

if __name__ == "__main__":
    main_scraper()