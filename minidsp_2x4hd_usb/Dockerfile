ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Рабочая директория
WORKDIR /app

# Устанавливаем системные зависимости и сборочные deps
RUN apk add --no-cache \
        python3 \
        py3-virtualenv \
        libusb \
        eudev \
    && apk add --no-cache --virtual .build-deps \
        gcc \
        musl-dev \
        linux-headers

# Создаём виртуальное окружение и ставим hidapi в venv (PEP 668-safe)
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install --no-cache-dir hidapi

# Убираем build deps
RUN apk del .build-deps

# Копируем содержимое аддона (скрипты, services.d и прочее)
COPY minidsp_2x4hd_usb/ /app/

# Копируем services в каталог s6
COPY minidsp_2x4hd_usb/services.d/ /etc/services.d/

# Убеждаемся, что скрипт исполняемый
RUN chmod +x /etc/services.d/minidsp/run

# Экспортим venv в PATH, чтобы /init и s6-сервис видели правильный python
ENV PATH="/venv/bin:$PATH"

# s6-overlay должен быть PID 1 — CMD /init
CMD [ "/init" ]
