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
