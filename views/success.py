import warnings
warnings.filterwarnings("ignore")

#Dash configuration
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from server import app, server, LoginManager, UserMixin, login_user, login_required, logout_user, current_user, load_user, User

# Create success layout
