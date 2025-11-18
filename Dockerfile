ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Рабочая директория
WORKDIR /app

# Устанавливаем Python + зависимости + virtualenv
RUN apk add --no-cache \
        python3 \
        py3-virtualenv \
        libusb \
        eudev \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers \
    && python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install hidapi \
    && apk del .build-deps

# Копируем директорию аддона
COPY minidsp_2x4hd_usb/ /app/

# Страхуемся: делаем run исполняемым
RUN chmod +x /app/services.d/minidsp/run

# Разрешаем s6 запускать сервисы
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2

# Указываем правильный сервисный каталог
COPY minidsp_2x4hd_usb/services.d/ /etc/services.d/

# Запускаем s6
CMD [ "/init" ]
