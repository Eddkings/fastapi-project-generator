import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir SQLAlchemy?", default=True)


def setup(project_path: Path):
    (project_path / "app" / "db" / "session.py").write_text(
        """from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql+asyncpg://user:password@localhost/dbname"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)
"""
    )

    requirements_path = project_path / "requirements.txt"
    with open(requirements_path, "a") as req:
        req.write("sqlalchemy\nasyncpg\ndatabases\n")

    print("📦 SQLAlchemy ha sido incluido.")
