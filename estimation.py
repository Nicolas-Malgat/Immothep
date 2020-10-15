import pickle
from sklearn.linear_model import LinearRegression
import pandas as pd


class EstimationBien():
    """
    Cette classe contient une méthode afin donner une prédiction
    """
    @staticmethod
    def estimation(nb_piece: int, surface: float, prix_metre:float):
        """Estime la valeur d'un bien, renvoie deux estimations pour un appartement et pour une maison

        Args:
            nb_piece (int): Nombre de pieces du bien
            surface (float): Surface en m² du bien
            prix_metre (float): Prix en m² du bien

        Returns:
            dict: contient les deux estimations
        """
        print('Estimation en cours ...')

        d = {'0': [nb_piece],'1': [surface],'2': [prix_metre]}
        df_test = pd.DataFrame(data=d)

        modele_lineaire_appart: LinearRegression = pickle.load(open("modele_lineaire_appartement.p","rb"))
        estimation_appart = modele_lineaire_appart.predict(df_test)
        print('Une estimation a été donnée pour un appartement: ', estimation_appart)

        modele_lineaire_maison: LinearRegression = pickle.load(open("modele_lineaire_maison.p","rb"))
        estimation_maison = modele_lineaire_maison.predict(df_test)
        print('Une estimation a été donnée pour une maison: ', estimation_maison)

        return {
            'estimation_maison': estimation_maison,
            'estimation_appart': estimation_appart
        }