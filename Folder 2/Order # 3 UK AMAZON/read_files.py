import pandas as pd


def read_csv():
    df=pd.read_csv('zillow.csv')
    return df['links'].values.tolist()