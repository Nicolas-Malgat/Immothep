from fastapi import FastAPI, HTTPException, exception_handlers
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException

app = FastAPI()

@app.exception_handler(StarletteHTTPException)
async def custom_http_exception_handler(request, exc):
    print(f"OMG! An HTTP error!: {repr(exc)}")
    return await http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc):
    print(f"OMG! The client sent invalid data!: {exc}")
    return await request_validation_exception_handler(request, exc)

@app.get("/")
async def root():
    return JSONResponse(content=jsonable_encoder({"message": "Hello world !"}))

@app.get("/maison")
async def estimation_maison(metre_carre: int, nb_pieces: int, terrain: int, code_postal: int):    
    raise HTTPException(404, detail="This api is not implemented yet :(")
    # return intelligence_artificielle.estimation_maison(metre_carre, nb_pieces, terrain, code_postal)
    