# Используем базовый образ Home Assistant для aarch64
FROM ghcr.io/home-assistant/aarch64-base:latest

# Рабочая директория
WORKDIR /app

# Устанавливаем системные зависимости
RUN apk add --no-cache python3 py3-virtualenv libusb eudev \
    && apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers

# Создаем виртуальное окружение и ставим Python пакеты
RUN python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install hidapi

# Убираем сборочные зависимости
RUN apk del .build-deps

# Добавляем скрипты addon
COPY minidsp_2x4hd_usb/ /app/

# Делаем run скрипт исполняемым (на случай, если права слетят)
RUN chmod +x /app/services.d/minidsp/run

# Устанавливаем путь к виртуальному окружению в PATH
ENV PATH="/venv/bin:$PATH"

# Стандартная точка входа
CMD ["/app/services.d/minidsp/run"]
