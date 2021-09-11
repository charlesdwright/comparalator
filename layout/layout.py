import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from funcs.funcs import *
from data.data import df
from layout.rows import *

import dash_table
from dash_table.Format import Format, Group, Scheme


row_1 = html.Div([
            dbc.Row
            (
                dbc.Col
                (
                    html.Div
                    (
                        id="div-row-1",
                        className="div-row-1",
                        children=
                        [
                            info_row("row-1","2x"),
                            content_row_1
                        ]
                    )
                )
            )
        ])

row_2 = html.Div([
            dbc.Row
            (
                dbc.Col
                (
                    html.Div
                    (
                        id="div-row-2",
                        className="div-row-2",
                        children=
                        [
                            info_row("row-2","lg"),
                            content_row_2
                        ]
                    )
                )
            )
        ])

row_3 = html.Div([
            dbc.Row
            (
                dbc.Col
                (
                    html.Div
                    (
                        id="div-row-3",
                        className="div-row-3",
                        children=
                        [
                            info_row("row-3","2x"),
                            content_row_3
                        ]
                    )
                )
            )
        ])

row_4 = html.Div([
            dbc.Row
            (
                dbc.Col
                (
                    html.Div
                    (
                        id="div-row-4",
                        className="div-row-4",
                        children=
                        [
                            info_row("row-4","lg"),
                            content_row_4
                        ]
                    )
                )
            )
        ])

row_5 = html.Div([
            dbc.Row
            (
                dbc.Col
                (
                    html.Div
                    (
                        id="div-row-5",
                        className="div-row-5",
                        children=
                        [
                            info_row("row-5","lg"),
                            content_row_5
                        ]
                    )
                )
            )
        ])

