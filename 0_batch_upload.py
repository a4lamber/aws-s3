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
from app.utils.helpers import find_csvs


def main(local_directory_name, bucket_name):
    """
    The script upload local data up to the raw s3 bucket
    """

    # Set up credentials to the s3 buckets
    s3 = boto3.client('s3')
 
    # get a list of csv files
    csv_files = find_csvs(local_directory_name)

    # upload csv and csv.gz files up to the s3 bucket
    for csv_file in csv_files:
        # local directory_path, bucket name, s3 path
        s3.upload_file(csv_file, bucket_name, csv_file)


if __name__ == "__main__":
    # upload to "ehr-raw" bucket filtered
    main(local_directory_name="./basic_filtered_data/",
         bucket_name='ehr-basic-filtered')
