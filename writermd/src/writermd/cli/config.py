"""Subcommand to manage writermd settings."""

import typer
from typing import Annotated, Optional, List

app = typer.Typer("config", help="Manage WriterMD application configuration settings.")


@app.command("set")
def set_config(
    key: Annotated[str, typer.Argument(help="Configuration key to set.", )],
    value: Annotated[str, typer.Argument(help="Value to set for the configuration key.", )],
):
    """Set a configuration key to a specified value"""
    pass

@app.command("get")
def get_config(
    key: Annotated[Optional[str], typer.Argument(help="Configuration key to get. If not provided, all settings are shown.", )] = None,
):
    """Get the value of a configuration key or all settings"""
    pass


@app.command("list-projects")
def list_projects():
    """List all WriterMD projects in the application settings"""
    pass
