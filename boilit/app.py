import dash
from dash import dcc, html

from agility.skeleton.custom_components import Sidebar
from boilit.config.main import CONFIG_SIDEBAR, STORE_ID
from boilit.project import Project

external_scripts = [
    # Tailwind CSS from JS src file
    "https://cdn.tailwindcss.com/"
]


def init_app(
    server,
    project_slug,
    app_title,
):
    route_path_name = f"/{project_slug}/"
    dash_app = dash.Dash(
        __name__,
        server=server,
        routes_pathname_prefix=route_path_name,
        external_stylesheets=[
            "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.3/css/all.min.css",
        ],
        external_scripts=external_scripts,  # Tailwind CSS from JS src file
        title=app_title,  # Update title if needed or use a variable
        suppress_callback_exceptions=True,
        use_pages=True,
    )

    sidebar = Sidebar(CONFIG_SIDEBAR, STORE_ID, Project(), dash_app)

    dash_app.layout = html.Div(
        [
            dcc.Store(id=STORE_ID, storage_type="session", data=None),
            dcc.Location(id="url", refresh=False),
            html.Div(
                sidebar.layout(),
                className="w-96 border-r-2 border-gray-200 min-h-screen",
            ),
            html.Div(
                id="page-content", children=[dash.page_container], className="w-full"
            ),
        ],
        className="flex min-h-screen w-full bg-gray-100",
    )

    return dash_app
