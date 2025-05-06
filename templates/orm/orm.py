import typer
from . import sqlalchemy, sqlmodel
from pathlib import Path


def ask_orm_choice() -> str:
    orm_choices = ["sqlalchemy", "sqlmodel", "no usar"]
    choice = typer.prompt(
        "¿Qué ORM deseas usar?\n"
        + "\n".join(f"{i+1}. {orm}" for i, orm in enumerate(orm_choices))
        + "\nSelecciona el número correspondiente",
        type=int,
        default=1,
    )
    if 1 <= choice <= len(orm_choices):
        return orm_choices[choice - 1]
    else:
        typer.echo("Selección inválida. Usando sqlalchemy por defecto.")
        return "sqlalchemy"


def setup(project_path: Path, choice: str):
    orm_choice = choice.lower()
    if orm_choice == "sqlalchemy":
        sqlalchemy.setup(project_path)
    elif orm_choice == "sqlmodel":
        sqlmodel.setup(project_path)
    else:
        typer.echo("No se utilizará ningún ORM.")
