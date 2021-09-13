import numpy as np
import pandas as pd


#from flask_caching import Cache
# TIMEOUT=20
#
# cache = Cache(app.server, config={
#     'CACHE_TYPE': 'filesystem',
#     'CACHE_DIR': 'cache-directory'
# })

#@cache.memoize(timeout=TIMEOUT)

def df():
#    theFile =r'/Users/cw/Dev/Misc Projects/Vote Comparator/src/data/nov3_time_series_sequential.json'
    theFile =r'./data/nov3_time_series_sequential.json'
    df=pd.read_json (theFile, dtype={'fips': str})

    df['layer']=pd.to_numeric(df.layer, errors="coerce")

    #isolate day and hour from layer. it's a bit more difficult than it should be
    df['day']=df['layer'].astype(int)
    #dealing w/accidental ceiling and flooring when dealing w/dec portion of float64
    df['hour']=((df['layer'].round(2)-df['day'])*100).round(0).astype(int)

    return df


#
# #@cache.memoize(timeout=TIMEOUT)
# def df_1(day, hour):
#
# #    df=df()
#     df=df[(df['day'] == day)&(df['hour'] == hour)]
#
#     return df
