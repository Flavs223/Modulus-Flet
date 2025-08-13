@echo off
REM ==== Crear estructura del sistema de Producción e Inventarios ====

REM Carpeta raíz del proyecto
set PROYECTO=inventarios_produccion
mkdir %PROYECTO%

REM Entrar a la carpeta raíz
cd %PROYECTO%

REM Crear carpetas principales
mkdir entorno_virtual
mkdir src
mkdir src\views
mkdir src\controllers
mkdir src\models
mkdir src\assets
mkdir src\qss
mkdir src\utils
mkdir data
mkdir data\backups

REM Crear archivos iniciales
type nul > app.py
type nul > requirements.txt
type nul > .gitignore
type nul > src\__init__.py
type nul > src\views\__init__.py
type nul > src\controllers\__init__.py
type nul > src\models\__init__.py
type nul > src\utils\__init__.py
type nul > src\utils\helpers.py
type nul > src\utils\validators.py
type nul > src\models\database.py

echo *.pyc> .gitignore
echo __pycache__/>> .gitignore
echo entorno_virtual/>> .gitignore
echo data/backups/>> .gitignore

echo Estructura creada exitosamente.
pause
