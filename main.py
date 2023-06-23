from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from config.base_datos import base, motor
from routes.ventas import router_ventas
from routes.auth import router_auth


app = FastAPI()
app.title = 'Aplicacion Tienda Kukiana'
app.version = '1.0.1'


base.metadata.create_all(bind=motor)


#INICIO
@app.get('/', tags=['Inicio'])
def mensaje():
    return HTMLResponse('<h2>Api tienda Kukiana</h2>')


app.include_router(router_ventas)
app.include_router(router_auth)





#VENTAS POR TIENDA
# @app.get('/ventas/', tags=['Ventas'], response_model=List[Ventas], status_code=200)
# def dame_ventas_tienda(tienda:str = Query(min_length=4, max_length=20)) -> List[Ventas]:

#     db = sesion()
#     resultado = db.query(VentasModelo).filter(VentasModelo.tienda == tienda).all()

#     if not resultado:
#         return JSONResponse(content={'mensaje':'No se encontro esa tienda'}, status_code=404)

#     return JSONResponse(content=jsonable_encoder(resultado), status_code=200)
