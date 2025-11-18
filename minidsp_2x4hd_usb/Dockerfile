ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Рабочая директория
WORKDIR /app

# Системные зависимости и build deps
RUN apk add --no-cache \
        python3 \
        py3-virtualenv \
        libusb \
        eudev \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers

# Создаём виртуальное окружение и ставим hidapi
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir hidapi

# Убираем build deps
RUN apk del .build-deps

# Копируем файлы аддона
COPY minidsp_2x4hd_usb/ /app/
COPY minidsp_2x4hd_usb/services.d/ /etc/services.d/

# Делаем run исполняемым
RUN chmod +x /etc/services.d/minidsp/run

# Экспортируем venv в PATH
ENV PATH="/venv/bin:$PATH"

# CMD для s6-overlay (PID 1)
CMD [ "/init" ]
