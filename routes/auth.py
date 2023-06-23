from fastapi import APIRouter
from fastapi.responses import JSONResponse

from jwt_config import dame_token
from schema_auth.auth import Usuario

router_auth = APIRouter()


#RUTA PARA EL LOGIN
@router_auth.post('/login', tags=['Autenticacion'])
def login(usuario:Usuario):
    if usuario.email == 'kuky@lanegra.cl' and usuario.clave == '123456':
        #OBTENEMOS TOKEN
        token:str = dame_token(usuario.dict())
        return JSONResponse(status_code=200, content=token)
    else:
        return JSONResponse(content={'mensaje':'Acceso Denegado'}, status_code=401)

