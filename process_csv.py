import pandas as pd
import numpy as np
import os

extension = 'csv'
target_folder = r'./processed'

print(os.getcwd())

for filename in list(filter(lambda f: f.endswith('.'+extension), os.listdir("./datasets"))):
    print('Processing: ',filename)
    df = pd.read_csv(r'dataset2.csv')
    # split name field into first_name and last_name
    df[['first_name', 'last_name']] = df['name'].str.split(' ', 1, expand=True)

    # Delete any rows which do not have a name
    print('Number of empty names: ',len(df[df['name'].isna()]))
    print('Original df:',len(df))
    df = df.dropna(subset=['name'])
    print('Cleaned df:',len(df))

    # remove zeros prepended to price 
    print('Price is :',df.price.dtypes)
    if df.price.dtypes == object:
        df['price'] = df['price'].str.lstrip("0")
        df['price'] = pd.to_numeric(df["price"])

    # Create a new field named above_100, which is true if the price is strictly greater than 100
    df['above_100'] = (df['price'] > 100)
    df.head()

    if not os.path.exists(target_folder):
        os.makedirs(target_folder)
    result_file = target_folder + '/processed_' + filename
    df.to_csv(result_file)
    print('File save: ' ,result_file)
    print('\n')
    

    