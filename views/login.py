import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import _, app, server, LoginManager, UserMixin, login_user, login_required, logout_user, current_user, load_user, User
from werkzeug.security import check_password_hash

layout =html.Div(
    children=[
        html.Div(
            className="container",
            children = [
                dcc.Location(id='url_login', refresh=True),
                html.Div(_('''Please log in to continue:'''), id='h1'),
                html.Div(
                    # method='Post',
                    children=[
                        dcc.Input(
                            placeholder=_('Enter your username'),
                            type='text',
                            id='uname-box'
                        ),
                        dcc.Input(
                            placeholder=_('Enter your password'),
                            type='password',
                            id='pwd-box'
                        ),
                        html.Button(
                            children='Login',
                            n_clicks=0,
                            type='submit',
                            id='login-button'
                        ),
                        html.Div(children='',id='output-state')
                    ]
                ),
            ]
        )
    ]
)

@app.callback(Output('url_login', 'pathname'),
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def open_dashboard(n_clicks, input1, input2):
    user = User.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/alicedash'
        else:pass
    else:pass

@app.callback(Output('output-state', 'children'),
              [Input('login-button', 'n_clicks')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def update_output(n_clicks, input1, input2):
    if n_clicks > 0:
        user = User.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return _('Incorrect username or password')
        else:
            return _('Incorrect username or password')
    else:
        return ''
