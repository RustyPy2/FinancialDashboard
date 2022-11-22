# Import Libraries

import dash as Dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output
import pandas as pd
import plotly.express as px
import plotly.graph_objs as go
import yfinance as yf
import datetime as dt

from pandas import DataFrame

# Initialize Dash App
app = Dash.Dash()

app.layout = html.Div(children = [html.H1("Financial Dashboard"),
html.H2("Money in Memes"),html.Div(style={'color': 'black'},children= [
dcc.Dropdown(id='Ticker-Dropdown',options=["SPY","AAPL","TSLA"],value='SPY')]),
dcc.Graph(id= 'Ticker-Graph', figure={'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
plot_bgcolor='rgba(0,0,0,0)')})])

@app.callback(
    Output(component_id= 'Ticker-Graph', component_property= 'figure'),
    Input(component_id= 'Ticker-Dropdown', component_property= 'value')
)

def update_ticker_graph(ticker):
    data_frame = pd.DataFrame(yf.download(tickers=ticker, period='1y', interval='1d'))
    
    adj_close = data_frame['Adj Close']
    
    figure = px.line(adj_close)
    return figure

# Run local server
if __name__ == "__main__":
    app.run_server(debug= True)
