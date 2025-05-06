import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir SQLModel?", default=True)


def setup(project_path: Path):
    (project_path / "app" / "db" / "session.py").write_text(
        """from sqlmodel import SQLModel, create_engine, Session

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, echo=True)

def get_session():
    with Session(engine) as session:
        yield session
"""
    )

    requirements_path = project_path / "requirements.txt"
    with open(requirements_path, "a") as req:
        req.write("sqlmodel\n")

    print("📦 SQLModel ha sido incluido.")
