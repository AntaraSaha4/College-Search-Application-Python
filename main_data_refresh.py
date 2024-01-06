"""
Group Project: Group 5
Author     :   Antara Saha,Ziyou Li
Specification: This script is to run the scripts responsible for fetching clean data from
                different datasources.

"""

# Import Other Modules and other required Libraries
import shutil
import unirankScrap as ur
import nces_ed as ne
import college_transition_data_scraper as ct
import admissions_deadline as ad
import niche_main_scraper as nm
import niche_link_list_scraper as nl
import niche_collegename_mismatch as nc
import final_data_merge as fm
import main_app as mp

def main_data_refresh():

    col = shutil.get_terminal_size().columns

    print ("="*col)
    grp_name = "Refresh Data Module"
    print (grp_name.upper().center(col))
    print ("="*col)

    #Define DataSources Name
    Datasource1 = "UniRank"
    Datasource2 = "NCES.ed.gov"
    Datasource3 = "College Transition"
    Datasource4 = "Niche.com"

    loop = True

    while loop:
        # Options to clean Datasource
        print ("\n")
        print("Option 1.Refresh Data->",Datasource1)
        print ("\t**Execution Time: 5 Mins")
        print("\nOption 2.Refresh Data->",Datasource2)
        print ("\t**Execution Time: 1 Hour")
        print("\nOption 3.Refresh Data->",Datasource3)
        print ("\t**Execution Time: 15 Mins")
        print("\nOption 4.Refresh Data->",Datasource4)
        print ("\t**Execution Time: 9-10 Hours")
        print("\nOption 5.Refresh all the Data.")
        print ("\t**Execution Time: 10-12 Hours")
        
        print ("\n**Please note Execution Time may vary with system.")

        ID = input("\nPlease enter the option ID to Refresh the Data:")
        try: 
            ID = int(ID)
            
            if ID == 1:                # To refresh data for UniRank
                print ("Fetching Data from UniRank url...")                
                ur.scrap_uniRank()
            elif ID == 2:               # To refresh data for Nces_edu
                print ("Fetching Data from nces_edu url...")
                ne.get_nces_data()
            elif ID == 3:               # To refresh data for College Transition
                print ("Fetching Data from College Transition url...")
                ct.SAT_data()
                ad.admission_deadlines()
            elif ID == 4:               # To refresh data for Niche.com
                print ("Fetching Data from Niche.com url...")
                nl.niche_link_list()
                nm.main_scraper()
                nc.collegename_clean()
            elif ID == 5:               # To refresh data for all datasources
                print ("\nFetching Data from UniRank url...")
                ur.scrap_uniRank()
                print ("\nFetching Data from NCES.ed.gov url...")
                ne.get_nces_data()
                print ("\nFetching Data from College Transition url...")
                ct.SAT_data()
                ad.admission_deadlines()
                print ("\nFetching Data from Niche.com url...")
                nl.niche_link_list()
                nm.main_scraper()
                nc.collegename_clean()
            else:                       # In case of Incorrect Option ID
                print ("Error:Incorrect Option ID.")
            
            if 1 <= ID <= 5:            # Execute Final Data Merge only incase of valid option ID
                print("Final Data Merge In Progress...")
                fm.final_data_merge()
                print ("\nProcess Completed Successfully.")
            choice = input("\nEnter 'Y' to refresh data again for other Datasources or Hit <Any Key> to exit.")
            if choice.upper() == "Y":
                loop = True
            else:
                loop = False        
        except Exception as e:
            print ("Error Occured:",e)
    print("\nExiting Refresh Data Module...")
    print("\nRedirecting to Main Module...")
    mp.main_app()

    
if __name__ == "__main__":
    main_data_refresh()