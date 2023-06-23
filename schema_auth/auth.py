from pydantic import BaseModel, EmailStr


class Usuario(BaseModel):
    email: EmailStr
    clave: str 