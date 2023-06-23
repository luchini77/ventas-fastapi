from fastapi import APIRouter, Body, Path, Query, Request, HTTPException, Depends
from fastapi.security import HTTPBearer
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List

from jwt_config import valida_token
from config.base_datos import sesion, motor, base
from schema.ventas import Ventas as VentasShemas
from modelos.ventas import Ventas as VentasModelo
from modelos_auth.auth import Usuario


router_ventas = APIRouter()


#PORTADOR TOKEN
class Portador(HTTPBearer):
    async def __call__(self, request:Request):
        autorizacion = await super().__call__(request)
        dato = valida_token(autorizacion.credentials)

        if dato['email'] != 'kuky@lanegra.cl':
            raise HTTPException(status_code=401, detail='No Autorizado')


#TODAS LAS VENTAS
@router_ventas.get('/ventas', tags=['Ventas'], response_model=List[VentasShemas], status_code=200)
#@app.get('/ventas', tags=['Ventas'], response_model=List[Ventas], status_code=200, dependencies=[Depends(Portador())])
def dame_ventas() -> List[VentasShemas]:

    db = sesion()
    resultado = db.query(VentasModelo).all()

    return JSONResponse(content=jsonable_encoder(resultado), status_code=200)


#VENTAS POR ID
@router_ventas.get('/ventas/{id}', tags=['Ventas'], response_model=VentasShemas, status_code=200, dependencies=[Depends(Portador())])
def dame_ventas_id(id:int = Path(ge=1, le=1000)) -> VentasShemas:

    db = sesion()
    resultado = db.query(VentasModelo).filter(VentasModelo.id == id).first()
    if not resultado:
        return JSONResponse(content={'mensaje':'No se encontro ventas con ese ID'}, status_code=404)

    return JSONResponse(content=jsonable_encoder(resultado), status_code=200)

#AGREGAR UNA VENTA
@router_ventas.post('/ventas', tags=['Ventas'], response_model=dict, status_code=201, dependencies=[Depends(Portador())])
def crea_venta(venta: VentasShemas) -> dict:

    db = sesion()
    nueva_venta = VentasModelo(**venta.dict())
    db.add(nueva_venta)
    db.commit()

    return JSONResponse(content={'mensaje':'Venta Registrada'}, status_code=201)


#ACTUALIZAR VENTA
@router_ventas.put('/ventas/{id}', tags=['Ventas'], response_model=dict, status_code=200, dependencies=[Depends(Portador())])
def actualiza_ventas(id:int, venta:VentasShemas) -> dict:

    db = sesion()
    resultado = db.query(VentasModelo).filter(VentasModelo.id == id).first()

    if not resultado:
        return JSONResponse(content={'mensaje':'No se encontro la venta con ese ID'}, status_code=404)
    
    resultado.fecha = venta.fecha
    resultado.producto = venta.producto
    resultado.valor = venta.valor
    db.commit()

    return JSONResponse(content={'mensaje':'Venta Actualizada'}, status_code=200)


#ELIMINAR VENTA
@router_ventas.delete('/ventas/{id}', tags=['Ventas'], response_model=dict, status_code=200, dependencies=[Depends(Portador())])
def borrar_ventas(id:int) -> dict:

    db = sesion()
    resultado = db.query(VentasModelo).filter(VentasModelo.id == id).first()

    if not resultado:
        return JSONResponse(content={'mensaje':'No se encontro la venta con ese ID'}, status_code=404)

    db.delete(resultado)
    db.commit()

    return JSONResponse(content={'mensaje':'Venta Eliminada'}, status_code=200)