# app/config.py

class Config:
    MODEL_PATH = './model/model.keras'
    SCALER_PATH = './scaler/scaler.save'
    TIME_STEP = 60
    COLUMN_MAPPING = {
            'close': 'close',
            'adj close': 'adj close',
            'adj_close': 'adj close',
            'adjclose': 'adj close'
        }
