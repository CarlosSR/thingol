FROM python:3.10-slim

WORKDIR /thingol

COPY ./app/requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY ./ ./

ENV FLASK_APP=app/src/main.py
ENV FLASK_DEBUG=1

CMD ["cd","app"]
CMD ["cd","src"]
CMD ["python3","-B","-m","flask","run","--host=0.0.0.0"]