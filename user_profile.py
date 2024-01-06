"""
Group Project: Group 5
User Profile Module
@author: Shreya Bedi, Joe Holleran
12/05/2021
"""
import pandas as pd
import shutil
import main_app as mp

# Import user_profile and call profile_search() to run the module to allow
# user to create a profile of their desired college state and their SAT scores
# the module will then output matches for scores and state

def profile_search():
    
    # read csv file
    college_records = pd.read_csv('final_college_data.csv',encoding = "ISO-8859-1")
    
    col = shutil.get_terminal_size().columns
    
    # print user greeting
    print ("="*col)
    mod_name = "User Profile Search"
    print(mod_name.upper().center(col))
    print("="*col)
    
    state_check = True
    
    # get user state to build profile
    while state_check:
    
        user_state = input("Please enter the state where you would like to attend college: ")
        user_state = user_state.upper()
        state_results = college_records[college_records['state'].str.contains(user_state, na=False)]
        
        if state_results.empty:
            
            print("\nSorry, there are no college matches for state: " + user_state)
            state_check == True
            
        else:
            state_check = False
            
    # get user SAT math scores    
    math_check = True
    
    while math_check:
        
        SAT_math = input("Please enter your SAT Math score: ")
        
        try:
            
            SAT_math = int(SAT_math)
            
            if SAT_math < 400:
                print("\nPlease enter a valid SAT Math score (400-800).")
                math_check = True
            elif SAT_math > 800:
                print("\nPlease enter a valid SAT Math score (400-800).")
                math_check = True
            else:
                math_check = False
            
        except ValueError:
            # int(str) raises ValueError
            print("Please enter your SAT Math score again.\n")
            math_check = True
    
    # get user SAT read/write scores
    rw_check = True
    
    while rw_check:
        
        SAT_rw = input("Please enter your Reading & Writing score: ")
        
        try:
            
            SAT_rw = int(SAT_rw)
            
            if SAT_rw < 400:
                print("\nPlease enter a valid SAT Reading & Writing score (400-800).")
                rw_check = True    
            elif SAT_rw > 800:
                print("\nPlease enter a valid SAT reading & Writing score (400-800.")
                rw_check = True  
            else:
                rw_check = False
        
        except ValueError:
            # int(str) raises ValueError
            print("Please enter your SAT Reading & Writing Score again.\n ")
            rw_check = True
            
    # Split state_results math
    college_records[['SAT_Math_Low', 'SAT_Math_High']] = college_records['SAT Math'].str.split("-",expand=True)
    
    # Split state_results RW
    college_records[['SAT_RW_Low', 'SAT_RW_High']] = college_records['SAT R/W'].str.split("-",expand=True)
    
    
    # convert SAT_Math_Low to int
    college_records['SAT_Math_Low'] = pd.to_numeric(college_records['SAT_Math_Low'], errors='coerce')
    college_records = college_records.dropna(subset=['SAT_Math_Low'])
    college_records['SAT_Math_Low'] = college_records['SAT_Math_Low'].astype(int)
    
    # convert SAT_RW_Low to int
    college_records['SAT_RW_Low'] = pd.to_numeric(college_records['SAT_RW_Low'], errors='coerce')
    college_records = college_records.dropna(subset=['SAT_RW_Low'])
    college_records['SAT_RW_Low'] = college_records['SAT_RW_Low'].astype(int)
    
    # Filter by state, then by math, then by read/write
    # Filter college_records by state
    state_df = college_records[(college_records['state'] == user_state)]
    
    # Filter state_df by math scores    
    math_df = state_df[(state_df['SAT_Math_Low'] <= SAT_math)]
    # Filter state_df by rw scores
    rw_df = state_df[(state_df['SAT_RW_Low'] <= SAT_rw)]
    # Filter rw_df by math scores - this dataframe has colleges that match both scores
    math_rw_df = rw_df[(rw_df['SAT_Math_Low'] <= SAT_math)]
    
    print("="*col)
    print("\n")
    
    # if user math & read/write scores do not return any schools then notify user
    # also, if there are 10 or less schools in the given state with SAT data then
    # notify user there are not many schools to evaluate with their profile
    # and consider another state
    if math_df.empty and rw_df.empty:
        print("Sorry, there are no schools in " + user_state + " that matched your profile.\n")
         
        len_count = len(state_df['state'] == user_state)
        
        if len_count < 11:
            
            print("There are only " + str(len_count) + " colleges in " + user_state + " where SAT score data is available:")
            
            for i in state_df.index:
                print(state_df.loc[i]['College Name'])
                
        print("\nYou may want to consider evaluating colleges in another state.")
    
    # if no schools in state return user read/write scores, but math scores then
    # notify user of the schools that match their math scores
    elif rw_df.empty and not math_df.empty:
        print("Sorry, no schools in " + user_state + " matched your Read & Write scores. But these schools match your Math scores.\n")
        
        display_df(math_df)
        
    # if no schools in state return user math scores, but read/write scores then
    # notify user of the schools that match their read/write scores
    elif math_df.empty and not rw_df.empty:
        print("Sorry, no schools in " + user_state + " matched your Math scores. But these schools match your Read & Write scores.\n")
        
        display_df(rw_df)
    
    # if there are schools that match both math & read/write then notify the user
    # the schools that match their complete profile.
    # also, notify user of the schools that matched their math & read/write
    # as the "overlap" df may not display scores that match a school with just
    # one match in math or read/write
    else:
        print("Congratulations, these schools in " + user_state + " match your profile!\n")
                   
        display_df(math_rw_df)
        
        
        print("\nThese schools match your Math scores.\n")
        
        display_df(math_df)
        
        print("\nThese schools match your Read & Write scores.\n")
        
        display_df(rw_df)

    # redirect user to main module where they choose to build another profile
    # or try another option
    print ("\nRedirecting to Main Module...")
    print("\n")
    mp.main_app()
    
def display_df(df):
    
    # function to print dataframe of math or read/write scores or both
    # dataframe is passed and then the applicable columns are printed to terminal
    
    header = '{:5s}{:55s}{:10s}{:10s}'.format('Rank', 'College Name', 'SAT Math', 'SAT R/W')
    
    print(header)
    
    for i in df.index:
        df_str = '{:5s}{:55s}{:10s}{:10s}'.format(df.loc[i]['rank'], df.loc[i]['College Name'], str(df.loc[i]['SAT Math']), str(df.loc[i]['SAT R/W']))
        print(df_str)



if __name__ == "__main__":
    profile_search()
