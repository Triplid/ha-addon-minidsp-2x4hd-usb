ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM} AS builder

# Пакеты для сборки Python hidapi
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    python3 \
    py3-pip \
    libusb-dev \
    eudev-dev

# Сборка Python hidapi (сам компилирует C backend hidraw)
RUN pip install --no-cache-dir hidapi

FROM ${BUILD_FROM}

RUN apk add --no-cache \
    python3 \
    libusb \
    eudev

COPY --from=builder /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
