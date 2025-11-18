ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM} AS builder

# Сборка пакетов
RUN apk add --no-cache --virtual .build-deps \
    gcc musl-dev linux-headers python3 py3-pip libusb-dev eudev-dev

# Создаем виртуальное окружение
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Устанавливаем hidapi в venv
RUN pip install --no-cache-dir hidapi

FROM ${BUILD_FROM}

# Runtime библиотеки
RUN apk add --no-cache python3 libusb eudev

# Копируем venv
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
