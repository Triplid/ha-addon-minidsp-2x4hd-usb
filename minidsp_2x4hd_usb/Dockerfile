# Базовый образ Home Assistant для aarch64
FROM ghcr.io/home-assistant/aarch64-base:latest

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

# Копируем скрипт запуска
COPY run.sh /usr/src/app/run.sh
RUN chmod a+x /usr/src/app/run.sh

# Установка Python библиотеки hidapi в виртуальной среде
RUN python3 -m venv /usr/src/app/venv && \
    /usr/src/app/venv/bin/pip install --no-cache-dir hidapi

# CMD обязательно /init для s6-overlay
CMD ["/init"]
