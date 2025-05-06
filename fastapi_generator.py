from typer import Typer
from templates import (
    base,
    docker,
    alembic,
)
from templates.db import db
from templates.environment import env
from templates.orm import orm
from templates.requirements import generar_requirements, opciones
import templates.commands.runner as runner
from templates.security import jwt
from templates.test import pytest

app = Typer()
app.command()(runner.run)


@app.command()
def new(name: str):
    """Crea un nuevo proyecto FastAPI con opciones personalizadas."""

    project_path = base.create_structure(name)

    if db.ask_to_include():
        db_choice = db.ask_db_choice()
        db.setup(project_path, db_choice)
        opciones["db"] = db_choice

    orm_choice = orm.ask_orm_choice()
    opciones["orm"] = orm_choice
    orm.setup(project_path, orm_choice)

    if jwt.ask_to_include():
        jwt.setup(project_path)
        opciones["usar_jwt"] = True

    if docker.ask_to_include():
        docker.setup(project_path)

    if env.ask_to_include():
        env.setup(project_path)

    if alembic.ask_to_include():
        alembic.setup(project_path)
        opciones["usar_alembic"] = True

    if pytest.ask_to_include():
        pytest.setup(project_path)
        opciones["usar_pytest"] = True

    generar_requirements(
        project_path=str(project_path),
        usar_jwt=opciones["usar_jwt"],
        usar_alembic=opciones["usar_alembic"],
        usar_pytest=opciones["usar_pytest"],
        db=opciones["db"],
        orm=opciones["orm"],
    )

    print(f"✅ Proyecto {name} creado exitosamente en {project_path}.")


if __name__ == "__main__":
    app()
