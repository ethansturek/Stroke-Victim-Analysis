import pandas as pd
import numpy as np
def load_and_process(url_or_path_to_csv_file):

    df1 =( #load and drop any useless information
            pd.read_csv(
                url_or_path_to_csv_file
            )
            .drop(
                ['id'], axis=1  
            )
    )
    df2 = ( #filters outliers and remaps values
            df1   
            .loc[lambda x: x['bmi']<60]
            .replace({'ever_married': {'Yes': 1, 'No': 0}})
          )
    return df2

def percentage(df, sdf, column, value):
    heartmax= df[df[column] == value]
    hmax = heartmax[column].count()
    snonheartmax= sdf[sdf[column] == value]
    snhmax = snonheartmax["work_type"].count()
    return (snhmax/hmax* 100)
