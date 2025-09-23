import pandas as pd

def preprocess(df, region_df):

    #filtering for summer olympics
    df=df[df['Season']== 'Summer']
    #merge with region_df
    df=df.merge(region_df,on='NOC',how='left')
    #droping duplicated
    df.drop_duplicates(inplace=True)
    #one hot encoding melads
    df = pd.concat([df, pd.get_dummies(df['Medal']).astype(int)], axis=1)

    return df