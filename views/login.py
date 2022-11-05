import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app, User
from flask_login import login_user
from werkzeug.security import check_password_hash

layout = html.Div(
    children=[
        html.Div(
            className="container",
            children=[
                dcc.Location(id='url_login', refresh=True),
                html.Div('''Please log in to continue:''', id='h1'),
                html.Div(
                    # method='Post',
                    children=[
                        dcc.Input(
                            placeholder='Enter your username',
                            n_submit=0,
                            type='text',
                            id='uname-box'
                        ),
                        dcc.Input(
                            placeholder='Enter your password',
                            n_submit=0,
                            type='password',
                            id='pwd-box'
                        ),
                        html.Button(
                            children='Login',
                            n_clicks=0,
                            type='submit',
                            id='login-button'
                        ),
                        html.Div(children='', id='output-state')
                    ]
                ),
            ]
        )
    ]
)


@app.callback(Output('url_login', 'pathname'),
              [Input('login-button', 'n_clicks'),
              Input('uname-box', 'n_submit'),
               Input('pwd-box', 'n_submit')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def success(n_clicks, n_submit_uname, n_submit_pwd, input1, input2):
    user = User.query.filter_by(username=input1).first()
    if user:
        if check_password_hash(user.password, input2):
            login_user(user)
            return '/success'
        else:
            pass
    else:
        pass


@app.callback(Output('output-state', 'children'),
              [Input('login-button', 'n_clicks'),
               Input('uname-box', 'n_submit'),
               Input('pwd-box', 'n_submit')],
              [State('uname-box', 'value'),
               State('pwd-box', 'value')])
def update_output(n_clicks, n_submit_uname, n_submit_pwd, input1, input2):
    if n_clicks > 0 or n_submit_uname > 0 or n_submit_pwd > 0:
        user = User.query.filter_by(username=input1).first()
        if user:
            if check_password_hash(user.password, input2):
                return ''
            else:
                return 'Incorrect username or password'
        else:
            return 'Incorrect username or password'
    else:
        return ''
