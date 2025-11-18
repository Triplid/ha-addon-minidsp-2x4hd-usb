ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:3.22
FROM ${BUILD_FROM} AS builder

# Build-deps: hidapi-dev для компиляции (если нужно), но pip hidapi берёт из source
RUN apk add --no-cache --virtual .build-deps \
    gcc \
    musl-dev \
    linux-headers \
    python3-dev \
    py3-pip \
    hidapi-dev  # Правильный dev-пакет для aarch64

# Venv + pip (upgrade pip для стабильности)
RUN python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir hidapi  # Соберётся из source с dev-пакетом

# Финальный образ
FROM ${BUILD_FROM}

# Runtime: hidapi и libusb (из apk, не dev)
RUN apk add --no-cache \
    python3 \
    hidapi \  # Основной пакет для HID
    libusb

# Копируем venv
COPY --from=builder /venv /venv
ENV PATH="/venv/bin:$PATH"

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
