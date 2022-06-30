import pandas as pd

def preprocess(df,region_df):
    #filtering for Summer Olympic only
    df = df[df['Season'] == 'Summer']
    #merging with region_df
    df = df.merge(region_df, on='NOC', how='left')
    #dropping the duplicates rows
    df.drop_duplicates(inplace=True)
    #One Hot Encoding Medals
    df = pd.concat([df, pd.get_dummies(df['Medal'])], axis=1)
    return df

