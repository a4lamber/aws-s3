from pyspark.sql.types import StructType, StructField, IntegerType, StringType, TimestampType, DoubleType

def rename_columns(data,from_cols,to_cols):
    """map a dataframe with original columns to destination columns

    :param _type_ data: pyspark dataframe
    :param list from_cols: list of original name
    :param list to_cols: list of destination name
    :return _type_: renamed dataframe 
    """
    
    for i in range(len(from_cols)):
        # if columns names are different, then dump in mapper
        if from_cols[i] != to_cols[i]:
            data = data.withColumnRenamed(from_cols[i],to_cols[i])
    
    return data


def create_schema(pandas_types, mappers, column_names):
    """
    map pandas data types such as int and float to pyspark dtypes such as .
    
    :param list pandas_types: pandas_types
    :param dict mappers: a mapper
    :param list column_names: column names you wish to put in the schema
    :return pyspark.sql.types.StructType: _description_
    """
    # map from pandas datatype to pyspark dtype
    data_types = [mappers[type] for type in pandas_types]    
    
    # create fields
    fields = [StructField(name, dataType) for name, dataType in zip(column_names, data_types)]
    schema = StructType(fields)

    return schema


def cast_schema(df,schema):
    """

    :param _type_ df: _description_
    :param _type_ schema: _description_
    :return _type_: _description_
    """
    df_casted = df.select([df[field.name].cast(field.dataType) for field in schema.fields])
    
    return df_casted



def write_to_db(data_frame, table_name, db_name, db_usrname, db_pssword,port):
    data_frame.write.format('jdbc').options(
              url=f'jdbc:postgresql://localhost:{port}/{db_name}',
              driver='org.postgresql.Driver',
              dbtable=table_name,
              user=db_usrname,
              password=db_pssword).\
              mode('overwrite') \
              .save()