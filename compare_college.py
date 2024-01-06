"""
Compare Two Colleges
Group 5
@authors: Antara Saha, Joe Holleran
12/06/2021
"""
# Import Libraries
import pandas as pd
import main_app as mp
import shutil

# Import compare_college and call c_college() to run the module to compare
# two colleges and display side by side comparison of the two colleges

def c_college(): 
    
    # read csv file
    college_records = pd.read_csv('final_college_data.csv',encoding = "ISO-8859-1")
    
    col = shutil.get_terminal_size().columns
    
    # display module title
    print ("="*col)
    mod_name = "Compare Two Colleges"
    print(mod_name.upper().center(col))
    print("="*col)
            
    loop = True
    
    # get two college names provided by user
    # the user may either provide a not valid college name or a college that
    # has other like-named colleges.  These options are handled here.
    while loop:
        
        col_1 = input("\nPlease enter first College Name: ")
        print("\n")
        
        _col1results = college_records[college_records['College Name'].str.contains(col_1, case = False)]
        _col1results = _col1results.fillna(value="Data Not Available")

        
        if _col1results.empty:
            print("No record found for " + col_1 + ". Please try another college.")
            loop = True  
        else:
            pd.set_option("display.max_colwidth", None)
            if _col1results.shape[0] > 1:
                print("Below mentioned are the colleges you might be looking for:")
                l = _col1results["College Name"].str.len().max()
                print ('{:<4s} {:>{}s}'.format("Id","College Name",l))
                l = (int(l)+10)
                print("-"*l)
                print(_col1results["College Name"].to_string())
                id_1 = input("\nPlease enter College ID to see result:")
            else:
                index_1 = _col1results.index
                for i in index_1:
                    id_1 = i
            index_1 = _col1results.index
    
        col_2 = input("\nPlease enter second College Name: ")
        print("\n")
        
        _col2results = college_records[college_records['College Name'].str.contains(col_2, case = False)]
        _col2results = _col2results.fillna(value="Data Not Available")
        
        if _col2results.empty:
            print("No record found for " + col_2 + ". Please try another college.")
            loop = True
        else:
            pd.set_option("display.max_colwidth", None)
            if _col2results.shape[0] > 1:
                print("Below mentioned are the colleges you might be looking for:")
                l = _col2results["College Name"].str.len().max()
                print ('{:<4s} {:>{}s}'.format("Id","College Name",l))
                l = (int(l)+10)
                print("-"*l)
                print(_col2results["College Name"].to_string())
                id_2 = input("\nPlease enter College ID to see result:")
            else:
                index_2 = _col2results.index
                for i in index_2:
                    id_2 = i
            index_2 = _col2results.index
            
            # display data for the two colleges selected
            try:
                id_1 = int(id_1)
                id_2 = int(id_2)
                
                if id_1 not in index_1:
                    print("\nError: Incorrect College ID. Please start again.")
                elif id_2 not in index_2:
                    print("\nError: Incorrect College ID. Please start again.")
                else:               
                    print("="*col)
                    print("1.College Report Card")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print("US Ranking : "+ str(int(_col1results.loc[id_1]["rank"])))
                    print("Overall Grade: "+ str(_col1results.loc[id_1]["Overall Grade"]))
                    print("College Grade Card:"+"\n"+str(_col1results.loc[id_1]["College Grade Card"]))
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print("US Ranking : "+ str(int(_col2results.loc[id_2]["rank"])))
                    print("Overall Grade: "+ str(_col2results.loc[id_2]["Overall Grade"]))
                    print("College Grade Card:"+"\n"+str(_col2results.loc[id_2]["College Grade Card"]))
                    print("\n")
                    print("="*col)
                    print("2.About")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print("Town:", str(_col1results.loc[id_1]["Location"]))
                    print("\n")
                    print(_col1results.loc[id_1]["College Description"])
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"])
                    print(_col1results.loc[id_1]["College Highlights"])
                    print("\n")
                    print("Address:",_col1results.loc[id_1]["address"])
                    print("Website:",_col1results.loc[id_1]["website"])
                    print("College Type:",_col1results.loc[id_1]["type"])                 
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print("Town:", str(_col2results.loc[id_2]["Location"]))
                    print("\n")
                    print(_col2results.loc[id_2]["College Description"])
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"])
                    print(_col2results.loc[id_2]["College Highlights"])
                    print("\n")
                    print("Address:",_col2results.loc[id_2]["address"])
                    print("Website:",_col2results.loc[id_2]["website"])
                    print("College Type:",_col2results.loc[id_2]["type"])
                    print("\n")
                    print("="*col)
                    print("3.Admissions")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print("Acceptance Rate:",_col1results.loc[id_1]["Admission Rate"])
                    print("SAT Math:",_col1results.loc[id_1]["SAT Math"])
                    print("SAT R/W:",_col1results.loc[id_1]["SAT R/W"])
                    print("Admission Deadline:",_col1results.loc[id_1]["Admissions Deadline"])
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print("Acceptance Rate:",_col2results.loc[id_2]["Admission Rate"])
                    print("SAT Math:",_col2results.loc[id_2]["SAT Math"])
                    print("SAT R/W:",_col2results.loc[id_2]["SAT R/W"])
                    print("Admission Deadline:",_col2results.loc[id_2]["Admissions Deadline"])
                    print("\n")
                    print("="*col)
                    print("4.Students")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print("Student Population:",_col1results.loc[id_1]["student_population"])
                    print("Student Faculty Ratio:",_col1results.loc[id_1]["student_faculty_ratio"])
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print("Student Population:",_col2results.loc[id_2]["student_population"])
                    print("Student Faculty Ratio:",_col2results.loc[id_2]["student_faculty_ratio"])
                    print("\n")
                    print("="*col)
                    print("5.Popular Majors")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print(_col1results.loc[id_1]["Popular Majors"])
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print(_col2results.loc[id_2]["Popular Majors"])
                    print("\n")
                    print("="*col)
                    print("6.Future")
                    print("\n")
                    print(_col1results.loc[id_1]["College Name"].upper().center(col))
                    print("Employment Rate:",_col1results.loc[id_1]["Employment Rate"])
                    print("\nAverage Salary after 6 years:",_col1results.loc[id_1]["Avg Salary"])
                    print("\n")
                    print(_col2results.loc[id_2]["College Name"].upper().center(col))
                    print("Employment Rate:",_col2results.loc[id_2]["Employment Rate"])
                    print("\nAverage Salary after 6 years:",_col2results.loc[id_2]["Avg Salary"])
                    print("End".center(col,"-"))
                    
            except Exception as e:
                print ("Error Occured:",e)
        
        # prompt the user to verify they would like to continue
        option = input("Do you want to search more? (Y/N): ")
        if option.upper() == 'Y':
            loop = True
        else:
            loop = False
                
    # if user selects 'Y' then move to main module
    print ("\nRedirecting to Main Module...")
    print("\n")
    mp.main_app()
    

if __name__ == '__main__':
    c_college()
