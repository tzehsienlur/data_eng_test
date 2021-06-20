# Libraries
import pandas as pd
import numpy as np
import os
from datetime import datetime

# Created Files
from pkg.common.setup_logger import logger

# Constants
from pkg.data_pipeline.constants import TITLE_HASHMAP

# Read all excel or csv files dynamically
def read_all_files(path):
    logger.info("Executing read_all_files method.")
    result = []
    path = path + "/original"
    # Iterate through the entire folder to get only files with extension of 'csv' or 'xlsx'
    # and create a list of dataframes
    for root, dirs, files in os.walk(path):
        for filename in files:
            new_path = path + "/" + filename
            if (filename.endswith('.csv')):
                df = pd.read_csv(new_path, encoding="utf-8")
                split_filename = filename.split(".csv")
                df['filename'] = split_filename[0]
                result.append(df)
            elif (filename.endswith('.xlsx')):
                df = pd.read_excel(new_path, encoding="utf-8")
                split_filename = filename.split(".xlsx")
                df['filename'] = split_filename[0]
                result.append(df)

    return result

# Removing titles from the dataframe "name" column
def remove_title(row):
    for key, val in TITLE_HASHMAP.items():
        if key in row['name']:
            name = row['name'][len(key):]
        else:
            name = row['name']
    
    name = name.strip()
    return name

# Clean data to match the criteria
def clean_data(df):
    logger.info("Executing clean_data method.")
    # Remove Nan value found in "name" column
    df.dropna(subset = ["name"], inplace=True)
    # Remove the title in the name
    df['removed_title_name'] = df.apply(remove_title, axis=1)
    # Produce "first_name" and "last_name" columns data by using "removed_title_name" column data
    df[['first_name','last_name']] = df['removed_title_name'].str.split(" ", n=1, expand=True)

    # Convert price to numeric which will remove prepended "0" and create "above_100" column according to condition of "price" > 100
    df['price'] = df['price'].apply(pd.to_numeric)
    df['above_100'] = np.where(df['price'] > 100, True, False)

    # Addtional Add-on by Tze Hsien, "converted_price" is to round up the "price" data into 2 decimal place
    # as price is usually reflected up to 2dp unless purchase of crypto
    df['converted_price'] = df['price'].round(2)
    return df

# Create excel for processed data and storing in the format of "YYYYMMDD_<filename>.csv"
def create_excel(path, df):
    logger.info("Executing create_excel method.")
    curr_date = datetime.today().strftime('%Y%m%d')
    path = path + "/processed/" + curr_date + "_"  + df['filename'].loc[0] + ".csv"
    header = ["first_name", "last_name", "price", "converted_price", "above_100"]
    df[header].to_csv(path, index = False, encoding='utf-8')


def main(path):
    result = read_all_files(path)

    for df in result:
        clean_df = clean_data(df)
        create_excel(path, clean_df)
    logger.info("End of Preprocessing")
