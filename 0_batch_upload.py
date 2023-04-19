'''
 # @ Author: Yixiang Zhang
 # @ Create Time: 2023-04-17 15:30:49
 # @ Modified by: Yixiang Zhang
 # @ Modified time: 2023-04-18 21:46:56
 # @ Description: Upload the data to the cloud
 '''


import boto3
import os
import pathlib

def find_csvs(data_direcotry):
    """
    find every .csv and .csv.gz file in the directory and return it
    as a list
    Args:
        data_direcotry (_type_): _description_

    Returns:
        _type_: _description_
    """
    # Define the directory to search in
    path = pathlib.Path(data_direcotry)

    # Find all .csv and .csv.gz files in the directory
    gz_files = list(path.rglob('*.csv.gz'))

    csv_files = list(path.rglob('*.csv'))
    
    # # merge two list
    files = csv_files + gz_files

    # # convert from POSIX to str
    files = [str(file) for file in files]
    return files

def main():
    """
    The script upload local data up to the raw s3 bucket
    """
    # local directories and more
    LOCAL_DIRECTORY_NAME = "./rawdata/"
    RAW_BUCKET_NAME = 'ehr-raw'


    # Set up credentials to the s3 buckets
    s3 = boto3.client('s3')

    # get a list of csv files
    csv_files = find_csvs(LOCAL_DIRECTORY_NAME)
    
    # upload csv and csv.gz files up to the s3 bucket
    for csv_file in csv_files:
        s3.upload_file(csv_file,RAW_BUCKET_NAME,csv_file)
    
if __name__ =="__main__":
    main()