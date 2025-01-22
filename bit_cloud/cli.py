import typer
from .objects import ObjectType
from pathlib import Path

app = typer.Typer()

@app.command(help="Read contents of the bit object", rich_help_panel="inspect")
def show(type: ObjectType = typer.Option(ObjectType.BLOB, "-t", "--type", show_choices=True), file: Path = typer.Argument(..., exists=True)):
    typer.echo(f"cat_file: {type}")

@app.command(help="hash the file and (optionally) write it to the object store", rich_help_panel="inspect")
def hash(file: Path = typer.Argument(..., exists=True), write: bool = typer.Option(False, "-w", "--write"), type: ObjectType = typer.Option(ObjectType.BLOB, "-t", "--type", show_choices=True)):
    typer.echo(f"hash_object: {file} {write} {type}")

@app.command(help="initialize a new bit repository", rich_help_panel="creation")
def init():
    typer.echo("init")
    dire = Path(".bit")
    curr = Path(".")
    dire.mkdir(exist_ok=True)
    (dire / "objects").mkdir()
    (dire/"config.toml").write_text(
        f"""
[repo]
name = {curr.name}
ctr = 0
"""
    )
