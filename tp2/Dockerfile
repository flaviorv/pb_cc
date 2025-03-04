FROM ubuntu:latest

WORKDIR /app

COPY . /app

VOLUME data

RUN mkdir -p /data/charts /data/images/blurred /data/images/embossed

RUN apt-get update && apt-get install -y \
    python3 \
    python3-venv \
    gcc

RUN python3 -m venv ve 
RUN . ve/bin/activate && apt-get install -y python3-pip && pip install \
    numpy \
    aiohttp \
    aiofiles \
    matplotlib \
    requests \
    Cython \
    Faker
