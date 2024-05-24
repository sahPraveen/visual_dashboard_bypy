

print("py Dash")

# app.py

import pandas as pd
from dash import Dash, dcc, html

#"C:\Users\Praveen_Sah\vs_code_files\avocado.csv"

data = (
    pd.read_csv("C:\\Users\\Praveen_Sah\\vs_code_files\\avocado.csv")
    .query("type == 'conventional' and region == 'Albany'")
    .assign(Date=lambda data: pd.to_datetime(data["Date"], format="%Y-%m-%d"))
    .sort_values(by="Date")
)

app = Dash(__name__)

# app.py

app.layout = html.Div(
    children=[
        html.H1(
            children="Avocado Analytics | Data Project",
            style={"fontSize": "48px", "color": "red"},
        ),
        html.P(
            children=(
                "Analyze the behavior of Avocado prices and the number"
                " of avocados sold in the US between 2015 and 2018"
            ),
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["AveragePrice"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Average Price of Avocados"},
            },
        ),
        dcc.Graph(
            figure={
                "data": [
                    {
                        "x": data["Date"],
                        "y": data["Total Volume"],
                        "type": "lines",
                    },
                ],
                "layout": {"title": "Avocados Sold"},
            },
        ),
    ]
)

# app.py


if __name__ == "__main__":
    app.run_server(debug=True)
