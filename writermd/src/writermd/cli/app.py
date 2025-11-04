import typer

from writermd.cli.creator import app as creator_app
from writermd.cli.config import app as configurator_app

app = typer.Typer(
    name = "writermd",
    help = "A utility project to aid writers organise and generate manuscripts from markdown files",
)

app.add_typer(
    creator_app
)
app.add_typer(
    configurator_app,
    name="config"
)

def main():
    app()

if __name__ == "__main__":
    main()
