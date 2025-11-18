ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-addon-base:latest
FROM ${BUILD_FROM}

# Рабочая директория
WORKDIR /app

# Устанавливаем системные зависимости
RUN apk add --no-cache \
        python3 \
        py3-virtualenv \
        libusb \
        eudev \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers

# Создаём виртуальное окружение
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir hidapi

# Удаляем сборочные пакеты
RUN apk del .build-deps

# Копируем всё содержимое аддона
COPY . /app/

# Копируем службу s6
COPY services.d/ /etc/services.d/

# Даем права на run
RUN chmod +x /etc/services.d/minidsp
