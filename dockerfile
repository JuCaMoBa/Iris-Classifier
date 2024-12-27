FROM python:3.12

WORKDIR /api-iris

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt 

COPY . .

CMD uvicorn app.main:app --host 0.0.0.0 --port 5000