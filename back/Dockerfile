FROM python:latest

WORKDIR /app/

COPY ./app /app/
COPY ./requirements.txt /app/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]