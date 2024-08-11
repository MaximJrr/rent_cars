FROM python:3.10

RUN mkdir /rent_car

WORKDIR /rent_car

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /rent_car/docker/app.sh

CMD ["gunicorn", "app.main:app", "--workers", "4", "--worker-class", "uvicorn.workers.UvicornWorker", "--bind=0.0.0.0:8000"]