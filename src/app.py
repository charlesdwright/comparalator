import numpy as np
import pandas as pd
import math
import time

import dash
import dash_core_components as dcc
import dash_html_components as html
#import dash_table_experiments as dt
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import dash_table
from dash_table.Format import Format, Group, Scheme

import plotly.express as px

from funcs.funcs import *
from layout.layout import *
from data.data import *
#==============================================
from urllib.request import urlopen
import json
import random
#==============================================

df=df()

dfRange=[0,1]
range_state={}
#FA=r'./assets/css/font-awesome-4.7.0/css/font-awesome.min.css'
FA=r'./assets/css/font-awesome.min.css'

app = dash.Dash(external_stylesheets=[dbc.themes.CYBORG, FA])

app.layout = \
dbc.Container\
([
    html.Br(),
     row_1,
     row_2,
     row_3,
     row_4,
     row_5,
])

#================ good bad & ugly ====================
@app.callback(
    Output("graph", "figure"),
    Output('data-table', 'data'),
    Output('data-table', 'columns'),
    Output('range-slider', 'value'),
    [Input('operand_0', 'value'),
    Input('operator', 'value'),
    Input('operand_1', 'value'),
    Input('range-slider', 'value'),
    Input('day-slider', 'value'),
    Input('hour-slider', 'value')]
    #,prevent_initial_call=True
    )
def display_animated_graph(operand_0, operator, operand_1, range, day, hour):
    if (not operand_0 or not operand_1):
        print("operand is nothing")
        #do nothing

    try:
        print(operand_0 + "  " + dataHeaders[operand_0])
    except:
        pass
        print("error  " + str(operand_0))

    ctx = dash.callback_context
    range_state['top']=ctx.inputs['range-slider.value'][1]
    range_state['bot']=ctx.inputs['range-slider.value'][0]

    print("+++++++++++++++++")
    print("day " + str(day) + " " + "hour " + str(hour))
    global dfRange
    print("dfrange before " + str(dfRange) + "  " + str(range))
    dfRange = setRange(range, dfRange)
    print("dfrange after " + str(dfRange) + "  " + str(range))
    print("+++++++++++++++++")

    filtered_df = df[(df.day == day)&(df.hour == hour)]

    filtered_df=filtered_df.groupby(['location','day','hour']).agg({'fips':'last','layer':'max','trumpd':'last','ab_trumpd':'last','bidenj':'last','ab_bidenj':'last'})
    filtered_df=filtered_df.reset_index()

    try:
        filtered_df['result']=eval('filtered_df["' + dataHeaders[operand_0] + '"]' + operator + '(filtered_df["' + dataHeaders[operand_1] + '"]+1)')
    except:
        filtered_df['result']=-1

    filtered_df_1 = filtered_df[(filtered_df['result']<= filtered_df['result'].max()*dfRange[1]) & (filtered_df['result']>= filtered_df['result'].max()*dfRange[0])]

    dfMax = filtered_df['result'].max()*dfRange[1]
    dfMin = filtered_df['result'].max()*dfRange[0]

    print("---------")
    if filtered_df_1['result'].empty:
#        recreate filtered_df w/zeroes in 'result'
        print("dfMin " + str(dfMin) + "   dfMax " + str(dfMax))
        print('df is empty...')
        filtered_df['fips']=''
    else:
        print('df Not empty...')
        filtered_df=filtered_df_1
        print("dfMin " + str(dfMin) + "   dfMax " + str(dfMax))
    print("---------")

    pd.set_option("display.max_rows", None, "display.max_columns", None)

    top ='{:0.2f}'.format(dfMax * dfRange[1])
    bottom ='{:0.2f}'.format(dfMin * dfRange[0])

    tic = time.perf_counter()
    fig = px.choropleth(
        filtered_df, geojson=counties,
        locations='fips',
        color='result',
        range_color=(dfMin, dfMax),
        color_continuous_scale=getColor(operand_0,operand_1),
        scope="usa",
        )
    toc = time.perf_counter()

    data_table=updateDataTable(filtered_df,operation[operator])
    theTitle=operation[operator]

    fig.update_layout(coloraxis_colorbar=dict(
        title=theTitle,
        thicknessmode="pixels", thickness=25,
        lenmode="pixels", len=280,
        yanchor="top", y=1,
        tickmode="linear",
        tickfont_size=10,
        dtick=dfMax-dfMin,
        nticks=1,
        tick0=dfMin
    ))

    print('dtick ' + str(dfMax-dfMin) + "  tick0 " + str(dfMax))

    print(f"Completed update function in {toc - tic:0.4f} seconds")

    return fig, data_table[0], data_table[1], dfRange #animations[s]

#================ end good bad & ugly ====================

# functionality is the same for both dropdowns, so we reuse filter_options
app.callback(Output("operand_0", "options"), [Input("operand_1", "value")])(
    filter_options
)
app.callback(Output("operand_1", "options"), [Input("operand_0", "value")])(
    filter_options
)


if __name__ == "__main__":
    app.run_server(debug=True, port=8051, host='0.0.0.0')
