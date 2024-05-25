from fastapi import FastAPI
from app.password import router as password_router  # Importar el enrutador desde password.py

app = FastAPI()

# Importar y agregar enrutadores aquí, si es necesario

# Rutas
app.include_router(password_router)  # Agregar el enrutador de contraseñas
