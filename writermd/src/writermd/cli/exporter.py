"""Commands to export WriterMD projects to various formats."""

import typer
from typing import Annotated, Optional, List

app = typer.Typer()

@app.command("export")
def export_project(
    project_path: Annotated[str, typer.Option("--path", help="Path to the WriterMD project to export")] = "",
    output_format: Annotated[str, typer.Option("--format", "-f", help="Output format (e.g., pdf, epub, mobi)")] = "pdf",
    output_path: Annotated[Optional[str], typer.Option("--output", "-o", help="Path to save the exported file")] = None,
    sources_dir: Annotated[Optional[str], typer.Option("--sources", "-s", help="Path to the sources")] = None,

):
    """Exports a WriterMD project to the specified format.

    :param project_path: Path to the WriterMD project to export.
    :param output_format: Output format (e.g., pdf, epub, mobi).
    :param output_path: Path to save the exported file.
    """

    pass
