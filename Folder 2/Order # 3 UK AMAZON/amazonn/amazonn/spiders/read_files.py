import pandas as pd


def read_csv():
    df=pd.read_csv('Zillow.csv')
    return df['links'].values.tolist()