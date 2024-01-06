"""
Group Project: Group 5
Author       :   Antara Saha               
Specification: This script is to search college based on keyword entered by user. It will display all the 
               colleges based on your keyword and then user can choose for which college they want to see the
               details. This part of the module will provide user with all the necessary details they required
               to make the decision.
"""

# Import Libraries
from os import replace
import pandas as pd
import main_app as mp
import shutil

def s_college(): # Function defination to search college and showing the output on screen
    college_records = pd.read_csv('final_college_data.csv',encoding = "ISO-8859-1")
    col = shutil.get_terminal_size().columns
    print ("="*col)
    grp_name = "Search Based on College Name"
    print (grp_name.upper().center(col))
    print ("="*col)
    loop = True
    while loop:
        k_word = input("\nPlease enter college name:") # Enter the keyword you want to search for college
        results = college_records[college_records['College Name'].str.contains(k_word, case = False)] # Store the matching results
        results = results.fillna(value="Data Not Available")
        
        if results.empty:
            print ("No Record Found.Please Try Again.")
            loop = True
        
        else:
            pd.set_option("display.max_colwidth", None)
            
            if results.shape[0] > 1: # Based on keyword if it has multiple college name
                print ("\nBelow mentioned are the colleges you might be looking for:")
                l = results["College Name"].str.len().max()
                print ('{:<4s} {:>{}s}'.format("Id","College Name",l))
                l = (int(l)+10)
                print("-"*l)
                print(results["College Name"].to_string())
                id = input("\nPlease enter College Id to see result :")                
            
            else:                       # If there is only one college based on keyword search
                index = results.index
                for i in index:
                    id = i
            
            index = results.index
            
            try:
                id = int(id)
                
                if id not in index: # If College ID entered is not in the list
                    print ("\nError: Incorrect College ID. Start Again.")
                
                else:               # Everything ok show the output data
                    print ("\nPrinting the results...\n")
                    print (results.loc[id]["College Name"].upper().center(col))
                    print ("="*col)
                    print ("1.College Report Card")
                    print("\n")
                    print("US Ranking : "+ str(int(results.loc[id]["rank"])))
                    print("Overall Grade: "+ str(results.loc[id]["Overall Grade"]))
                    print("\nCollege Grade Card:"+"\n"+str(results.loc[id]["College Grade Card"]).replace(",","\n"))
                    print ("\n")
                    print ("="*col)
                    print ("2.About")
                    print ("City:", str(results.loc[id]["Location"]))
                    print ("State:", str(results.loc[id]["state"]))
                    print ("\n")
                    print (results.loc[id]["College Description"])
                    print ("\n")
                    print ((results.loc[id]["College Name"])+" Rankings:","\n",str(results.loc[id]["College Highlights"]))
                    print ("\n")
                    print ("Address:",results.loc[id]["address"])
                    print ("Website:",results.loc[id]["website"])
                    print ("College Type:",results.loc[id]["type"])
                    print ("College Housing:",results.loc[id]["campus_housing"])
                    print ("="*col)
                    print ("3.Admissions")
                    print("\n")
                    print ("SAT Math Score Requirement:",results.loc[id]["SAT Math"])
                    print ("SAT R/W Score Requirement:",results.loc[id]["SAT R/W"])
                    print ("Admissions Deadline:",results.loc[id]["Admissions Deadline"])
                    print("\n")
                    print ("="*col)
                    print ("4.Students")
                    print ("\n")
                    print ("Student Population:",results.loc[id]["student_population"])
                    print ("Student Faculty Ratio:",results.loc[id]["student_faculty_ratio"])
                    print("\n")
                    print ("="*col)
                    print ("5.Popular Majors")
                    print ("\n")
                    print (results.loc[id]["Popular Majors"])
                    print("\n")
                    print ("="*col)
                    print("6.Future")
                    print ("\n")
                    print ("Employment Rate:",results.loc[id]["Employment Rate"])
                    print ("\nAverage Salary after 6 years:",results.loc[id]["Avg Salary"])
                    print ("End".center(col,"-"))
                    option = input("\nEnter 'Y' to search more colleges or Hit <Any Key> to exit.")
                    
                    if option.upper() == 'Y':
                        loop = True
                    
                    else:
                        loop = False
            except Exception as e:
                print ("Error Occured:",e)
    print ("\nRedirecting to Main Module...")
    mp.main_app()
