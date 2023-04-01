FROM python:3.10-slim

WORKDIR /app

COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./app/src ./

ENV FLASK_APP=app/main.py

CMD ["python3","-B","-m","flask","run","--host=0.0.0.0"]