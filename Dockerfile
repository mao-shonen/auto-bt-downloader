FROM python

WORKDIR /app
COPY . .

RUN apt-get update -y && apt-get install  \
        python-mysqldb && \
    pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
