from pathlib import Path
import typer

def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir soporte para .env?", default=True)


def setup(project_path: Path):
    env_path = project_path / ".env"
    env_path.write_text(
        """# .env
DATABASE_URL=postgresql+asyncpg://user:password@localhost/dbname
SECRET_KEY=changeme
"""
    )

    # Agrega dotenv a requirements
    req_path = project_path / "requirements.txt"
    with open(req_path, "a") as f:
        f.write("python-dotenv\n")

    # Agrega carga de dotenv al main.py
    main_path = project_path / "app" / "main.py"
    content = main_path.read_text()
    content = "from dotenv import load_dotenv\nimport os\n\nload_dotenv()\n\n" + content
    main_path.write_text(content)

    print("📄 .env creado y cargado en main.py")
