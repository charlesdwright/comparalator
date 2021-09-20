import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc

import dash_table
from dash_table.Format import Format, Group, Scheme

from content.content import *
from funcs.funcs import *
from data.data import df
df=df()

from dash.dependencies import Input, Output, State


modalHeader=generalInfo['headers']['modal-1'] #html.Div("How this project came to be.")
modalBody = html.Div([

            #top_text,
            dbc.ListGroupItemText(generalInfo['body']['modal-1']["p1"]),
            dbc.ListGroupItemText(generalInfo['body']['modal-1']["p2"]),
            cards,
            html.Br(),
            dbc.ListGroupItemText(generalInfo['body']['modal-1']["p3"]),
            dbc.ListGroupItemText(generalInfo['body']['modal-1']["p4"])

])


#-------------------- modal ------------------------
def theModal(row, size):
    modal = html.Div(
        [
            #dbc.Button("Open", id="open-centered-"+row),
            dbc.Modal(
                [
                    dbc.ModalHeader(modalHeader),
                    dbc.ModalBody([modalBody],className="modalBody"),
                    dbc.ModalFooter(
                        dbc.Button(
                            "Close",
                            id="close-centered-" + row,
                            className="ml-auto",
                            n_clicks=0,
                        )
                    )
                ],
                id="modal-centered-"+row,
                centered=True,
                is_open=False,
                size= size,
            )
        ],className="theModal"
    )
    return modal


#-------------------- end modal ------------------------
#-------------------- card ------------------------
# card = dbc.Card(
#     [
#         dbc.CardHeader("This is the header"),
#         dbc.CardBody(
#             [
#                 html.H4("Card title", className="card-title"),
#                 html.P("This is some card text", className="card-text"),
#             ]
#         ),
#         dbc.CardFooter("This is the footer"),
#     ],
#     style={"width": "18rem"},
# )
#-------------------- end card ------------------------
#-------------------- tooltip ------------------------
# def theToolTip(row):
#     tooltip = html.Div(
#         [
#             html.P(
#                 [
#                     "I wonder what ",
#                     html.Span(
#                         "floccinaucinihilipilification",
#                         id="tooltip-target-"+row,
#                         style={"textDecoration": "underline", "cursor": "pointer"},
#                     ),
#                     " means?",
#                 ]
#             ),
#             dbc.Tooltip(
#                 "Noun: rare, "
#                 "the action or habit of estimating something as worthless.",
#                 target="tooltip-target-"+row,
#             ),
#         ]
#     )
#     return tooltip

#-------------------- end tooltip ------------------------

def popover_content(row):
    return [
        dbc.PopoverHeader(generalInfo['headers'][row]),
        dbc.PopoverBody([
            dbc.ListGroupItemText(generalInfo['body'][row]["p1"]),
            dbc.ListGroupItemText(generalInfo['body'][row]["p2"]),
            dbc.ListGroupItemText(generalInfo['body'][row]["p3"]),
            dbc.ListGroupItemText(generalInfo['body'][row]["p4"]),
            # dbc.ListGroupItemText(theToolTip(row)),
            # theModal(row)
        ]),
    ]

def info_row(row, size):
    detailRow =None
    if (row=="row-1"):
        detailRow=detail_row(row,"lg")

    theRow = dbc.Row(
        [
        dbc.Col
        ([
            html.Div
            ([
                html.I
                (
                    className="fa fa-info-circle fa-" + size,#classname,
                    id="info-" + row,#idd,
                    **{'aria-hidden': 'true'},
                    children=None
                ),

                popover(row),
                detailRow

            ])
        ],className="col-info")
        ],
        className="div-row-info")

    return theRow


def detail_row(row, size):
    theRow = dbc.Row(
        [
        dbc.Col
        ([
            html.Div
            ([
                dbc.NavLink(
                    html.I
                    (
                        className="fa fa-question-circle fa-" + size,#classname,
                        id="detail-" + row,#idd,
                        **{'aria-hidden': 'true'},
                        children=None
                    ),
                    id="open-centered-"+row,
                    n_clicks=0
                ),

                theModal(row, size)

            ])
        ],className="col-detail")
        ],
        className="div-row-detail")

    return theRow

def dropdown(id,value):
    theDropdown = dcc.Dropdown(
                    id='operand_' + id,
                    className='dropdown',
                    options=[
                        {"label": key, "value": key} for key in dataHeaders
                    ],
                    value=value
                )
    return html.Div([theDropdown], className='dropdown')

