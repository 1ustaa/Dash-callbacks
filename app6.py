from dash import Dash, dcc, html, Input, Output, callback, State

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    dcc.Input(id="first_input",
              value="Введите"),
    dcc.Input(id="second_input",
              value="что-нибудь"),
    html.Button(id="submit_button",
                n_clicks=0,
                children="Подтвердить"),
    html.Div(id="output_message")
])


@callback(
    Output("output_message", "children"),
    State("first_input", "value"),
    State("second_input", "value"),
    Input("submit_button", "n_clicks")
)
def generate_message(word1, word2, n_clicks):
    return f"Кнопка была нажата {n_clicks} раз | Первое слово {word1}| Второе слово {word2}"


if __name__ == "__main__":
    app.run(debug=True)
