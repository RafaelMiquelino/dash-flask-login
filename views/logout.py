#Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import _, app, server, LoginManager, UserMixin, login_user, login_required, logout_user, current_user, load_user, User

# Create app layout
layout = html.Div(children=[
    dcc.Location(id='url_logout', refresh=True),
    html.Div(
        className="container",
        children=[
            html.Div(
                html.Div(
                    className="row",
                    children=[
                        html.Div(
                            className="ten columns",
                            children=[
                                html.Br(),
                                html.Div(_('User disconnected - Please login to view the dashboard again')),
                            ]
                        ),
                        html.Div(
                            className="two columns",
                            # children=html.A(html.Button('LogOut'), href='/')
                            children=[
                                html.Br(),
                                html.Button(id='back-button', children=_('Go back'), n_clicks=0)
                            ]
                        )
                    ]
                )
            )
        ]
    )
])

# Create callbacks

@app.callback(Output('url_logout', 'pathname'),
              [Input('back-button', 'n_clicks')])
def logout_dashboard(n_clicks):
    if n_clicks > 0:
        return '/'