# row_1_x = html.Div(
#     [
#         dbc.Row(
#             dbc.Col(
#                 html.Div(
#                     id="div-row-1",
#                     className="div-row-1",
#                     children=[
#                         dbc.Row(
#                             [
#                                 content_row_1
#                                 dbc.Col(
#                                     html.Div([
#                                     html.Label("2020 US Election Vote Compar-A-Lator",className='div-label',id='div-title-label'),
#                                     ]),
#                                     ),
#                                 html.Div([
#                                     html.I(className="fa fa-info-circle fa-2x",id="row-1-info",**{'aria-hidden': 'true'}, children=None),
#                                     dbc.Popover(
#                                         popover_general,
#                                         id="pop-general",
#                                         target="row-1-info",
#                                         trigger="hover",
#                                         ),
#                                     ]),
#                             ]
#                         ),
#
#                     ],
#                 ),
#             )
#         ),
#     ]
# )
#
# row_2_x = html.Div(
#     [
#         dbc.Row(
#             dbc.Col(
#                 html.Div(
#                     className="div-row-2",
#                     children=[
#                     dbc.Row(
#                         [
#                             dbc.Col([
#                                 html.Div(
#                                     dropdown_0,
#                                     ),
#                                 ]),
#                             dbc.Col(
#                                 html.Div(
#                                     calc_buttons
#                                     )
#                                 ),
#                             dbc.Col(
#                                 html.Div(
#                                     dropdown_1,
#                                     ),
#                                 ),
#                         ]
#                     )],
#                 ),
#                 ),
#             ),
#     ]
# )
#
# row_3_x = html.Div(
#         [
#         dbc.Row(
#             dbc.Col(
#                 html.Div(
#                     id="div-row-3",
#                     className="div-row-3",
#                     children=[
#                         dbc.Row(
#                             [
#                             dbc.Col(
#                                 [
#                                 dcc.Loading(
#                                     id="loading-1",
#                                     type="default",
#                                     children=[
#                                         html.Div(className ='div-graph', children=[
#                                             dcc.Graph(id="graph"),
#                                         ]),
#                                     ],
#                                 ),
#                                 ], width=11),
#
#                                 dbc.Col(
#                                     [
#                                     html.Div([
#                                         html.I(className="fa fa-info-circle fa-2x",id="graph-info",**{'aria-hidden': 'true'}, children=None),
#                                         dbc.Popover(
#                                             popover_graph,
#                                             id="pop-graph",
#                                             target="graph-info",
#                                             trigger="hover",
#                                             ),
#                                         ]),
#                                     html.Div(
#                                        className="div-range-slider",
#                                        children=
#                                             [
#                                                 dcc.RangeSlider(
#                                                 className="range-slider",
#                                                 id='range-slider',
#                                                 vertical=True,
#                                                 min=0,
#                                                 max=1,
#                                                 step=0.01,# None,# 10,
#                                                 value=[0, 1],
#                                                 verticalHeight=282,
#                                                 tooltip = { 'always_visible': False },
#                                                 allowCross=False,
#                                                 persistence=True,
#                                                 persistence_type='local'
#                                                 ),
#                                             ],
#                                         ),
#                                     ], width=1),
#                                 ]
#                             ),
#
#                         ],
#                     ),
#                 )
#             ),
#         ]
#     )
#
# row_4_x = html.Div(
#     [
#         dbc.Row(
#             dbc.Col(
#                 html.Div(
#                     id="div-row-4",
#                     className="div-row-4",
#                     children=[
#
#                         dbc.Row(
#                             [
#                             dbc.Col(
#                                 [
#                                 html.Div(
#                                     className="div-time-sliders",
#                                     children=
#                                         [
#                                         html.Div(
#                                             [
#                                                 html.Label("Day",className='div-label'),
#                                             ],
#                                         className="slider-label",
#                                         ),
#                                         dcc.Slider(
#                                             className='day-slider',
#                                             id='day-slider',
#                                             min=df['day'].min(),
#                                             max=df['day'].max(),
#                                             value=df['day'].min(),
#                                             marks={str(day):str(day)+"/Nov" for day in df['day'].unique()},
#                                             ),
#                                         html.Div(
#                                             [
#                                                 html.Label("Hour",className='div-label'),
#                                             ],
#                                         className="slider-label",
#                                         ),
#                                         dcc.Slider(
#                                             id='hour-slider',
#                                             min=df['hour'].min(),
#                                             max=df['hour'].max(),
#                                             value=df['hour'].max(),
#                                             marks={str(hour):str(hour) for hour in df['hour'].unique()},
#                                             ),
#                                         ],
#                                     ),
#                                 ],width=11),
#
#                                 html.Div([
#                                     html.I(className="fa fa-info-circle fa-lg",id="time-sliders-info",**{'aria-hidden': 'true'}, children=None),
#                                     dbc.Popover(
#                                         popover_time_sliders,
#                                         id="pop-time-sliders",
#                                         target="time-sliders-info",
#                                         trigger="hover",
#                                         ),
#                                     ]),
#
#                             ]
#                         ),
#
#                     ],
#                 ),
#             )
#         ),
#     ]
# )
#
# row_5_x = html.Div([
#             dbc.Row
#             (
#                 dbc.Col
#                 (
#                     html.Div
#                     (
#                         id="div-row-5",
#                         className="div-row-5",
#
#                         children=
#                         [
#                             dbc.Row
#                             ([
#                                 dbc.Col
#                                 ([
#                                     # html.Div
#                                     # (
#                                     #     [
#                                     #         html.Label("Data",className='div-label',id='div-data-label'),
#                                     #         #html.Label("Data",className='div-label'),
#                                     #     ],
#                                     #
#                                     # className="slider-label",
#                                     # ),
#                                     #
#                                     # html.Div
#                                     # ([
#                                     #     html.I
#                                     #     (
#                                     #         className="fa fa-info-circle fa-lg",
#                                     #         id="data-table-info",
#                                     #         **{'aria-hidden': 'true'},
#                                     #         children=None
#                                     #     ),
#                                     #
#                                     #     dbc.Popover
#                                     #     (
#                                     #         popover_data_table,
#                                     #         id="pop-data",
#                                     #         target="data-table-info",
#                                     #         trigger="hover",
#                                     #     ),
#                                     # ],
#                                     # className="div-row-5-info"),
#                                     #
#                                     # dash_table.DataTable
#                                     # (
#                                     #     id='data-table'
#                                     #     ,page_action="native"
#                                     #     ,page_current= 0
#                                     #     ,page_size= 10
#                                     #     ,filter_action='native'
#                                     #     ,columns=[]
#                                     #     ,data=[]
#                                     #     ,merge_duplicate_headers=True
#                                     #     ,style_data={'overflow': 'hidden'}
#                                     #     ,style_header={'textAlign': 'center'}
#                                     #     ,style_cell=
#                                     #     {
#                                     #         'textAlign': 'right'
#                                     #         ,'padding':'5px'
#                                     #     }
#                                     #     ,style_cell_conditional=
#                                     #     [
#                                     #         {
#                                     #             'if': {'column_id': 'location'}
#                                     #             ,'textAlign': 'left'
#                                     #             ,'textOverflow': 'ellipsis'
#                                     #             ,'maxWidth': 200
#                                     #         },
#                                     #         {
#                                     #             'if': {'column_id': 'fips'}
#                                     #             ,'textAlign': 'left'
#                                     #         }
#                                     #     ]
#                                     # ),
#                                 ]),
#                             ]),
#                         ]
#                     ),
#                 )
#             ),
#         ])

# row_x = html.Div([
#             dbc.Row
#             (
#                 dbc.Col
#                 (
#                     html.Div
#                     (
#                         id="div-row-x",
#                         className="div-row-x",
#                         children=
#                         [
#                             info_row("x","lg"),
#                             content_row_x
#                         ]
#                     )
#                 )
#             )
#         ])
