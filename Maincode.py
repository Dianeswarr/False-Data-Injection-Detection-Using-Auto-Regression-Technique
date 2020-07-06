import dash
from dash.dependencies import Output, Input
import dash_core_components as dcc
import dash_html_components as html
import plotly
import random
import plotly.graph_objs as go
from collections import deque
import sqlite3
import pandas as pd


app = dash.Dash(__name__)
app.layout = html.Div(
    [
        
        dcc.Graph(id='live-graph1',animate=True),
        dcc.Graph(id='live-graph2',animate=True),
        dcc.Graph(id='live-graph3',animate=True),
        dcc.Interval(
            id='graph-update',
            interval=1*5000
        ),
    ]
)



@app.callback(Output('live-graph1', 'figure'),
              [Input('graph-update', 'n_intervals')])


def update_graph_scatter1(input_data):
    conn = sqlite3.connect("falsedata112.db")
    dataSQL = []
    X = deque(maxlen=20)
    Y = deque(maxlen=20)
    cursor = conn.cursor()
    cursor.execute("SELECT Time, Temperature48, Temperature31, Temperature54, Temperature32, Temperature71, Temperature65, Temperature78, Temperature37, Temperature76 FROM data")
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['Time','Temperature48', 'Temperature31', 'Temperature54','Temperature32','Temperature71','Temperature65','Temperature78','Temperature37','Temperature76']
        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        X = df['Time']
        Y = df['Temperature48']
        Z = df['Temperature31']
        A = df['Temperature54']
        B = df['Temperature32']
        C = df['Temperature71']
        D = df['Temperature65']
        E = df['Temperature78']
        F = df['Temperature37']
        G = df['Temperature76']
        

       
    data=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Temperature48',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data1=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Z),
            name='Temperature31',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data2=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(A),
            name='Temperature54',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data3=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(B),
            name='Temperature32',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data4=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(C),
            name='Temperature71',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data5=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(D),
            name='Temperature65',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data6=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(E),
            name='Temperature78',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data7=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(F),
            name='Temperature37',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data8=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(G),
            name='Temperature76',
            connectgaps=True,
            mode= 'lines+markers'
            )
    
    
    return {'data': [data,data1,data2,data3,data4,data5,data6,data7,data8],'layout': go.Layout(title="Live Temperature Data",xaxis= dict(
        title= 'Time',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),yaxis=dict(
        title='Temperature',
        titlefont_size=16,
        tickfont_size=14,
    ))} 

@app.callback(Output('live-graph2', 'figure'),
              [Input('graph-update', 'n_intervals')])


def update_graph_scatter2(input_data):
    conn = sqlite3.connect("DB48.db")
    dataSQL = []
    X = deque(maxlen=20)
    Y = deque(maxlen=20)
    cursor = conn.cursor()
    cursor.execute("SELECT id, real, predicted FROM data")
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['id','real', 'predicted']
        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        X = df['id']
        Y = df['real']
        Z = df['predicted']
        
    data=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Real value of Node:48',
            connectgaps=True,
            mode= 'lines+markers'
            )
    data1=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Z),
            name='Predicted value of Node:48',
            connectgaps=True,
            mode= 'lines+markers'
            )
    return {'data': [data,data1],'layout': go.Layout(title="Real vs Predicted",xaxis= dict(
        title= 'Window margin',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),yaxis=dict(
        title='Temperature',
        titlefont_size=16,
        tickfont_size=14,
    ))} 

@app.callback(Output('live-graph3', 'figure'),
              [Input('graph-update', 'n_intervals')])

def update_graph_scatter3(input_data):
    conn = sqlite3.connect("falsedata112.db")
    dataSQL = []
    X = deque(maxlen=20)
    Y = deque(maxlen=20)
    cursor = conn.cursor()
    cursor.execute("SELECT Time, Temperature48, Temperature31, Temperature54, Temperature32, Temperature71, Temperature65, Temperature78, Temperature37, Temperature76 FROM data")
    rows = cursor.fetchall()
    for row in rows:
        dataSQL.append(list(row))
        labels = ['Time','Temperature48', 'Temperature31', 'Temperature54','Temperature32','Temperature71','Temperature65','Temperature78','Temperature37','Temperature76']
        df = pd.DataFrame.from_records(dataSQL, columns=labels)
        X = df['Time']
        Y = df['Temperature48']
        Z = df['Temperature31']
        A = df['Temperature54']
        B = df['Temperature32']
        C = df['Temperature71']
        D = df['Temperature65']
        E = df['Temperature78']
        F = df['Temperature37']
        G = df['Temperature76']
        

       
    data=plotly.graph_objs.Scatter(
            x=list(X),
            y=list(Y),
            name='Temperature48',
            connectgaps=True,
            mode= 'lines+markers'
            )
    
    return {'data': [data],'layout': go.Layout(title="Live data from mote id 48",xaxis= dict(
        title= 'Time',
        ticklen= 5,
        zeroline= False,
        gridwidth= 2,
    ),yaxis=dict(
        title='Temperature',
        titlefont_size=16,
        tickfont_size=14,
    ))} 

if __name__ == '__main__':
    app.run_server(debug=True)
