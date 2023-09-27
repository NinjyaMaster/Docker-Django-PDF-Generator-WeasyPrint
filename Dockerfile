FROM python:3.10-bullseye

LABEL maintainer="Mia"

ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

RUN apt-get update && apt-get install -y \
    build-essential \
    libffi-dev \
    postgresql-client \
    libjpeg-dev \
    zlib1g-dev \
    libheif-dev \
    libx265-dev \
    git \
    # for WeasyPrint
    libpangoft2-1.0-0 \
    libharfbuzz0b \
    libpango-1.0-0 && \
    # end for WeasyPrint
    python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install --upgrade cffi &&\
    /py/bin/pip install -r /tmp/requirements.txt &&\
    rm -rf /tmp && \
    useradd --system --no-create-home django-user && \
    mkdir -p /vol/web/media && \
    mkdir -p /vol/web/static && \
    chown -R django-user:django-user /vol && \
    chmod -R 755 /vol && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV PATH="/py/bin:$PATH"

USER django-user