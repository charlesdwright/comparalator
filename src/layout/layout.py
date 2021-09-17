import dash_html_components as html
import dash_core_components as dcc
import dash_bootstrap_components as dbc
from funcs.funcs import *
from data.data import df
from layout.rows import *
from content.content import *

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
                            content_row_1,
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
