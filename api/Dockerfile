FROM python:3.7

WORKDIR /app
COPY ./api/requirements.txt /app/requirements.txt

RUN pip install -r /app/requirements.txt
CMD ["python","-m","http.server","8082"]