calc_buttons = html.Div(
    [
    dbc.RadioItems(
        id="operator",
        className="btn-group",
        labelClassName="btn btn-secondary",
        labelCheckedClassName="active",
        options=[
            {"label": "/", "value": "/"},
            {"label": "-", "value": "-"},
            {"label": "+", "value": "+"},
        ],
        value='/',
    ),
    #html.Div(id="output"),
    ],
    className="radio-group",
)

content_row_1 = dbc.Row ([
    dbc.Col
    ([
        html.Div
        (
            [
                html.Label("2020 US Election Vote Compar-A-Lator",className='div-label',id='div-title-label'),

            ]
        )

    ],
    className="col-content")

],
className="div-row-x-content")

content_row_2 = dbc.Row ([
                    dbc.Col([
                        html.Div([
                            dbc.Row([
                                dbc.Col(
                                    dropdown('0', 'Biden')
                                    ,className="r2-col-content"
                                    ),
                                dbc.Col(
                                    calc_buttons
                                    ,className="r2-col-content"
                                    ),
                                dbc.Col(
                                    dropdown('1', 'Trump')
                                    ,className="r2-col-content"
                                    )
                            ],id="div-row-2-2")
                        ])
                    ],
                    className="col-content")
                ],

className="div-row-x-content")

content_row_3 = dbc.Row ([
    dbc.Col
    ([
        html.Div
        (
        dbc.Row(
            [
            dbc.Col(
                [
                dcc.Loading(
                    id="loading-1",
                    type="default",
                    children=[
                        html.Div(className ='div-graph', children=[
                            dcc.Graph(id="graph"),
                        ]),
                    ],
                ),
                ], width=11),

                dbc.Col(
                    [
                    html.Div(
                       className="div-range-slider",
                       children=
                            [
                                dcc.RangeSlider(
                                className="range-slider",
                                id='range-slider',
                                vertical=True,
                                min=0,
                                max=1,
                                step=0.01,# None,# 10,
                                value=[0, 1],
                                verticalHeight=282,
                                tooltip = { 'always_visible': False },
                                allowCross=False,
                                persistence=True,
                                persistence_type='local'
                                ),
                            ],
                        ),
                    ], className="div-col-range-slider", width=1),
                ]
            ),
        )

    ],
    className="col-content",
    id="content-row-3")

],
className="div-row-x-content")

content_row_4 = dbc.Row ([
    dbc.Col
    ([
            html.Div(
                className="div-time-sliders",
                children=
                    [
                    html.Div(
                        [
                            html.Label("Day",className='div-label'),
                        ],
                    className="slider-label",
                    ),
                    dcc.Slider(
                        className='day-slider',
                        id='day-slider',
                        min=df['day'].min(),
                        max=df['day'].max(),
                        value=df['day'].min(),
                        marks={str(day):str(day)+"/Nov" for day in df['day'].unique()},
                        ),
                    html.Div(
                        [
                            html.Label("Hour",className='div-label'),
                        ],
                    className="slider-label",
                    ),
                    dcc.Slider(
                        id='hour-slider',
                        min=df['hour'].min(),
                        max=df['hour'].max(),
                        value=df['hour'].max(),
                        marks={str(hour):str(hour) for hour in df['hour'].unique()},
                        ),
                    ],
                ),

    ],
    className="col-content")

],
className="div-row-x-content")

content_row_5 = dbc.Row ([
                    dbc.Col
                    ([
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    html.Div
                                    (
                                        [
                                            html.Label("Data",className='div-label',id='div-data-label'),
                                        ],

                                    className="slider-label"),

                                    dash_table.DataTable
                                    (
                                        id='data-table'
                                        ,page_action="native"
                                        ,page_current= 0
                                        ,page_size= 10
                                        ,filter_action='native'
                                        ,columns=[]
                                        ,data=[]
                                        ,merge_duplicate_headers=True
                                        ,style_data={'overflow': 'hidden'}
                                        ,style_header={'textAlign': 'center'}
                                        ,style_cell=
                                        {
                                            'textAlign': 'right'
                                            ,'padding':'5px'
                                        }
                                        ,style_cell_conditional=
                                        [
                                            {
                                                'if': {'column_id': 'location'}
                                                ,'textAlign': 'left'
                                                ,'textOverflow': 'ellipsis'
                                                ,'maxWidth': 200
                                            },
                                            {
                                                'if': {'column_id': 'fips'}
                                                ,'textAlign': 'left'
                                            }
                                        ]
                                    ),
                                ])
                            ])
                        ])


                    ],
                    className="col-content")
],
className="div-row-x-content")

content_row_x = dbc.Row ([
    dbc.Col
    ([
        html.Div
        (
            [
                html.Label("Content!",className='div-label',id='div-content-label'),
            ]
        )

    ],
    className="col-content")

],
className="div-row-x-content")
