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
# theFile=r'/Users/cw/Dev/Misc Projects/Vote Comparator/data/counties.txt'
# with open(theFile) as response:
#     counties = json.load(response)
#==============================================

#theFile =r'/Users/cw/Dev/Misc Projects/Election Data/nov3_time_series_sequential.json'
# theFile =r'/Users/cw/Dev/Misc Projects/Vote Comparator/data/nov3_time_series_sequential.json'
# df = pd.read_json (theFile, dtype={'fips': str})
# df['layer']=pd.to_numeric(df.layer, errors="coerce")
# #isolate day and hour from layer. it's a bit more difficult than it should be
# df['day']=df['layer'].astype(int)
# #dealing w/accidental ceiling and flooring when dealing w/dec portion of float64
# df['hour']=((df['layer'].round(2)-df['day'])*100).round(0).astype(int)

#dataHeaders={'Trump':'trumpd','Trump Absentee':'ab_trumpd','Biden':'bidenj','Biden Absentee':'ab_bidenj'}

df=df()

dfRange=[0,1]
range_state={}
FA=r'/Users/cw/Dev/Misc Projects/Vote Comparator/assets/css/font-awesome-4.7.0/css/font-awesome.min.css'

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
#     row_x,
    # html.Br(),
    #     html.Div(
    #         className="div-row-1",
    #         children=[
    #
    #         dbc.Row(
    #         [
    #             dbc.Col(
    #                 [
    #
    #
    #                 html.Label("Vote Compar-a-lator",className='div-title',id='div-title-label'),
    #
    #                     #dbc.Button("row 1 col 1-12",style={"width":"100%"})
    #                 ]), #width=12,style={'paddingRight':'3px','paddingLeft':'3px'}),
    #
    #         ]),
    #         ]),

#    html.Br(),
        # html.Div(
        #     className="div-row-1",
        #     children=[
        #         html.Label("2020 US Election Vote Comparator",className='div-label',id='div-calc-label'),
        #         dbc.Row([
        #             dbc.Col(
        #                 [
        #                 dbc.ButtonGroup(
        #                     [
        #                     # dbc.FormGroup(
        #                     #     [
        #                     #     dcc.Dropdown(
        #                     #         id='operand_0',
        #                     #         className='dropdown',
        #                     #         options=[
        #                     #             {"label": key, "value": key} for key in dataHeaders #iris.columns
        #                     #         ],
        #                     #         value="Biden",
        #                     #     ),
        #                     #     ]
        #                     # ),
        #                     # html.Div(
        #                     #     [
        #                     #     dbc.RadioItems(
        #                     #         id="operator",
        #                     #         className="btn-group",
        #                     #         labelClassName="btn btn-secondary",
        #                     #         labelCheckedClassName="active",
        #                     #         options=[
        #                     #             {"label": "/", "value": "/"},
        #                     #             {"label": "-", "value": "-"},
        #                     #             {"label": "+", "value": "+"},
        #                     #         ],
        #                     #         value='/',
        #                     #     ),
        #                     #     html.Div(id="output"),
        #                     #     ],
        #                     #     className="radio-group",
        #                     # ),
        #                     dbc.FormGroup(
        #                         [
        #                         # dcc.Dropdown(
        #                         #     id='operand_1',
        #                         #     className='dropdown',
        #                         #     options=[
        #                         #         {"label": key, "value": key} for key in dataHeaders #iris.columns
        #                         #     ],
        #                         #     value="Trump",
        #                         # ),
        #                         ]
        #                     ),
        #                     ] #end button-group
        #                 ),
        #                 ],
        #             ),
        #         ]),
        #     ]),

    #html.Br(),

    # html.Div(
    #     className="div-row-2",
    #     children=[
    #         dbc.Row([
    #                 #graph here
    #             # dbc.Col(
    #             #     [
    #             #     dcc.Loading(
    #             #         id="loading-1",
    #             #         type="default",
    #             #         children=[
    #             #             html.Div(className ='div-graph', children=[
    #             #                 dcc.Graph(id="graph"),
    #             #             ]),
    #             #         ],
    #             #     ),
    #             #     ], width=11),
    #
    #             # dbc.Col(
    #             #     [
    #             #     html.Div(
    #             #        className="div-range-slider",
    #             #        children=
    #             #        [
    #             #             dcc.RangeSlider(
    #             #             className="range-slider",
    #             #             id='range-slider',
    #             #             vertical=True,
    #             #             min=0,
    #             #             max=1,
    #             #             step=0.01,# None,# 10,
    #             #             value=[0, 1],
    #             #             verticalHeight=282,
    #             #             tooltip = { 'always_visible': False },
    #             #             allowCross=False,
    #             #             persistence=True,
    #             #             persistence_type='local'
    #             #             ),
    #             #        ],
    #             #     ),
    #             #     ], width=1),
    #             ]),
    #         ]),

    # html.Br(),
    # dbc.Row([
    #     # dbc.Col(
    #     # [
    #     # html.Div(
    #     #     className="div-time-sliders",
    #     #     children=
    #     #     [
    #     #     html.Label("Day",className='div-label'),
    #     #     dcc.Slider(
    #     #         className='day-slider',
    #     #         id='day-slider',
    #     #         min=df['day'].min(),
    #     #         max=df['day'].max(),
    #     #         value=df['day'].min(),
    #     #         marks={str(day):str(day)+"/Nov" for day in df['day'].unique()},
    #     #         ),
    #     #     html.Label("Hour",className='div-label'),
    #     #     dcc.Slider(
    #     #         id='hour-slider',
    #     #         min=df['hour'].min(),
    #     #         max=df['hour'].max(),
    #     #         value=df['hour'].max(),
    #     #         marks={str(hour):str(hour) for hour in df['hour'].unique()},
    #     #         ),
    #     #     ],
    #     # ),
    #     # ],width=12),
    # ]),

    #     html.Div(
    #         className="div-row-5",
    # #         children=[
    # #             html.Label("Data",className='div-label',id='div-data-label'),
    # #             dbc.Row(
    # #             [
    # #                 dbc.Col(
    # #                     [
    # #                     dash_table.DataTable(
    # #                         id='data-table'
    # #                         ,page_action="native"
    # #                         ,page_current= 0
    # #                         ,page_size= 10
    # #                         ,filter_action='native'
    # #                         ,columns=[]
    # #                         ,data=[]
    # #                         ,merge_duplicate_headers=True
    # #                         ,style_data={'overflow': 'hidden'}
    # #                         ,style_header={'textAlign': 'center'}
    # #                         ,style_cell={
    # #                             'textAlign': 'right'
    # #                             ,'padding':'5px'
    # #                             }
    # #                         ,style_cell_conditional=[
    # #                             {
    # #                                 'if': {'column_id': 'location'}
    # #                                 ,'textAlign': 'left'
    # #                                 ,'textOverflow': 'ellipsis'
    # #                                 ,'maxWidth': 200
    # #                             },
    # #                             {
    # #                                 'if': {'column_id': 'fips'}
    # #                                 ,'textAlign': 'left'
    # #                             },
    # #                         ]
    # #                         ),
    # #                     ]), #width=12,style={'paddingRight':'3px','paddingLeft':'3px','textAlign':'center'}),
    # #             ]),
    # # ]
    # ),
])


