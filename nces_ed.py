"""
NCES Data Scrape Module
Group 5
@author: Joe Holleran
12/02/2021
"""
from urllib.request import urlopen  
from bs4 import BeautifulSoup
import pandas as pd

# Import nces_ed and call get_nces_data to return a csv of nces college data

def get_nces_data():
    
    # initialize list for dataframe
    nces_ls = []
    
    # nces ids and state for colleges to build link
    id_file = 'nces_ids.txt'
    
    # open ids/state file to loop through to build link
    file_in = open(id_file, 'rt', encoding='utf-8')
    
    # string to notify user the data collection process has started 
    # and can take up to 1 hour    
    print("""
          
          The NCES.ed.gov data is currently being gathered.
         
          Please be patient as the data collection process can take up to 1 hour.
         
          Thank you!
          
          """)

    for line in file_in:
        
        # initialize list for 1 college data
        interim_ls = []
        
        # get college id, state from file to build link
        id_ls = line.strip('\n')
        college_id = id_ls[0:6]
        college_state = id_ls[7:9]
        
        try:
            # build link for BeautifulSoup
            college_url = 'https://nces.ed.gov/collegenavigator/?s=' + str(college_state) + '&id=' + str(college_id)

            html = urlopen(college_url)
            bsyc = BeautifulSoup(html.read(), "lxml")
            
            # use BS to get college name info
            college_name = bsyc.find("div", {"class":"dashboard"}).find("span", {"class":"headerlg"})
            college_name = college_name.getText()
            # append id, name, state to file
            interim_ls.append(college_id)
            interim_ls.append(college_name)
            interim_ls.append(college_state)
            # length of college name
            l = len(college_name)
            
            # use BS to get college address
            college_address = bsyc.find("div", {"class":"dashboard"}).find("span", {"style":"position:relative"})
            college_address = college_address.getText()[l:]
            college_address = remove_commas(college_address)
            # append college address to file
            interim_ls.append(college_address)
            
            # use BS to get phone number, website, type, awards offered,
            # campus housing, student population, student faculty ratio
            other_list = bsyc.find('table', {'class' : 'layouttab'})

            for word in other_list.contents:
                for w in word.children:
                    new_word = w.text
                    # remove data field headings, but also removes campus setting
                    if ':' not in new_word:
                        new_word = remove_commas(new_word)
                        interim_ls.append(new_word)
            
            # append 1 college data to list of lists
            nces_ls.append(interim_ls)
            
        except:
            # if error thrown (link does not work) add id, name, state to list
            interim_ls.append(college_id)
            interim_ls.append("Institution could not be found.")
            interim_ls.append(college_state)
            nces_ls.append(interim_ls)
    
    # close id, state file
    file_in.close()
    
    # create header list
    header = ['nces_id', 'College Name', 'state', 'address', 'phone_number', 'website', 'type', 'awards_offered', 'campus_housing', 'student_population', 'student_faculty_ratio']
    
    # build pandas DataFrame from list of lists     
    nces_df = pd.DataFrame(nces_ls, columns=header)
    # write pandas DataFrame to CSV file
    nces_df.to_csv("nces_data.csv", index=False)
    
    # string to let user know the data collection has finished
    print("""
          The NCES.ed.gov data collection process has finished.
          
          """)
                        
def remove_commas(line):
    
    # function to remove commas from data fields
    
    line = line.replace(",", "")
    
    return line
                    

# run program if not imported
if __name__ == "__main__":    
    get_nces_data()
    