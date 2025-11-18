ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:3.22
FROM ${BUILD_FROM}

# Runtime пакеты (hidapi из apk для aarch64)
RUN apk add --no-cache \
    python3 \
    hidapi \
    libusb

# Рабочая директория
WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
