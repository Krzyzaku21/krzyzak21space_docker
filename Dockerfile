FROM python:3.9-alpine3.13
LABEL maintainer="krzyzak21.pl"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt /requirements.txt
COPY ./app /app
COPY ./scripts /scripts

WORKDIR /app
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    apk add --update --no-cache postgresql-client && \
    apk add --update --no-cache --virtual .tmp-deps \
    build-base postgresql-dev musl-dev linux-headers && \
    apk add jpeg-dev zlib-dev libjpeg && \
    /py/bin/pip install Pillow && \
    /py/bin/pip install -r /requirements.txt && \
    apk del .tmp-deps && \
    adduser --disabled-password --no-create-home --gecos "" appuser && \
    mkdir -p /app/static && \
    mkdir -p /app/mediafiles && \
    chown -R appuser:appuser /app && \
    chmod -R 755 /app && \
    chmod -R +x /scripts

ENV PATH="/scripts:/py/bin:$PATH"

USER appuser

CMD ["run.sh"]