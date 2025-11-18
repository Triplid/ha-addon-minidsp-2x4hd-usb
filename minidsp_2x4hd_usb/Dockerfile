ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Установка зависимостей
RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb \
    eudev \
    eudev-dev \
    gcc \
    musl-dev \
    linux-headers

# Копируем скрипт
COPY minidsp_status.py /usr/src/app/minidsp_status.py

# Создаём виртуальное окружение для Python и ставим hidapi
RUN python3 -m venv /usr/src/app/venv && \
    /usr/src/app/venv/bin/pip install --no-cache-dir hidapi

# Копируем s6 сервис
COPY services.d/ /etc/services.d/

# Правильный CMD для s6
CMD ["/init"]
