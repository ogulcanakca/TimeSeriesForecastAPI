FROM python:3.12.4-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    make \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

COPY requirements/requirements_app.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


COPY app/ app/
COPY model/ model/
COPY scaler/ scaler/

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
