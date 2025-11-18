ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16
FROM ${BUILD_FROM}

RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb-dev \
    gcc \
    musl-dev \
    linux-headers

RUN pip install --no-cache-dir cython hidapi

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
