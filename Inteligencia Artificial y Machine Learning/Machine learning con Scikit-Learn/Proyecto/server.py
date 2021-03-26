import joblib
import numpy as np 

from flask import Flask
from flask import jsonify

app = Flask(__name__)

# POSTMAN para pruebas
@app.route('/predict', methods= ['GET'])
# Funcion para retornar una lista de predicciones
def predict():
    X_test = np.array([7.594444821,7.479555538,1.616463184,1.53352356,0.796666503,0.635422587,0.362012237,0.315963835,2.277026653])
    prediccion = model.predict(X_test.reshape(1, -1))
    return jsonify({'prediction': list(prediccion)})

if __name__ == '__main__':

    # Importar nuestro modelo
    model = joblib.load('./models/best_model.pkl')

    # Correr nuestro servidor en el puerto 8888 <- puede ser el que gusten
    app.run(port=8888)