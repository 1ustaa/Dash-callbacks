from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px

import pandas as pd

app = Dash(__name__)

df = pd.read_csv("C:\\Users\\Сергей\\Downloads\\country_indicators.csv")

app.layout = html.Div([
    html.Div([
        dcc.Dropdown(
            df['Indicator Name'].unique(),
            'Fertility rate, total (births per woman)',
            id="xaxis-column"
        ),
        dcc.RadioItems(
            options=['Linear', 'Log'],
            value=['Linear'],
            id="xaxis-type",
            inline=True
        )
    ],
        style={"width": "48%",
               "display": "inline-block"}),

    html.Div([
        dcc.Dropdown(
            df["Indicator Name"].unique(),
            "Life expectancy at birth, total (years)",
            id="yaxis_column"
        ),
        dcc.RadioItems(
            ['Linear', 'Log'],
            ['Linear'],
            id="yaxis_type",
            inline=True
        )
    ], style={"width": "48%",
              "float": "right",
              "display": "inline_block"}),

    dcc.Graph(id="indicator_graphic"),

    dcc.Slider(
        df["Year"].min(),
        df["Year"].max(),
        step=None,
        id="year_slider",
        value=df["Year"].max(),
        marks={str(year): str(year) for year in df["Year"].unique()}
    )
])


@callback(
    Output("indicator_graphic", "figure"),
    Input("xaxis-column", "value"),
    Input("xaxis-type", "value"),
    Input("yaxis_column", "value"),
    Input("yaxis_type", "value"),
    Input("year_slider", "value"),
)
def update_graph(xaxis_column_name, yaxis_column_name,
                 xaxis_type, yaxis_type,
                 year_value):
    dff = df[df["Year"] == year_value]

    fig = px.scatter(x=dff[dff['Indicator Name'] == xaxis_column_name]['Value'],
                     y=dff[dff['Indicator Name'] == yaxis_column_name]['Value'],
                     hover_name=dff[dff['Indicator Name'] == yaxis_column_name]['Country Name'])

    fig.update_layout(margin={'l': 40, 'b': 40, 't': 10, 'r': 0}, hovermode='closest')

    fig.update_xaxes(title=xaxis_column_name,
                     type='linear' if xaxis_type == 'Linear' else 'log')

    fig.update_yaxes(title=yaxis_column_name,
                     type='linear' if yaxis_type == 'Linear' else 'log')

    return fig


if __name__ == '__main__':
    app.run(debug=True)
