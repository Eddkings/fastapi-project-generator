import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir soporte para bases de datos?", default=True)


def ask_db_choice() -> str:
    db_choices = ["PostgreSQL", "MySQL", "SQLite", "Oracle", "SQLServer"]
    choice = typer.prompt(
        "¿Qué base de datos deseas usar?\n"
        + "\n".join(f"{i+1}. {db}" for i, db in enumerate(db_choices))
        + "\nSelecciona el número correspondiente",
        type=int,
        default=1,
    )
    # Validar rango
    if 1 <= choice <= len(db_choices):
        return db_choices[choice - 1]
    else:
        typer.echo("Selección inválida. Usando PostgreSQL por defecto.")
        return "PostgreSQL"


def setup(project_path: Path, db_choice: str):
    db_choice = db_choice.lower()
    db_url = ""

    # Definir URL de conexión según la base de datos seleccionada
    if db_choice == "postgresql":
        db_url = "postgresql+asyncpg://user:password@localhost/dbname"
    elif db_choice == "mysql":
        db_url = "mysql+aiomysql://user:password@localhost/dbname"
    elif db_choice == "sqlite":
        db_url = "sqlite+aiosqlite:///./test.db"
    elif db_choice == "oracle":
        db_url = "oracle+cx_oracle://user:password@localhost:1521/dbname"
    elif db_choice == "sqlserver":
        db_url = "mssql+pyodbc://user:password@localhost/dbname?driver=ODBC+Driver+17+for+SQL+Server"

    # Modificar `session.py` con la URL seleccionada
    (project_path / "app" / "db" / "session.py").write_text(
        f"""from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "{db_url}"

engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(
    bind=engine,
    expire_on_commit=False,
    class_=AsyncSession
)
"""
    )

    # Agregar dependencias a `requirements.txt`
    req_file = project_path / "requirements.txt"
    with open(req_file, "a") as f:
        if db_choice == "postgresql":
            f.write("asyncpg\n")
        elif db_choice == "mysql":
            f.write("aiomysql\n")
        elif db_choice == "sqlite":
            f.write("aiosqlite\n")
        elif db_choice == "oracle":
            f.write("cx_oracle\n")
        elif db_choice == "sqlserver":
            f.write("pyodbc\n")

    print(f"🔌 Soporte para {db_choice.capitalize()} agregado.")
