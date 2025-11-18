ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16
FROM $BUILD_FROM

# Установка зависимостей
RUN apk add --no-cache python3 py3-pip libusb-dev gcc musl-dev linux-headers
RUN pip install --no-cache-dir hidapi cython

# Копируем скрипт
WORKDIR /app
COPY minidsp_status.py ./
RUN chmod +x /app/minidsp_status.py

# Запуск
CMD [ "python3", "/app/minidsp_status.py" ]