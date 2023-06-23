from pydantic import BaseModel, Field
from typing import Optional
from datetime import date


class Ventas(BaseModel):
    id: Optional[int] = None
    fecha: str
    producto: str = Field(min_length=4, max_length=10)
    valor: int

    class Config:
        schema_extra = {
            'example':{
                'fecha':date.today(),
                'producto':'Producto 1',
                'valor':1000
            }
        }