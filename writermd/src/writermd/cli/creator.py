"""Creates a new WriterMD project structure in the specified directory."""

import typer
from pathlib import Path
from typing import Annotated, Optional, List

from writermd.app.project import (
    SAMPLE_WIP_PATH, CONFIG_FILE_NAME,
    validate_project_structure,
    create_sample_project,
    load_project, write_config
)
import shutil

from writermd.app.settings import add_project, get_app_settings
from writermd.exceptions import WriterMDError

# No name/description, so that it inherits from the main app
app = typer.Typer()

@app.command("create")
def create_project(
    project_name: Annotated[str, typer.Argument(metavar="NAME", help="Name of the project to create")],
    dir_path: Annotated[Optional[str], typer.Option("-directory", "-d", help="Parent directory where the project should be created. Defaults to current directory.")] = None,
    path: Annotated[Optional[str], typer.Option("--path", "-p", help="Path where the project should be created. Overrides --dir if provided.")]= None,
    src_dir_override: Annotated[Optional[str], typer.Option("--sources-dir", "-s", help="Custom name for the sources directory")] = None,
    author: Annotated[Optional[str], typer.Option("--author", "-a", help="Author name to set in the project config")] = None,
    template: Annotated[Optional[str], typer.Option("--template", help="Template to use (dev only)")]= None,
):
    """Creates a new WriterMD project structure in the specified directory.
    """

    parent_dir: Path = Path(dir_path) if dir_path else Path.cwd()

    if not path:
        # Sanitize project name
        sanitised_name = project_name.replace("'", "").replace('"', "").replace(" ", "-").lower()
        proj_path = parent_dir / sanitised_name
    else:
        proj_path = Path(path)

    if proj_path.exists():
        typer.echo(f"Error: The specified path '{path}' already exists.")
        raise typer.Exit(1)

    author = author or get_app_settings().author

    proj = create_sample_project(name=project_name, path=proj_path, author=author, sources_dir=src_dir_override, template_path=template)

    add_project(get_app_settings(), proj_path)



@app.command("rename")
def rename_project(
    project_path: Annotated[str, typer.Argument(help="Path to the existing project")],
    new_name: Annotated[str, typer.Option("--name", "-n", help="New name for the project")],
):
    """Renames an existing WriterMD project.

    :param project_path: Path to the existing project.
    :param new_name: New name for the project.
    """

    try:
        config = validate_project_structure(Path(project_path))
    except Exception as e:
        typer.echo(f"Error: {e}") # use your own logging?
        raise typer.Exit(1) from e

    config.name = new_name

def create_review_questionaire(
    project_path: Annotated[str, typer.Argument(help="Path to the existing project")],
    reviewers: Annotated[List[str], typer.Option("--reviewer", "-r", help="List of reviewers' names")] = [],
    output_path: Annotated[Optional[str], typer.Option("--output", "-o", help="Path to save the generated questionnaire. Defaults to the review folder")] = None,
):
    """Generates a reviewer questionnaire for the project.

    :param project_path: Path to the existing project.
    :param reviewers: List of reviewers' names.
    :param output_path: Path to save the generated questionnaire. Defaults to the review folder.
    """
    try:
        config = validate_project_structure(Path(project_path))
    except Exception as e:
        typer.echo(f"Error: {e}") # use your own logging?
        raise typer.Exit(1) from e



# def _create_directory_structure(project_name: str, path: Path):

#     # Copy the sample WIP structure to the new project directory
#     destination = path / project_name
#     shutil.copytree(SAMPLE_WIP_PATH, path)

#     # Edit the config file to set the project name
#     config_yaml = destination / CONFIG_FILE_NAME
#     config = load_project(config_yaml)
#     config.name = project_name

#     write_config(config_yaml)

#     # Note that all the paths are relative to the project root (where the writermd.yaml is located)

# TODO: Update the other files that may contain the project name?
# Use str.Template
