# this script will attempt to strip the Postcode file and create
# a local database of all the postcodes. 

import pandas as pd

def clean_table(df):
    df.New_PostCode_2 = df.New_PostCode.fillna(method='ffill')
    df.Ward_2 = df.Ward.fillna(method='ffill')
    df.Old_PostCode_2 = df.Old_PostCode.fillna(method='ffill')
    df.PostCode_Prefix_2 = df.Postcode_Prefix.fillna(method='ffill')
    
    print (df.head(5))
    return df

def read_table(filename):
    df = pd.read_csv(filename)
    
    return df


def main():
    # Read the cleaned CSV file with the right columns.
    
    filename = 'PostCode_clean.csv'
    OG_postcode_table = read_table(filename)
    
    # Clean up the empty rows and perform the forward fill function. 
    postcode_table = clean_table(OG_postcode_table)
    
main()
    
    