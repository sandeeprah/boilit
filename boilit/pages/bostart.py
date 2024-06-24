"""Start page for the boilit application."""

import json
import os
import dash
from typing import Final
from pathlib import Path
from dash import Dash, Input, Output, State, dcc, html
from dash.exceptions import PreventUpdate
from agility.skeleton.custom_components import (
    ButtonCustom,
    InputCustom,
    MessageCustom,
    FileHandler
)

from boilit.config.main import STORE_ID, PROJECT_NAME, PROJECT_SLUG
from boilit.project import Project, start


# from my_dash_app.components.file_handler import FileHandler

dash.register_page(__name__)
app: Dash = dash.get_app()


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
        self.file_name: Final[str] = f"{prefix}_file_name"
        self.client_name: Final[str] = f"{prefix}_client_name"
        self.project_name: Final[str] = f"{prefix}_project_name"
        self.project_description: Final[str] = f"{prefix}_project_description"
        self.root_message: Final[str] = f"{prefix}_root_message"


ids = PageIDs()


 # Get the directory where run.py is located
BASE_DIR = Path(__file__).resolve().parent.parent
# Get path to project_default.json file 
PROJECT_DEFAULT_PATH = BASE_DIR / "config/project_default.json"
file_handler = FileHandler(
    PROJECT_SLUG, STORE_ID, PROJECT_DEFAULT_PATH, Project(), app
)

START_HELP_TEXT = """

To begin create a New Project or Open an existing project by uploading a project file.
"""

layout = (
    html.Div(
        [
            html.H1(
                PROJECT_NAME,
                className="text-2xl font-bold",
            ),
            html.H2(
                "Start",
                className="text-xl font-bold my-6",
            ),
            html.P(START_HELP_TEXT, className="my-12"),
            html.Div(
                children=[
                    file_handler.layout,
                ],
                className="my-12 w-full",
            ),
            html.Div(id=ids.feedback_save, className="my-12"),
            html.Div(id=ids.input, className="my-12"),
            #      html.Div(id="project_settings", className="my-12"),
        ],
        className="p-6",
    ),
)


@app.callback(
    Output(ids.input, "children"),
    [Input(STORE_ID, "data"), Input("url", "pathname")],
)
def meta_input_display(data, pathname):
    if not data:
        return None
    data = data or {}  # Ensure data is always a dictionary
    meta_input = data.get("meta_input", {})
    meta_input, error_messages = start.validate_meta_input(meta_input)

    # meta_input = project_data.get("meta_input", {})
    file_name = InputCustom(
        id=ids.file_name,
        label="File Name",
        value=meta_input.get("file_name", ""),
        error_message=error_messages.get("file_name", ""),
    )
    client_name = InputCustom(
        id=ids.client_name,
        label="Client Name",
        value=meta_input.get("client_name", ""),
        error_message=error_messages.get("client_name", ""),
    )
    project_name = InputCustom(
        id=ids.project_name,
        label="Project Name",
        value=meta_input.get("project_name", ""),
        error_message=error_messages.get("project_name", ""),
    )
    project_description = InputCustom(
        id=ids.project_description,
        label="Project Description",
        value=meta_input.get("project_description", ""),
        error_message=error_messages.get("project_description", ""),
    )

    root_message = MessageCustom(messages=error_messages.get("__root__"), success=False)

    # Create a simple form layout
    meta_input_layout = html.Div(
        [
            html.H1("Project Information", className="text-2xl font-bold w-1/2"),
            file_name.layout,
            client_name.layout,
            project_name.layout,
            project_description.layout,
            html.Div(
                root_message.layout,
                className="mt-4",
            ),
            ButtonCustom(ids.save_btn, "Save").layout,
        ],
    )
    return meta_input_layout


@app.callback(
    Output(STORE_ID, "data", allow_duplicate=True),
    Input(
        ids.save_btn,
        "n_clicks",
    ),  # Assuming your save button has an ID with "-save" postfix
    State(ids.file_name, "value"),
    State(ids.client_name, "value"),
    State(ids.project_name, "value"),
    State(ids.project_description, "value"),
    State(STORE_ID, "data"),
    prevent_initial_call=True,  # Prevent the callback from running on initial load
)
def update_project_meta_input(
    n_clicks,
    file_name,
    client_name,
    project_name,
    project_description,
    data,
):
    if n_clicks is None:
        raise PreventUpdate  # Do nothing if the button hasn't been clicked

    # Check if the store already contains data to prevent overwriting other data unintentionally.
    if data is None or "meta_input" not in data:
        raise PreventUpdate
    meta_input = {}
    meta_input["file_name"] = file_name
    meta_input["client_name"] = client_name
    meta_input["project_name"] = project_name
    meta_input["project_description"] = project_description

    meta_input, errors = start.validate_meta_input(meta_input)
    if not errors:
        data["meta_input"] = meta_input
        return data
    return dash.no_update
