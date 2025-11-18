ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16
FROM ${BUILD_FROM}

# Установка зависимостей для Python и HID
RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb-dev \
    libhidapi-dev \
    gcc \
    musl-dev \
    linux-headers

# Установка Python пакетов
RUN pip install --no-cache-dir cython hidapi

# Рабочая директория
WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

# Запуск
CMD ["./run.sh"]
