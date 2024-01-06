"""
Group Project: Group 5
Author     :   Antara Saha 
Updated By :              
Specification: This script is to merge all the extracted data from different datasources. To create
               a final merge file "final_college_data.csv"
"""

# Import libraries
import pandas as pd

def final_data_merge():
    
    # reading csv files
    data1 = pd.read_csv('US_Ranking_Data.csv',encoding = "ISO-8859-1")
    data2 = pd.read_csv('nces_data.csv',encoding = "ISO-8859-1")
    data3 = pd.read_csv('SAT_Data.csv',encoding = "ISO-8859-1")
    data4 = pd.read_csv('Admissions_deadline.csv',encoding = "ISO-8859-1")
    data5 = pd.read_csv('niche_college_data.csv',encoding = "ISO-8859-1")


    # using merge function by setting how='left'
    output2 = pd.merge(data1, data2,
                    on='College Name', 
                    how='left')

    output2 = pd.merge(output2, data3,
                    on='College Name', 
                    how='left')

    output2 = pd.merge(output2, data4,
                    on='College Name', 
                    how='left')

    output2 = pd.merge(output2, data5,
                    on='College Name', 
                    how='left')

    output2.dropna(subset = ["College Name"], inplace=True) #drop rows where college name is null
    output2 = output2.drop_duplicates(subset=["College Name"] ,keep = 'first' )

    # Create final csv file
    output2.to_csv('final_college_data.csv',encoding='utf-8',index = False, header= True) 

if __name__ == "__main__":
    final_data_merge()
