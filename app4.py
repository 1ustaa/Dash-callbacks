from dash import Dash, dcc, html, Input, Output, callback

external_stylesheet = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = Dash(__name__, external_stylesheets=external_stylesheet)

app.layout = html.Div([
    dcc.Input(
        id="num_multi",
        type="number",
        value=5,
    ),
    html.Table([
        html.Tr([html.Td(["x", html.Sub(2)]), html.Td(id="square")]),
        html.Tr([html.Td(["x", html.Sub(3)]), html.Td(id="cube")]),
        html.Tr([html.Tr([2, html.Sub("x")]), html.Td(id="twos")]),
        html.Tr([html.Tr([3, html.Sub("x")]), html.Td(id="threes")]),
        html.Tr([html.Tr(["x", html.Sup("x")]), html.Td(id="x**x")])
    ])
])


@app.callback(
    Output("square", "children"),
    Output("cube", "children"),
    Output("twos", "children"),
    Output("threes", "children"),
    Output("x**x", "children"),
    Input("num_multi", "value")
)
def digit_counter(number):
    if number is not None:
        return number ** 2, number ** 3, 2 ** number, 3 ** number, number ** number
    else:
        return "", "", "", "", ""


if __name__ == "__main__":
    app.run(debug=True)
