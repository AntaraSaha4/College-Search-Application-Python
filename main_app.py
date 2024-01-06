"""
Group Project: Group 5
Author     :   Antara Saha
Updated By :                
Specification: This script is to run the main app for our Project Bright Academy.
"""

# Import Libraries
import shutil
import search_college as sc
import compare_college as cc
import main_data_refresh as md
import user_profile as up

def main_app(): # Main function to call other functions
    col = shutil.get_terminal_size().columns

    print ("="*col)
    grp_name = "SECTION-D2,PROJECT GROUP : 5"
    app_name = "BRIGHT ACADEMY- Empowering Youth For A Bright Future"
    print (grp_name.center(col))
    print (app_name.center(col))
    print ("="*col)

    module1 = "REFRESH DATA"
    module2 = "SEARCH BASED ON USER PROFILE"
    module3 = "SEARCH BASED ON COLLEGE NAME"
    module4 = "COMPARE TWO COLLEGES FOR DETAILED COMPARISON "

    print ("MODULE 1: ",module1)
    print ("MODULE 2: ",module2)
    print ("MODULE 3: ",module3)
    print ("MODULE 4: ",module4)
    print ("\nEnter '0' to exit.")
    print ("\n")

    loop = True
    
    while loop:
        mod_id = input("Please Enter Module ID to begin with: ")
        try:
            mod_id = int(mod_id)
            if mod_id == 1:     # Search Based on User Profile
                md.main_data_refresh()
                loop = False
            
            elif mod_id == 2:     # Search Based on User Profile
                up.profile_search()
                loop = False
            
            elif mod_id == 3:   # Search Based on College Name
                sc.s_college()
                loop = False
            
            elif mod_id == 4:   # Compare two Colleges for detailed comparison
                cc.c_college()
                loop = False
            
            elif mod_id == 0:   # To exit the program
                loop = False
                print ("\nGood Luck for your Future.\n")
                break
            
            else:
                print ("Error: You have entered wrong module ID.")
                opt = input("Enter 'Y' to try again or Hit <Any Key> to exit.")
                loop = True
                
                if opt.upper() == "Y":
                    loop = True
                else:
                    loop = False
                    print ("\nGood Luck for your Future.\n")
        except Exception as e:
            print ("Error Occured:",e)    

if __name__ == "__main__":
    main_app()





