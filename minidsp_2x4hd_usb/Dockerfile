ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16
FROM ${BUILD_FROM}

# Build-stage deps
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers

RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb-dev \
    libhidapi-dev

# Установка с компиляцией, но чистим после
RUN pip install --no-cache-dir cython hidapi \
    && apk del .build-deps

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
