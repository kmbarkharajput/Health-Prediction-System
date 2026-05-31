import os
import joblib
from django.conf import settings

MODEL_PATH = os.path.join(settings.BASE_DIR, "health_model.pkl")

model = None

try:
    if os.path.exists(MODEL_PATH):
        model = joblib.load(MODEL_PATH)
        print("ML Model Loaded Successfully")
    else:
        print("health_model.pkl not found")
except Exception as e:
    print(f"Error loading model: {e}")


def predict_health(glucose, haemoglobin, cholesterol):
    if model is None:
        return "Model Not Available"

    try:
        input_data = [[
            float(glucose),
            float(haemoglobin),
            float(cholesterol)
        ]]

        prediction = model.predict(input_data)

        return prediction[0]

    except Exception as e:
        return f"Prediction Error: {str(e)}"