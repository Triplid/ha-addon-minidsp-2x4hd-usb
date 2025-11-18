# Используем официальный базовый образ HA (не hassio-addons/base — он для x86/amd64)
ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:3.22
FROM ${BUILD_FROM} AS builder

# Устанавливаем только то, что реально есть в Alpine aarch64
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    python3-dev \
    py3-pip \
    libusb-dev

# Создаём venv и ставим hidapi (он соберётся из исходников, т.к. wheels нет под aarch64)
RUN python3 -m venv /venv && \
    /venv/bin/pip install --no-cache-dir --upgrade pip && \
    /venv/bin/pip install --no-cache-dir hidapi

# Финальный образ — чистый
FROM ${BUILD_FROM}

# Runtime-зависимости (только libusb — hidapi тянет его сам)
RUN apk add --no-cache python3 libusb

# Копируем готовый venv
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

# Копируем скрипты
WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
