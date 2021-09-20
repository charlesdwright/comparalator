import dash_bootstrap_components as dbc
import dash_html_components as html

import base64


from funcs.funcs import generalInfo

image_filename = './content/absentee-ratios.png'
encoded_image = base64.b64encode(open(image_filename, 'rb').read())
theImgSrc='data:image/png;base64,{}'.format(encoded_image.decode())

top_text=[
    dbc.ListGroupItemText([
    html.P("I was very curious about the impact of mail-in ballots on the election, so I got ahold of the NYT dataset (it seemed to be be the reference standard and was publicly available).  It was too big for convenient spreadsheet work so I opened it up in a Jupyter Notebook and looked it over."),
    html.P("I tend to look at ratios, so I computed the absentee vote ratios and filtered the dataset by the largest of those to see what I could see, and I thought I could see some interested trends, as I describe below:")
    ])
]

card_text=[
                # dbc.CardHeader(
                #     html.H5("Summary:  high-absentee districts disproportionately benefited Biden by nearly a 7:1 margin.", className="card-text"),
                # ),
                # html.Br(),
                html.P("Speaking strictly of absentee ballots, looks like there was some curious behavior on both sides, though quite disproportionately."),
                html.P("To gain some insight into this, we’ve done a superficial analysis as follows: Filtered by precincts where the ratio of absentee votes favored Biden by 7:1 or more over Trump."),
                html.P("In these locations:"),
                html.Li("Biden netted a total of 679,214 absentee votes."),
                html.Li("The Biden-Trump ratio was as high as 16.5:1 (netting Biden 440,219 votes)"),
                html.Br(),
                html.P("The opposite case was run. In locales where Absentee Votes tallied at 7:1 or greater for Trump:", className="card-text"),

                html.Li("Trump netted 103,688 absentee votes."),
                html.Li("The Trump-Biden ratio was as high as 35:1 (netting Trump 341 votes)")
            ]

botton_text=[
    html.P("After tweaking with thresholds, I decided it would be handy to build a tool to make such comparisons easier to do.  Then, of course, it made sense to put it out there in case others wanted to look at the data, and the 'Compar-A-Lator' was born.")
]


abs_ratio_card = dbc.Card(
    [

        dbc.CardBody(
            html.P(card_text, className="card-text")
        ),

        dbc.CardImg(src=theImgSrc, top=True),

        dbc.CardBody(
            html.Sub("(NYT Data)", className="card-text")
        )

    ],
    style={"width": "36rem"},
    className="abs_ratio_card"
)


cards = dbc.Row(
    [
        dbc.Col(abs_ratio_card, width='auto')

    ], className='abs_card_row'
)

modal_1 = html.Div([
    top_text,
    abs_ratio_card,
    botton_text
])


#======= popovers ========

def blah():

    x= html.Div([
        html.P("Speaking strictly of absentee ballots, looks like there was some curious behavior on both sides, though quite disproportionately."),
        html.P("To gain some insight into this, we’ve done a superficial analysis as follows: Filtered by precincts where the ratio of absentee votes favored Biden by 7:1 or more over Trump."),
        html.P("In these locations:"),
        html.Li("Biden netted a total of 679,214 absentee votes."),
        html.Li("The Biden-Trump ratio was as high as 16.5:1 (netting Biden 440,219 votes)"),
        html.Br(),
        ])
    return x



def popover(row):
    p= dbc.Popover(
        popover_content(row),
        id="pop-" + row,
        target="info-" + row ,
        trigger="hover",
        className="pop-info"
    )

    return p

#put this on a card or ?
def popover_content(row):
    i=row.split("-")[1]
    theBody='pop_body_row_' + i

    # popBody=[]
    # for key in generalInfo['body'][row]:
    #     popBody.append(dbc.ListGroupItemText(generalInfo['body'][row][key]))

    print(row + "  " + str(theBody))
    return [
        dbc.PopoverHeader(generalInfo['headers'][row]),
#        dbc.PopoverBody(popBody)
        eval(theBody)
        #popover_body_row_1
        # dbc.PopoverBody([
        #     dbc.ListGroupItemText(html.Li(generalInfo['body'][row]["p1"])),
        #     dbc.ListGroupItemText(html.Li(generalInfo['body'][row]["p2"])),
        #     dbc.ListGroupItemText(html.Li(generalInfo['body'][row]["p3"])),
        #     dbc.ListGroupItemText(html.Li(generalInfo['body'][row]["p4"])),
        #     # dbc.ListGroupItemText(theToolTip(row)),
        #     # theModal(row)
        # ]),
    ]


pop_body_row_1 = dbc.PopoverBody([
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-1"]["p1"])),
    # dbc.ListGroupItemText(generalInfo['body']["row-1"]["p2"])),
    dbc.ListGroupItemText(
        html.Li([
            "For a little more detail, with an example, click that little blue",
        html.I
        (
            className="fa fa-question-circle fa-sm",
            id="pop-row_1",
            **{'aria-hidden': 'true'},
            children=None
        ),
        "."
        ]),
        )

    #dbc.ListGroupItemText(html.Li(generalInfo['body']["row-1"]["p3"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-1"]["p4"]))
])
pop_body_row_2 = dbc.PopoverBody([
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-2"]["p1"])),
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-2"]["p2"])),
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-2"]["p3"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-2"]["p4"]))
])
pop_body_row_3 = dbc.PopoverBody([
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-3"]["p1"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-3"]["p2"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-3"]["p3"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-3"]["p4"]))
])
pop_body_row_4 = dbc.PopoverBody([
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-4"]["p1"])),
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-4"]["p2"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-4"]["p3"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-4"]["p4"]))
])
pop_body_row_5 = dbc.PopoverBody([
    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-5"]["p1"])),
    dbc.ListGroupItemText(
        html.Li([
            "Be aware of the 'case sensitivity' toggle.' This uses Dash's filtering syntax which is intuitive enough but if you need details see",
            html.A(' here.',href='https://dash.plotly.com/datatable/filtering')
        ]),
        )
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-5"]["p2"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-5"]["p3"])),
#    dbc.ListGroupItemText(html.Li(generalInfo['body']["row-5"]["p4"]))
])
