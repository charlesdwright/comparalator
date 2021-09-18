import numpy as np
import pandas as pd

# def df():
#     theFile =r'./data/nov3_time_series_sequential_full.json'
#     df=pd.read_json (theFile, dtype={'fips': str})
#
#     print(df.head())
#
#     df['layer']=pd.to_numeric(df.layer, errors="coerce")
#
#     #isolate day and hour from layer. it's a bit more difficult than it should be
#     df['day']=df['layer'].astype(int)
#     #dealing w/accidental ceiling and flooring when dealing w/dec portion of float64
#     df['hour']=((df['layer'].round(2)-df['day'])*100).round(0).astype(int)
#
#     return df

#memory-lite chunk
def df():
    theFile =r'./data/nov3_time_series_full.csv'

    # read the large csv file with specified chunksize
    df_chunk = pd.read_csv(theFile, chunksize=10000, dtype={'fips': str})

    chunk_list = []  # append each chunk df here

    # Each chunk is in df format
    for chunk in df_chunk:
        #print(len(chunk))
        chunk_list.append(chunk)

    # concat the list into dataframe
    df_concat = pd.concat(chunk_list)

    print(df_concat.head())

    df_concat['layer']=pd.to_numeric(df_concat.layer, errors="coerce")

    #isolate day and hour from layer. it's a bit more difficult than it should be
    df_concat['day']=df_concat['layer'].astype(int)
    #dealing w/accidental ceiling and flooring when dealing w/dec portion of float64
    df_concat['hour']=((df_concat['layer'].round(2)-df_concat['day'])*100).round(0).astype(int)

    return df_concat
