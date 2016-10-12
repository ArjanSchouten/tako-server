FROM python:2.7-alpine

RUN mkdir -p /usr/app
WORKDIR /usr/src/app

COPY . /usr/src/app

RUN apk add --no-cache -X http://dl-cdn.alpinelinux.org/alpine/edge/main py-psycopg2 && \
    pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python"]
CMD ["app.py"]

EXPOSE 8888