# app/prediction_service.py

from fastapi import HTTPException
from app.model import ModelHandler
from app.utils import validate_csv, preprocess_data, create_time_steps
from app.config import Config

class PredictionService:
    def __init__(self):
        self.model_handler = ModelHandler()
    
    async def process_file(self, file):
        try:
            contents = await file.read()
            data = validate_csv(contents)
            data = preprocess_data(data)

            time_step = Config.TIME_STEP
            data = create_time_steps(data.to_numpy(), time_step)

            predictions = self.model_handler.predict(data)
            predictions_list = predictions.flatten().tolist()
            return predictions_list
        except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
