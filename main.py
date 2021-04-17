import dash
import dash_core_components as dcc
import dash_html_components as html

from dash.dependencies import Input, Output

import plotly.graph_objs as go
import pandas as pd

# Data
df = pd.read_csv('d:/data/data set for python/gapminderDataFiveYear.csv')

app = dash.Dash()

year_options = []
for y in df['year'].unique():
    year_options.append({'label': str(y), 'value': y})

app.layout = html.Div([
    dcc.Graph(id='graph'),
    dcc.Dropdown(id='dd-1', options=year_options, value=df['year'].min())
])

@app.callback(Output('graph', 'figure'),
              [Input('dd-1', 'value')])
def update_figuret(selected_year):
    filtered_df = df[df['year'] == selected_year]
    traces = []
    for cn in filtered_df['continent'].unique():
        df_by_continennt = filtered_df[filtered_df['continent'] == cn]
        traces.append(go.Scatter(
            x=df_by_continennt['gdpPercap'],
            y=df_by_continennt['lifeExp'],
            mode='markers',
            opacity=0.7,
            marker={'size': 15},
            name=cn
        ))
    return {'data': traces,
            'layout': go.Layout(title='PLOT',
                                xaxis={'title': 'GDP Per Cap', 'type': 'log'},
                                yaxis={'title': 'Life Expectancy'})}

if __name__ == '__main__':
    app.run_server()
