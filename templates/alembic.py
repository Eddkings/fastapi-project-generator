import typer
from pathlib import Path
import subprocess


def ask_to_include() -> bool:
    return typer.confirm(
        "¿Deseas incluir soporte para migraciones con Alembic?", default=True
    )


def setup(project_path: Path):
    subprocess.run(["pip", "install", "alembic"])

    # Inicializar Alembic
    subprocess.run(["alembic", "init", "app/alembic"])

    # Crear archivo de configuración `alembic.ini` (modificado para soportar bases de datos dinámicas)
    alembic_ini = project_path / "app/alembic/alembic.ini"
    with open(alembic_ini, "a") as f:
        f.write("\n# Base de datos URL configurada por Alembic")
        f.write("\nsqlalchemy.url = driver://user:pass@localhost/dbname")

    print("⚙️ Alembic configurado para migraciones.")
