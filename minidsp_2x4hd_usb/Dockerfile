ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16

# Builder stage для компиляции
FROM ${BUILD_FROM} AS builder
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    python3 \
    py3-pip \
    libusb-dev \
    libhidapi-dev
RUN pip install --no-cache-dir cython hidapi

# Final stage — чистый
FROM ${BUILD_FROM}
RUN apk add --no-cache \
    python3 \
    libusb-dev \
    libhidapi-dev

# Копируем установленное из builder
COPY --from=builder /usr/local/lib/python3.*/site-packages /usr/local/lib/python3.*/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
