from dash import Dash, html, dcc, Input, Output, callback

app = Dash(__name__)

app.layout = html.Div([
    html.H6(children="Введите любой текст"),
    html.Div(["Ввод",
              dcc.Input(id="input_field",
                        value="Введите текст",
                        type="text")]),
    html.Br(),
    html.Div(id="text_area")
])


@callback(
    Output("text_area", "children"),
    Input("input_field", "value")

)
def update_output(input_value):
    return f"Вывод {input_value}"


if __name__ == "__main__":
    app.run(debug=True)
