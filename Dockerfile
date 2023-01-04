FROM python:3.9

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /usr/src/app

EXPOSE 8000

ENTRYPOINT ["sh","./docker-entrypoint.sh"]