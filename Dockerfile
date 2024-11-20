FROM python:3.10

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

COPY requirements.txt .

RUN apt-get update && apt-get install -y libzbar0

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh