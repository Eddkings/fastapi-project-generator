import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir autenticación JWT?", default=True)


def setup(project_path: Path):
    core_dir = project_path / "app" / "core"
    models_dir = project_path / "app" / "models"

    # security.py con funciones de JWT
    (core_dir / "security.py").write_text(
        """from datetime import datetime, timedelta
from jose import JWTError, jwt

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=15))
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
"""
    )

    # modelo de usuario base (puedes extenderlo luego)
    (models_dir / "user.py").write_text(
        """from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    disabled: bool = False
"""
    )

    # añadir dependencias
    req_file = project_path / "requirements.txt"
    with open(req_file, "a") as f:
        f.write("python-jose[cryptography]\npasslib[bcrypt]\n")

    print("🔐 JWT y autenticación básica añadida.")
