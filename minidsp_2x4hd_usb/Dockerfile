# Stage 1: base
FROM ghcr.io/home-assistant/aarch64-base:latest

# Установка зависимостей для сборки
RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb \
    eudev \
    gcc \
    musl-dev \
    linux-headers \
    libusb-dev \
    eudev-dev \
    git \
    && python3 -m venv /venv \
    && /venv/bin/pip install --upgrade pip \
    && /venv/bin/pip install hidapi flask

# Копируем код приложения
COPY app /app
WORKDIR /app

# Указываем окружение venv
ENV PATH="/venv/bin:$PATH"

# Экспонируем порт для REST
EXPOSE 5000

# Запуск приложения
CMD ["python", "main.py"]
