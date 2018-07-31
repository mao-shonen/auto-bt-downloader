FROM python

WORKDIR /usr/src/app
COPY . .

RUN apt-get update -y && pip install --no-cache-dir -r requirements.txt

CMD ["python", "./main.py"]
