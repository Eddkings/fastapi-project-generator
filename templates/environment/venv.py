import typer
import subprocess
from pathlib import Path

def ask_to_include() -> bool:
    return typer.confirm("¿Deseas crear un entorno virtual (venv) para este proyecto?", default=True)

def setup(project_path: Path):
    venv_path = project_path / "venv"
    print("🛠️ Creando entorno virtual...")
    subprocess.run(["python3", "-m", "venv", str(venv_path)])
    print(f"✅ Entorno virtual creado en: {venv_path}")
    print(f"\nPara activarlo, ejecuta:\n  source {venv_path}/bin/activate\n")