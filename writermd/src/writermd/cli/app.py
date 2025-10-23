import typer

from writermd.cli.creator import app as creator_app

app = typer.Typer(
    name = "writermd",
    help = "A utility project to aid writters organise and generate manuscripts from markdown files",
)

app.add_typer(
    creator_app
)

def main():
    app()

if __name__ == "__main__":
    main()