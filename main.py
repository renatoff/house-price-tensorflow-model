from flask import Flask, request, jsonify
import pandas as pd
from keras.models import model_from_json

# Load model architecture from JSON
with open('model.json', 'r') as json_file:
    loaded_model_json = json_file.read()
loaded_model = model_from_json(loaded_model_json)

# Load weights into the new model
loaded_model.load_weights("model.weights.h5")

# Compile the model if necessary
loaded_model.compile(loss='mean_squared_error', optimizer='adam')

app = Flask(__name__)

@app.route('/predict', methods=['POST'])
def predict():
    # Get JSON data from the request
    data = request.get_json()

    df = pd.read_json(data)

    # Make predictions using the loaded model
    predictions = loaded_model.predict(df)
    
    # Convert the predictions to a list
    data = predictions.tolist()
    
    # Return the received data as a JSON response
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)