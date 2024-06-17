from dash import dcc, html, Dash, Input, Output, callback

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheet)

all_options = {"Playstation": ["God of war", "Kill-zone", "Uncharted"],
               "Xbox": ["Halo", "Gears of war", "Forza"]}

app.layout = html.Div([
    dcc.RadioItems(
        options=list(all_options.keys()),
        value="Playstation",
        id="console_radio"
    ),
    html.Hr(),
    dcc.RadioItems(id="games_radio"),
    html.Hr(),
    html.Div(id="display-selected-values")
])


@callback(
    Output("games_radio", "options"),
    Input("console_radio", "value")
)
def set_console_options(selected_console):
    return [{"label": i, "value": i} for i in all_options[selected_console]]


@callback(
    Output('games_radio', 'value'),
    Input('console_radio', 'value'))
def set_cities_value(available_options):
    return all_options[available_options][0]

@callback(
    Output("display-selected-values", "children"),
    Input("console_radio", "value"),
    Input("games_radio", "value")
)
def set_display_children(console, game):
    return f"{console} - {game}"


if __name__ == '__main__':
    app.run(debug=True)
