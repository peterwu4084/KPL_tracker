import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

bold=lambda s: '<b>'+s+'</b>'

teams = pd.read_csv('Data/team.csv', index_col=0)
teams.set_index('战队', inplace=True)

theta = list(teams.columns)
theta.append(theta[0])
visibles = [[False if j!=i else True for j in range(16)] for i in range(16)]
colors = px.colors.qualitative.Dark24
tnames = teams.index

fig = go.Figure()
for i in range(16):
    r = list(teams.iloc[i])
    r.append(r[0])
    fig.add_trace(go.Scatterpolar(
        r=r, theta=theta,
        mode='markers+lines',
        fill='toself',
        visible='legendonly' if i else True,
        line_color=colors[i],
        name=bold(tnames[i])
    ))
    
fig.update_layout(polar=dict(radialaxis_range=[0, 10.5]),
                  font=dict(family='Courier New', size=20),
                  width=800, height=800,
                  showlegend=True)
fig.update_layout(legend=dict(x=1.2, y=0.5, yanchor='middle', title=bold('Click team')),
                  title=dict(text='<b>TeamPower</b>', x=0.5, xanchor='center',
                            y=0.9, font_size=40))
fig.write_html('Figure/team.html')

players = pd.read_csv('Data/player.csv', index_col=0)
players.set_index('ID', inplace=True)

theta = list(players.columns)
visibles = [[False if j!=i else True for j in range(16)] for i in range(10)]
colors = px.colors.qualitative.G10
pnames = players.index

fig = go.Figure()
for i in range(10):
    r = list(players.iloc[i])
    fig.add_trace(go.Barpolar(
        r=r, theta=theta,
        r0=0,
        width=[0.5] * 5,
        marker=dict(color=colors[i], 
                    line=dict(color='black',
                              width=2)),
        visible='legendonly' if i else True,
        name=bold(pnames[i]),
        opacity=0.7,
        base='base'
    ))
    
fig.update_layout(polar=dict(radialaxis_range=[0, 10.5]),
                  font=dict(family='Courier New', size=20),
                  width=800, height=800,
                  showlegend=True)
fig.update_layout(legend=dict(x=1.2, y=0.5, yanchor='middle', title=bold('Click player')),
                  title=dict(text='<b>PlayerPower</b>', x=0.5, xanchor='center',
                            y=0.9, font_size=40))
fig.write_html('Figure/player.html')
