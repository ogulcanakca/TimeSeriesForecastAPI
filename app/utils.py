# app/utils.py

import pandas as pd
import numpy as np
import io
from fastapi import HTTPException
from app.config import Config


def validate_csv(file_contents):
    try:  
        data = pd.read_csv(io.StringIO(file_contents.decode('utf-8')))
        if data.empty:
            raise ValueError("CSV file is empty or file is not CSV.")
        
        return data
    
    except pd.errors.EmptyDataError:
        raise ValueError("CSV file is empty.")
    
    except pd.errors.ParserError:
        raise ValueError("Invalid CSV file format.")
    
    except UnicodeDecodeError:
        raise ValueError("Unable to decode the CSV file, check the file encoding.")
    
    except Exception as e:
        raise ValueError("An unexpected error occurred while processing the CSV file. Error: " + str(e))

def preprocess_data(df):
    required_columns = ['open', 'high', 'low', 'volume']
    df_columns_lower = [col.lower().strip() for col in df.columns]

    for column in required_columns:
        if column not in df_columns_lower:
            raise ValueError(f"Required column '{column}' not found in the CSV file.")
    
    df.columns = [col.lower().strip() for col in df.columns]
    df = df[required_columns]

    df = df.reindex(sorted(df.columns), axis=1)
    df.fillna(df.mean(), inplace=True)
    
    return df


def drop_columns_if_exists(df, columns):
    for column in columns:
        if column in df.columns:
            df.drop(columns=[column], inplace=True)
    return df


def create_time_steps(data, time_step=None):
    if time_step is None:
        time_step = Config.TIME_STEP
    
    if len(data) < time_step:
        raise ValueError(f"Not enough data. Minimum number of required data: {time_step}.")
    
    X = [data[i:i + time_step] for i in range(len(data) - time_step)]
    return np.array(X)

def raise_http_exception(status_code, detail):
    raise HTTPException(status_code=status_code, detail=detail)
