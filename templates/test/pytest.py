import typer
from pathlib import Path


def ask_to_include() -> bool:
    return typer.confirm("¿Deseas incluir Pytest para pruebas?", default=True)


def setup(project_path: Path):
    # Crear un archivo de configuración básico de pytest
    pytest_ini = project_path / "pytest.ini"
    pytest_ini.write_text(
        """[pytest]
addopts = --maxfail=1 --disable-warnings -q
"""
    )

    # Crear un ejemplo básico de prueba
    test_example = project_path / "app/tests/test_example.py"
    test_example.write_text(
        """import pytest

def test_example():
    assert 1 + 1 == 2
"""
    )

    print("🧪 Pytest configurado con pruebas de ejemplo.")
