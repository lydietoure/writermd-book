"""Subcommand to manage writermd settings."""

from dataclasses import asdict
import json
import typer
from rich import print as rich_print
from typing import Annotated, Optional, List

from writermd.app.settings import (
    EDITABLE_SETTINGS,
    get_app_settings, save_application_settings, set_app_setting,
    list_projects as list_projects_func,
)

app = typer.Typer(name="config", help="Manage WriterMD application configuration settings.")


@app.command("set")
def set_config(
    key: Annotated[str, typer.Argument(help="Configuration key to set.", )],
    value: Annotated[str, typer.Argument(help="Value to set for the configuration key.", )],
):
    """Set a configuration key to a specified value"""

    if key.lower() not in EDITABLE_SETTINGS:
        typer.echo(f"Error: The configuration key '{key}' is not editable. Valid keys are: {', '.join(EDITABLE_SETTINGS)}")
        raise typer.Exit(1)

    set_app_setting(key.lower(), value)

@app.command("get")
def get_config(
    key: Annotated[Optional[str], typer.Argument(help="Configuration key to get. If not provided, all settings are shown.", )] = None,
):
    """Get the value of a configuration key or all settings"""
    s = get_app_settings()

    if key:
        key = key.lower()
        if key not in EDITABLE_SETTINGS:
            typer.echo(f"Error: The configuration key '{key}' is not recognized. Valid keys are: {', '.join(EDITABLE_SETTINGS)}")
            raise typer.Exit(1)
        value = getattr(s, key, None)
        rich_print(f"[bold]{key}[/bold]: {value}")

    else:
        rich_print(json.dumps(s.as_dict(), indent=4))


@app.command("list-projects")
def list_projects():
    """List all WriterMD projects in the application settings"""
    ls = list_projects_func(get_app_settings())
    rich_print(json.dumps([asdict(p) for p in ls], indent=4))
