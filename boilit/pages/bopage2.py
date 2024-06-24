import os
import dash
import pandas as pd
from dash import Dash, Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate
from dash_ag_grid.AgGrid import AgGrid
from plotly import graph_objects as go
import plotly.express as px
from collections import namedtuple
from typing import Final

from agility.skeleton.custom_components import ButtonCustom, InputCustom, MessageCustom

from boilit.config.main import STORE_ID, PROJECT_NAME
from boilit.project import page_one


class PageIDs:
    def __init__(self) -> None:
        # Get the base name of the file where this instance is created
        filename = os.path.basename(__file__)
        # Remove the file extension to use only the file name as the prefix
        prefix: Final[str] = filename.replace(".py", "")
        self.prefix: Final[str] = prefix
        self.status: Final[str] = f"{prefix}_status"
        self.input: Final[str] = f"{prefix}_input"
        self.add_btn: Final[str] = f"{prefix}_add_btn"
        self.delete_btn: Final[str] = f"{prefix}_delete_btn"
        self.save_btn: Final[str] = f"{prefix}_save_btn"
        self.feedback_save: Final[str] = f"{prefix}_feedback_save"
        self.run_btn: Final[str] = f"{prefix}_run_btn"
        self.feedback_run: Final[str] = f"{prefix}_feedback_run"
        self.output: Final[str] = f"{prefix}_output"


ids = PageIDs()

dash.register_page(__name__)
app: Dash = dash.get_app()

PAGE_TITLE = "Page Two"

# create a sample dash page layout with heading and subheading
layout = html.Div(
    [
        html.H1(
            PROJECT_NAME,
            className="text-2xl font-bold",
        ),
        html.H2(
            PAGE_TITLE,
            className="text-xl font-bold my-6",
        ),
        html.Div(id=ids.status, className="mb-6"),
        html.Div(id=ids.input, className="mb-6"),
        html.Div(id=ids.save_btn, className="mb-6"),
        html.Div(id=ids.feedback_save, className="mb-6"),
        html.Div(id=ids.run_btn, className="mb-6"),
        html.Div(id=ids.feedback_run, className="mb-6"),
        html.Div(id=ids.output, className="mb-6"),
    ],
    className="p-6 bg-blue-100 w-full",
)


@app.callback(Output(ids.status, "children"), [Input("url", "pathname")])
def display_page_message(pathname: str) -> str:
    message = "Message to test Callback"
    return message
