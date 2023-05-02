import pathlib
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from app.utils.helpers import find_csvs, get_indexes


def get_files_with_null(files, thresh):
    """
    get
    Args:
        files (_type_): _description_
        thresh (_type_): _description_

    Returns:
        _type_: _description_
    """
    bad_files = []
    good_files = []

    for file in files:
        # read csv into dataframe
        df = pd.read_csv(file)
        # get the row rate
        row_rate = df.isnull().sum(axis=1)/len(df.columns)
        # get the indexes
        s = get_indexes(row_rate, thresh)

        # get the files in output list
        if len(s) != 0:
            bad_files.append(file)
        else:
            good_files.append(file)

    return bad_files, good_files


# read csv files
csv_files = find_csvs("./rawdata")

# find files with null rate higher than a certain value
bad_files, good_files = get_files_with_null(csv_files, 0.8)

print("files with high null rate, total: " + str(len(bad_files)))
for file in bad_files:
    print(file)


def clean_bad_files(files):
    for file in files:
        # read the CSV file into a pandas dataframe
        df = pd.read_csv(file)

        # calculate the percentage of null values per row
        null_percentage = df.isnull().sum(axis=1) / len(df.columns)

        # filter out rows where null rate per row is higher than 70%
        filtered_df = df[null_percentage <= 0.8]

        if filtered_df.empty:
            continue
        else:
            # get the new name for the path
            name = os.path.basename(file)
            output_dir = os.path.dirname(file)
            output_dir = output_dir.replace("rawdata", "basic_filtered_data")

            # create directories first
            os.makedirs(output_dir, exist_ok=True)

            # write the filtered dataframe to a new CSV file
            new_csvname = os.path.join(output_dir, name)
            filtered_df.to_csv(new_csvname)


def export_clean_files(files):
    for file in files:
        df = pd.read_csv(file)

        if df.empty:
            continue

        if len(df.columns) <= 1 or len(df.index) <= 1:
            continue

        name = os.path.basename(file)
        output_dir = os.path.dirname(file)
        output_dir = output_dir.replace("rawdata", "basic_filtered_data")

        # create directories first
        os.makedirs(output_dir, exist_ok=True)

        # write the filtered dataframe to a new CSV file
        new_csvname = os.path.join(output_dir, name)
        df.to_csv(new_csvname)


# clean bad files and export them to the desitination place
clean_bad_files(bad_files)
export_clean_files(good_files)


# name = input("Automatically modify the files? (y or n)")


# try:
#     if name == "y":
#         # modify the file
#         pass
#     elif name == "n":
#         # put the data directly to directory
#         exit()
#     else:
#         raise ValueError("Invalid input. Please enter either 'y' or 'n'.")
# except ValueError as e:
#     print(e)
