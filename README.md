# Time Series Forecast API for Amazon Stock Prices

This repository includes models that predict Amazon's stock prices using machine learning techniques and Docker integration with the REST API built with the best model.

## Overview

The aim of this project is to develop a model that can accurately predict Amazon's future stock prices. We analyzed stock data and used various models.

| Model                      | MAE       | MAPE     | R²        |
|----------------------------|-----------|----------|-----------|
| SARIMA                     | 363.234   | 17.413   | \-0.972   |
| Random Forest Regressor    | 0.547     | 0.155    | 0.999     |
| Prophet                    | 737.702   | 46.620   | \-1.305   |
| LSTM                       | 79.921    | 5.576    | 0.969     |
| LSTM-CNN-Raw Data          | 92.710    | 5.836    | 0.951     |
| CNN-LSTM-Processing Data   | 0.074     | 71.747   | 0.945     |

Based on the evaluation metrics, the best model LSTM-CNN-Raw Data was selected, tested and saved in the model folder as model.keras. If needed, the desired model can be tested with notebook.ipynb in the notebook folder, taking into account the model input specifications in Report.pdf.

The dataset to be given as input to the LSTM-CNN-Raw Data model must contain the columns in the Table 1. Columns other than these will be dropped.

| Features |
|----------|
| Open     |
| High     |
| Low      |
| Volume   |

*Table 1: List of features used in the model.*

## Installation & Initialization 

### Installation to run notebook

* Check that you are in the `TimeSeriesForecastAPI` directory.
1. Clone the repository: `git clone https://github.com/ogulcanakca/TimeSeriesForecastAPI.git` 
2. Create a Python virtual environment: `python -m venv .venv` 
3. Activate the created python virtual environment: `.venv\Scripts\activate`
4. Install the require dependecies for notebook: `pip install -r ./requirements/requirements_notebook.txt`

### Installation and running the app with Docker Cli

1. Pull the image: `docker pull ogulcanakca/stock-prediction-app:latest`
2. Create the container: `docker run -it --name stock-prediction-app-container -p 8000:8000 --entrypoint /bin/bash ogulcanakca/stock-prediction-app:latest`
3. Start the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

or

1. Clone the repository: `git clone https://github.com/ogulcanakca/TimeSeriesForecastAPI.git`
2. Create the image: `docker build --no-cache -t ogulcanakca/stock-prediction-app:latest .`
3. Create the container: `docker run -it --name stock-prediction-app-container -p 8000:8000 --entrypoint /bin/bash ogulcanakca/stock-prediction-app:latest`
4. Start the application: `uvicorn app.main:app --host 0.0.0.0 --port 8000`

### Installation and running the app with Docker Compose

* Check that you are in the `TimeSeriesForecastAPI` directory.
1. Clone the repository: `git clone https://github.com/ogulcanakca/TimeSeriesForecastAPI.git`
2. Create the image: `docker build --no-cache -t ogulcanakca/stock-prediction-app:latest .`
3. Create the container: `docker-compose up`

### Installation and running the app without Docker

* Check that you are in the `TimeSeriesForecastAPI` directory.
1. Clone the repository: `git clone https://github.com/ogulcanakca/TimeSeriesForecastAPI.git`
2. Create a Python virtual environment: `python -m venv .venv` 
3. Activate the created python virtual environment: `.venv\Scripts\activate`
4. Install the require dependecies for app: `pip install -r ./requirements/requirements_app.txt`
5. Start the application: `python -m app.main`

## Usage

* Using API client applications such as Postman, cURL or command line tools such as CMD, Powershell, we can interact with the API by sending the dataset required for the model to make predictions to the /predict endpoint via HTTP POST request.
* After completing **installation and running the app** styles without any problems, send an HTTP POST request to `http://0.0.0.0:8000/predict/` endpoint **(the endpoint where the model will make predictions)** with data that meets the following conditions that the model will predict.
  * Provided that it is in .csv format.
  * Provided that there are at least 60 lines. **(Since a 60-day window is applied to the data on which the model is trained)**
  * Must include the columns in Table 1.
  * As needed, 3 .csv data set samples in the `TimeSeriesForecastAPI/data` folder were created with the ChatGPT 4o model. If available, if an HTTP POST request can be sent to the API so that the model can predict with the available dataset or the created dataset, it is expected to return a response like the following after processing the data sent to the API.

```json
{
    "predictions": [
        742.9829571564755,
        479.46198545826877,
        880.5189730546189,
        723.0954146860538,
        908.9192076988778,
        858.07631696814,
        607.9550592389352,
                .
                .
                .
        916.7704339205503,
        730.5222026382331,
        700.8287300864888,
        859.3897162892129,
        732.8567322777363,
        919.8326809658504
    ]
}
```

## Contributing

Contributions are welcome! If you have any suggestions or improvements, please open an issue or submit a pull request.

## License

This project is licensed under the CC0-1.0 License. See the [LICENSE](LICENSE) file for more details.
