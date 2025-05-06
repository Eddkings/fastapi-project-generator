import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir un Dockerfile?", default=True)


def setup(project_path: Path):
    dockerfile = project_path / "Dockerfile"
    dockerfile.write_text(
        """FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
    )

    dockerignore = project_path / ".dockerignore"
    dockerignore.write_text(
        """__pycache__/
*.pyc
.env
"""
    )

    print("🐳 Dockerfile y .dockerignore añadidos.")
