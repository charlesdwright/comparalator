import pandas as pd
import json
import ast

dataHeaders={'Trump':'trumpd','Trump Absentee':'ab_trumpd','Biden':'bidenj','Biden Absentee':'ab_bidenj'}
operation={'/':'Ratio (:1)','-':'Difference','+':'Sum'}

#theFile=r'/Users/cw/Dev/Misc Projects/Vote Comparator/src/content/info.txt'
theFile=r'./content/info.txt'
with open(theFile) as response:
    generalInfo = ast.literal_eval(response.read())

#theFile=r'/Users/cw/Dev/Misc Projects/Vote Comparator/src/data/counties.txt'
theFile=r'./data/counties.txt'
with open(theFile) as response:
    counties = json.load(response)


# make sure that x and y values can't be the same variable
def filter_options(v):
    """Disable option v"""
    return [
        {"label": key, "value": key, "disabled": key == v}
        for key in dataHeaders #iris.columns
    ]

def setRange(r_s,r_d):
    top=r_s[1]
    bot=r_s[0]

    if (top != 1):
        if(top != r_d[1]):
            print("updating top")
            r_d[1]=top

    if (bot != 0):
        if (bot != r_d[0]):
            print("updating bot")
            r_d[0]=bot

    #reset...
    if (top==bot):
        r_d=[0,1]

    #    return r_d
    # override the range-slider reset; uncomment above to invoke (but why?)
    return r_s

def getColor(operand_0,operand_1):
    color='gray'
    try:
        operand_0=operand_0.lower()
        operand_1=operand_1.lower()

        print(operand_0 + "  " + operand_1)

        if (operand_0 in operand_1) or (operand_1 in operand_0):
            if ('trump' in operand_0): color="PuBu"
            else: color="PuRd"
        else: #mixed
            if ('trump' in operand_0): color="PuBu" #"RdBu"
            else: color="PuRd"# "balance" colorscale #"oxy_r" #
    except:
        pass

    return color


def updateDataTable(filtered_df,operation):
    filtered_df['result']=pd.to_numeric(filtered_df.result, errors="coerce")

    b=filtered_df[filtered_df['fips']!='']
    b=b.groupby(['location','trumpd','ab_trumpd','bidenj','ab_bidenj','result']).agg({'fips':'last','layer':'last'})
    b=b.sort_values(by='result', ascending=False)
    b=b.reset_index()
    b['result']=b['result'].map('{:,.2f}'.format)
    b=b[['fips','location','trumpd','ab_trumpd','bidenj','ab_bidenj','result','layer']]
    b=b.sort_index()
    data=b.to_dict('records')
    columns=[
        {"name": ["Location", "FIPS"], "id": "fips"},
        {"name": ["Location", ""], "id": "location"},
        {"name": ["Votes", "Trump"], "id": "trumpd"},
        {"name": ["Votes", "Biden"], "id": "bidenj"},
        {"name": ["Absentee Votes", "Trump"], "id": "ab_trumpd"},
        {"name": ["Absentee Votes", "Biden"], "id": "ab_bidenj"},
        {"name": ["Result",operation], "id": "result","type":"numeric"},
        {"name": ["Time", "Day.Hour"], "id": "layer","type":"numeric"},
    ]
    return data,columns
