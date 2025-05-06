# FastAPI Project Generator

Este generador de proyectos FastAPI facilita la creación rápida de un proyecto con configuración personalizada. Permite seleccionar opciones como base de datos, ORM (SQLAlchemy o SQLModel), autenticación JWT, Docker, migraciones con Alembic y pruebas con Pytest.

## 🚀 Instalación

### Requisitos

- Python 3.7 o superior
- `pip` (para instalar dependencias)

### Instalación

1. **Clona el repositorio:**

   ```bash
   git clone https://github.com/Eddkings/fastapi-project-generator.git
   cd fastapi-project-generator
   ```

2. **Instala las dependencias:**

   Asegúrate de tener `pip` actualizado y luego instala las dependencias del generador:

   ```bash
   pip install -r requirements.txt
   ```

## 🛠 Uso

### Generar un nuevo proyecto

Para generar un nuevo proyecto, ejecuta el siguiente comando. El generador te guiará paso a paso para personalizar tu proyecto:

```bash
python fastapi_generator.py new <nombre_del_proyecto>
```

Durante la generación, podrás elegir:

- **Base de datos:** PostgreSQL, MySQL, SQLite, Oracle o SQLServer.
- **ORM:** SQLAlchemy, SQLModel o ninguno.
- **Autenticación JWT:** Incluir o no autenticación basada en JWT.
- **Docker:** Incluir o no archivos de configuración para Docker.
- **Variables de entorno:** Incluir o no soporte para `.env`.
- **Migraciones Alembic:** Incluir o no soporte para migraciones de base de datos.
- **Pytest:** Incluir o no configuración para pruebas automáticas.

Al finalizar, encontrarás tu nuevo proyecto en una carpeta con el nombre que hayas elegido.
