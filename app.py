from flask import Flask, request, jsonify
import pickle
import pandas as pd

app = Flask(__name__)

# Load Model
with open("model_training/churn_model.pkl", "rb") as file:
    model = pickle.load(file)

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df = pd.DataFrame([data])
    prediction = model.predict(df)[0]
    return jsonify({"prediction": int(prediction)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)
