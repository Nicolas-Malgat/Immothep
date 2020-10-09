from fastapi import FastAPI, HTTPException

app = FastAPI()

http_exception = HTTPException(
            400
            , detail="""Les paramètres passés dans l'url ne sont pas complétés ou invalides:
            metre_carre (int): le nombre de m² habitables loi Carrez. Defaults to None.
            nb_pieces (int): nombre de pièces principales. Defaults to None.
            terrain (int): le nombre de m² du terrain. Defaults to None.
            code_postal (int): le code postal où se trouve le bien. Defaults to None.
            Exemple: https://website.com/maison?metre_carre=200&nb_piece=5&terrain=100&code_postal=63800"""
            , headers={"Paramètres invalides"}
        )

@app.get("/")
async def root():
    return {"message": "Hello World"}

    
@app.get("/maison")
async def estimation_maison(metre_carre: int = None, nb_pieces: int = None, terrain: int = None, code_postal: int = None):
    """Renvoie une estimation pour la maison passée en paramètre

    Args:
        metre_carre (int): le nombre de m² habitables loi Carrez. Defaults to None.
        nb_pieces (int): nombre de pièces principales. Defaults to None.
        terrain (int): le nombre de m² du terrain. Defaults to None.
        code_postal (int): le code postal où se trouve le bien. Defaults to None.

    Returns:
        json(jsp): Une estimation de la valeur de la maison
    """
    error = ""
    if not(metre_carre and nb_pieces and terrain and code_postal):
        raise http_exception
    
    raise NotImplemented()
    # return intelligence_artificielle.estimation_maison(metre_carre, nb_pieces, terrain, code_postal)
    