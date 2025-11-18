ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Задаём рабочую директорию
WORKDIR /app

# Устанавливаем зависимости
RUN apk add --no-cache python3 py3-pip libusb eudev \
    && apk add --no-cache --virtual .build-deps gcc musl-dev linux-headers \
    && pip install --no-cache-dir hidapi \
    && apk del .build-deps

# Копируем Python скрипт
COPY minidsp_status.py /app/minidsp_status.py

# Копируем s6 сервис
COPY services.d/ /etc/services.d/

# Делаем run исполняемым
RUN chmod +x /etc/services.d/minidsp/run

# s6-overlay автоматически стартует через PID 1
CMD ["/init"]
