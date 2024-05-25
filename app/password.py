from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import random
import string

router = APIRouter()

class PasswordRequest(BaseModel):
    length: int

def generate_password(length: int) -> str:
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

@router.post("/generate-password/")
async def generate_password_endpoint(password_request: PasswordRequest):
    if password_request.length < 8:
        raise HTTPException(status_code=400, detail="La longitud de la contraseña debe ser al menos 8 caracteres")
    return {"password": generate_password(password_request.length)}
