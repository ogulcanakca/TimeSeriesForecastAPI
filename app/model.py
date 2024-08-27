# app/model.py

import tensorflow as tf
import joblib
import numpy as np
from app.config import Config

class ModelHandler:
    def __init__(self):
        self.model = tf.keras.models.load_model(Config.MODEL_PATH)
        self.scaler = joblib.load(Config.SCALER_PATH)
    
    def predict(self, data):
        predictions_scaled = self.model.predict(data)
        
        predictions = self.scaler.inverse_transform(
            np.concatenate(
                (np.zeros((len(predictions_scaled), data.shape[2])), predictions_scaled),
                axis=1
            )
        )[:, -1]
        
        return predictions
