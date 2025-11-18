FROM ghcr.io/home-assistant/aarch64-base:latest

WORKDIR /app

RUN apk add --no-cache python3 py3-pip libusb eudev \
    && apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers \
    && pip install --break-system-packages hidapi \
    && apk del .build-deps

COPY . /app/

RUN chmod +x services.d/minidsp/run
