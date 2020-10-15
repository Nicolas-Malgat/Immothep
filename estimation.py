import pickle
from pandas.core.frame import DataFrame, Series
from pandas.core.indexes.base import Index
from sklearn.linear_model import LinearRegression
import pandas as pd
from modules.csvLoader import csvLoader


class EstimationBien():
    """
    Cette classe contient une méthode afin donner une prédiction
    """
    @staticmethod
    def getPrixMetreParCodePostalCordialement(code_postal: int):
    
        df_prix_metre_maison: DataFrame = csvLoader.load('prix_metre_maison')
        try:
            prix_metre_maison = df_prix_metre_maison.iloc[code_postal]['Prix metre carre']
        except IndexError as e:
            prix_metre_maison = e

        df_prix_metre_appartement: DataFrame = csvLoader.load('prix_metre_appartement')
        try:
            prix_metre_appart = df_prix_metre_appartement.iloc[code_postal]['Prix metre carre']
        except IndexError as e:
            prix_metre_appart = e

        return {
            'maison': prix_metre_maison,
            'appartement': prix_metre_appart
        }

    @staticmethod
    def estimation(nb_piece: int, surface: float, prix_metre: dict):
        """Estime la valeur d'un bien, renvoie deux estimations pour un appartement et pour une maison

        Args:
            nb_piece (int): Nombre de pieces du bien
            surface (float): Surface en m² du bien
            prix_metre (float): Prix en m² du bien

        Returns:
            dict: contient les deux estimations
        """
        print('Estimation en cours ...')

        prix_metre_maison = prix_metre['maison']
        prix_metre_appart = prix_metre['appartement']

        if isinstance(prix_metre_appart, IndexError):
           estimation_appart = "Aucune estimation pour un appartement n'a pu être donnée à cause du code postal" 
           print(estimation_appart)
        else:
            d = {'0': [nb_piece],'1': [surface],'2': [prix_metre_appart]}
            df_test = pd.DataFrame(data=d)
            modele_lineaire_appart: LinearRegression = pickle.load(open("modele_lineaire_appartement.p","rb"))
            estimation_appart = modele_lineaire_appart.predict(df_test)[0]
            print('Une estimation a été donnée pour un appartement: ', estimation_appart)

        if isinstance(prix_metre_maison, IndexError):
           estimation_maison = "Aucune estimation pour une maison n'a pu être donnée à cause du code postal" 
           print(estimation_maison)
        else:
            d = {'0': [nb_piece],'1': [surface],'2': [prix_metre_maison]}
            df_test = pd.DataFrame(data=d)
            modele_lineaire_maison: LinearRegression = pickle.load(open("modele_lineaire_maison.p","rb"))
            estimation_maison = modele_lineaire_maison.predict(df_test)[0]
            print('Une estimation a été donnée pour une maison: ', estimation_maison)

        return {
            'estimation_maison': estimation_maison,
            'estimation_appart': estimation_appart
        }

if __name__ == "__main__":

    metre_carre: float = 64.1
    nb_pieces: int = 4
    terrain: float = 78.1
    code_postal: int = 1000
    
    prix_metre: dict = EstimationBien.getPrixMetreParCodePostalCordialement(code_postal)
    estimations: dict = EstimationBien.estimation(nb_pieces, metre_carre, prix_metre)

    print(estimations)
