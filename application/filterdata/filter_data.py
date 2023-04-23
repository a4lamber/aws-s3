import pathlib
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from find_csvs import find_csvs

def get_indexes(series,thresh):
    """
    get the indexes of the series where it is greater
    than certain values.
    Args:
        thresh (_type_): _description_
        series (_type_): _description_

    Returns:
        _type_: _description_
    """
    mask = series > thresh
    return np.where(mask)[0].tolist()


def get_files_with_null(files,thresh):

    output = []

    for file in files:
        # read csv into dataframe
        df = pd.read_csv(file)    
        # get the row rate
        row_rate = df.isnull().sum(axis=1)/len(df.columns)
        # get the indexes
        s = get_indexes(row_rate,thresh)

        # get the files in output list
        if len(s) != 0:
            output.append(file)

    return output

# read csv files
csv_files = find_csvs("./rawdata")
# find files with null rate higher than a certain value
problem_files = get_files_with_null(csv_files,0.8)

print("files with high null rate, total: " + str(len(problem_files)-1))
for file in problem_files:
    print(file)


name = input("Automatically modify the files?")

if name == "y":
    """
    do something to modify the files
    """
    pass