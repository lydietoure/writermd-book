"""Commands to export WriterMD projects to various formats."""

import typer
import pandoc
from typing import Annotated, Optional, List

app = typer.Typer()

@app.command("export")
def export_project(
    project_path: Annotated[str, typer.Option("--path", help="Path to the WriterMD project to export")] = "",
    output_format: Annotated[str, typer.Option("--format", "-f", help="Output format (e.g., pdf, epub, mobi)")] = "pdf",
    output_path: Annotated[Optional[str], typer.Option("--output", "-o", help="Path to save the exported file")] = None,
    sources_dir: Annotated[Optional[str], typer.Option("--sources", "-s", help="Path to the sources")] = None,
    toc_depth: Annotated[Optional[int], typer.Option("--toc-depth", help="Depth of the table of contents")] = 2,

):
    """Exports a WriterMD project to the specified format.

    :param project_path: Path to the WriterMD project to export.
    :param output_format: Output format (e.g., pdf, epub, mobi).
    :param output_path: Path to save the exported file.
    """

    files: List[str] = []
    file_name: str = "chapter1.md"
    # converted_docs = pandoc.read(file_name, format="markdown")

    # doc = pandoc.read(files, format="markdown",
    #     options=[
    #         "--metadata", "title:My Book Title",
    #         "--metadata", "author:Author Name",
    #         "--metadata", "date:2024-01-01",
    #         "--extract-media=<images_dir>"
    #     ]
    # )
    # pandoc.write(
    #     doc, file_name, format=output_format,
    #     options=[
    #         "--toc=true",
    #         "--toc-depth=1",
    #         "--resource-dir=<sources_dir>",
    #     ]
    # )
