from fastapi import FastAPI
from fastapi.exception_handlers import (
    http_exception_handler,
    request_validation_exception_handler,
)
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from starlette.exceptions import HTTPException as StarletteHTTPException

from estimation import EstimationBien
from modules.csvLoader import csvLoader

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
    return JSONResponse(content=jsonable_encoder(
        {
            "estimate": "http://127.0.0.1:5003/estimate?metre_carre=30&nb_pieces=4&terrain=0&code_postal=1000",
            "code_postal": "http://127.0.0.1:5003/code_postal"
        }
    ))

@app.get("/code_postal")
async def root():
    
    df = csvLoader.load('prix_metre_maison').astype({"Code postal": int})
    data = df['Code postal'].to_dict()
    return JSONResponse(
        content = data 
    )

@app.get("/estimate")
async def estimation_maison(metre_carre: float, nb_pieces: int, terrain: float, code_postal: int):

    prix_metre_carre: dict = EstimationBien.getPrixMetreParCodePostalCordialement(code_postal)
    estimation: dict = EstimationBien.estimation(nb_pieces, metre_carre, prix_metre_carre)

    return JSONResponse({
            'request': {
                'metre_carre': metre_carre,
                'nb_pieces': nb_pieces,
                'terrain': terrain,
                'code_postal': code_postal
            },
            'response': estimation
    })
    # raise HTTPException(404, detail="This api is not implemented yet :(")
    # return intelligence_artificielle.estimation_maison(metre_carre, nb_pieces, terrain, code_postal)
    