# @app.callback(
#     Output("example-output", "children"), [Input("example-button", "n_clicks")]
# )
# def on_button_click(n):
#     if n is None:
#         return "Not clicked."
#     else:
#         return f"Clicked {n} times."

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

    #filtered_df = df_1(day, hour)

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
        title=theTitle, #"Results",
        thicknessmode="pixels", thickness=25,
        lenmode="pixels", len=280,
        yanchor="top", y=1,
        tickmode="linear",
        tickfont_size=10,
        dtick=dfMax-dfMin, #dfMax * (range[1]-range[0]),#
        nticks=1,
        tick0=dfMin #dfMax * (range[0])
    ))

    print('dtick ' + str(dfMax-dfMin) + "  tick0 " + str(dfMax))

    print(f"Completed update function in {toc - tic:0.4f} seconds")

    return fig, data_table[0], data_table[1], dfRange #animations[s]


#================ end good bad & ugly ====================



# # make sure that x and y values can't be the same variable
# def filter_options(v):
#     """Disable option v"""
#     return [
#         {"label": key, "value": key, "disabled": key == v}
#         for key in dataHeaders #iris.columns
#     ]

# functionality is the same for both dropdowns, so we reuse filter_options
app.callback(Output("operand_0", "options"), [Input("operand_1", "value")])(
    filter_options
)
app.callback(Output("operand_1", "options"), [Input("operand_0", "value")])(
    filter_options
)

# def setRange(r_s,r_d):
#     top=r_s[1]
#     bot=r_s[0]
#
#     if (top != 1):
#         if(top != r_d[1]):
#             print("updating top")
#             r_d[1]=top
#
#     if (bot != 0):
#         if (bot != r_d[0]):
#             print("updating bot")
#             r_d[0]=bot
#
#     #reset...
#     if (top==bot):
#         r_d=[0,1]
#
#     #    return r_d
#     # override the range-slider reset
#     return r_s
#
# def getColor(operand_0,operand_1):
#     color='gray'
#     if (operand_0 in operand_1) or (operand_1 in operand_0):
#         if ('trump' in operand_0): color="PuBu"
#         else: color="PuRd"
#     else: #mixed
#         if ('trump' in operand_0): color="PuBu" #"RdBu"
#         else: color="PuRd"# "balance" colorscale #"oxy_r" #
#
#     return color
#
#
# def updateDataTable(filtered_df):
#     filtered_df['result']=pd.to_numeric(filtered_df.result, errors="coerce")
#
#     # a=filtered_df[(filtered_df['result']<= t)
#     # & (filtered_df['result']>= b)]
#     b=filtered_df[filtered_df['fips']!='']
#     b=b.groupby(['location','trumpd','ab_trumpd','bidenj','ab_bidenj','result']).agg({'fips':'last','layer':'last'})
#     b=b.sort_values(by='result', ascending=False)
#     b=b.reset_index()
#     b['result']=b['result'].map('{:,.2f}'.format)
#     b=b[['fips','location','trumpd','ab_trumpd','bidenj','ab_bidenj','result','layer']]
#     b=b.sort_index()
#     data=b.to_dict('records')
#
#     columns=[
#         {"name": ["Location", "FIPS"], "id": "fips"},
#         {"name": ["Location", ""], "id": "location"},
#         {"name": ["Votes", "Trump"], "id": "trumpd"},
#         {"name": ["Votes", "Biden"], "id": "bidenj"},
#         {"name": ["Absentee Votes", "Trump"], "id": "ab_trumpd"},
#         {"name": ["Absentee Votes", "Biden"], "id": "ab_bidenj"},
#         {"name": ["Calc", "Value"], "id": "result","type":"numeric"},
#         {"name": ["Time", "Day.Hour"], "id": "layer","type":"numeric"},
#     ]
#     return data,columns

if __name__ == "__main__":
    app.run_server(debug=True, port=8051, host='0.0.0.0')
