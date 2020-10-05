import pandas as pd
from os import path, makedirs

class csvLoader:

    LOCATION = r'../datas/CURATED/'

    @staticmethod
    def save(df: pd.DataFrame, name: str):
        if '.csv' not in name:
            name = name + '.csv'

        csvLoader.__check_location()

        df.to_csv(name)

    @staticmethod
    def load(name: str):
        if '.csv' not in name:
            name = name + '.csv'

        pd.read_csv('{}{}'.format(csvLoader.LOCATION, name), encoding='utf-8')
        print('Successfully created ', name)

    @staticmethod
    def __check_location():
        
        if path.exists(csvLoader.LOCATION) == False:
            try:
                makedirs(csvLoader.LOCATION)
            except OSError:
                print ("Creation of the directory %s failed" % csvLoader.LOCATION)
                exit(1)
            else:
                print ("Successfully created the directory %s " % csvLoader.LOCATION)