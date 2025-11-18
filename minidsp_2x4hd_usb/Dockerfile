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

# Копируем скрипт запуска
COPY run.sh /usr/src/app/run.sh
RUN chmod a+x /usr/src/app/run.sh

# Установка hidapi в виртуальной среде
RUN python3 -m venv /usr/src/app/venv && \
    /usr/src/app/venv/bin/pip install --no-cache-dir hidapi

# Устанавливаем s6-overlay как PID 1
# В HA add-on CMD должен быть только /init
CMD [ "/init" ]
