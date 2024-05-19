import os
from flask import Flask, request, jsonify
import joblib
import traceback

app = Flask(__name__)

# Get the absolute path of the current directory
current_dir = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(current_dir, 'SVM_model.pkl')
print(f"Loading model from: {model_path}")

# Load pre-trained model
model = joblib.load(model_path)

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Expecting a JSON array in the request body
        data = request.json

        # Check if the input is a list with 20 elements
        if not isinstance(data, list) or len(data) != 20:
            return jsonify({"error": "Invalid input data"}), 400

        # Extract features from the input data list
        features = data

        # Perform prediction
        prediction = model.predict([features])

        # Convert the prediction to a native Python int type
        predicted_price = int(prediction[0])

        # Return the predicted class
        return jsonify({"predicted price category is": predicted_price})
    except Exception as e:
        print("Error occurred:", e)
        print(traceback.format_exc())
        return jsonify({"error": f"An error occurred during prediction: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)