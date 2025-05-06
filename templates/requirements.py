import os


def generar_requirements(
    project_path: str,
    usar_jwt=False,
    usar_alembic=False,
    usar_pytest=False,
    db: str = "sqlite",
    orm: str = "sqlalchemy",
):
    requirements = ["fastapi", "uvicorn[standard]", "python-dotenv"]

    if orm == "sqlalchemy":
        requirements.append("sqlalchemy")
    elif orm == "sqlmodel":
        requirements.append("sqlmodel")

    if usar_jwt:
        requirements.extend(["python-jose[cryptography]", "passlib[bcrypt]"])

    if usar_alembic:
        requirements.append("alembic")

    if usar_pytest:
        requirements.extend(["pytest", "httpx"])

    db = db.lower()
    if db == "postgresql":
        requirements.append("psycopg2-binary")
    elif db == "mysql":
        requirements.append("pymysql")
    elif db == "sqlite":
        requirements.append("sqlite-utils")
    elif db == "oracle":
        requirements.append("oracledb")
    elif db == "sqlserver":
        requirements.append("pyodbc")

    req_path = os.path.join(project_path, "requirements.txt")
    with open(req_path, "w") as f:
        f.write("\n".join(requirements))

    print(f"✅ Archivo requirements.txt generado en: {req_path}")


opciones = {
    "usar_jwt": True,
    "usar_alembic": True,
    "usar_pytest": True,
    "db": "sqlite",
    "orm": "sqlalchemy",
}
