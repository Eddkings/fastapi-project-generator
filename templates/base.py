from pathlib import Path


def create_structure(name: str) -> Path:
    project_path = Path(name)
    if project_path.exists():
        print("❌ La carpeta ya existe.")
        exit(1)

    folders = [
        "app/api",
        "app/core",
        "app/db",
        "app/models",
        "app/schemas",
        "app/services",
        "app/tests",
    ]

    for folder in folders:
        (project_path / folder).mkdir(parents=True, exist_ok=True)

    (project_path / "app" / "main.py").write_text(
        """from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hola desde FastAPI!"}
"""
    )

    (project_path / "requirements.txt").write_text("fastapi\nuvicorn[standard]\n")

    return project_path
