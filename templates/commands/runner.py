from typer import Typer
import subprocess
from pathlib import Path

app = Typer()


@app.command()
def run(path: str = "."):
    """Inicia el servidor FastAPI con Uvicorn."""
    main_path = Path(path) / "app" / "main.py"
    if not main_path.exists():
        print("❌ No se encontró app/main.py en el path indicado.")
        return

    print("🚀 Iniciando FastAPI con Uvicorn...")
    subprocess.run(["uvicorn", "app.main:app", "--reload"])
