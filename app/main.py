# app/main.py
from fastapi import FastAPI, File, UploadFile, HTTPException
from app.prediction_service import PredictionService
import uvicorn


app = FastAPI(
    title="Stock Price Prediction API",
    description="An API to predict stock prices based on historical data.",
    version="1.0.0"
)

prediction_service = PredictionService()

@app.post("/predict/", response_model=dict)
async def predict(file: UploadFile = File(...)):
    try:
        predictions = await prediction_service.process_file(file)
        return {
            "predictions": predictions
        }
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
