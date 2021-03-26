from utils import Utils 
from models import Models

if __name__ == '__main__':
    
    # Instanciando 
    utils = Utils()
    models = Models()

    # Cargando nuestro dataset
    dataset = utils.load_from_csv('./data/felicidad.csv')

    # Partir nuestro dataset
    X, Y = utils.features_target(dataset, ['score', 'rank', 'country'], ['score'])

    models.grid_training(X, Y)