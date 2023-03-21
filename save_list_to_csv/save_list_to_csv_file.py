#
#
#
# This script will help me save data to CSV file
#
#
#
import csv
import pandas as pd
#
#
# 
def save_data_to_csv_files(keyword, data_for_csv: list) -> None:
    """
    This function add a list to CSV file. 
    Parameter "keyword" need for custom CSV file name.
    """
    
    headers = ['Site', 'h1', 'h2_list', 'h3_list', 'Meta_content', 'Meta_description']
    df = pd.DataFrame(data_for_csv, columns=headers)
    df.to_csv(f"{keyword}.csv", encoding="utf8")
    
    return f"Done with keyword {keyword}"