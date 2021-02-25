# Importando librerias necesarias
import pandas as pd
import joblib

class Utils:

    # Funcion para cargar un archivo .csv 
    def load_from_csv(self, path):
        return pd.read_csv(path)

    # Funcion para crear nuestras features y el target
    def features_target(self, dataset, drop_cols, Y):
        X = dataset.drop(drop_cols, axis=1)
        Y = dataset[Y]
        return X, Y

    # Funcion para exportar nuestro modelo
    def model_export(self, clf, score):
        print('Best score: ', score * 100)
        joblib.dump(clf, './models/best_model.pkl')