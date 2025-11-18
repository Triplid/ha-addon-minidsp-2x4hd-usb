ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base-debian:bookworm
FROM $BUILD_FROM

# Labels для HA multi-arch (обязательно для 2025!)
LABEL \
    io.hass.name="MiniDSP 2x4 HD USB Control" \
    io.hass.description="USB HID control for miniDSP 2x4 HD" \
    io.hass.type="addon" \
    io.hass.version="1.1.0" \
    maintainer="Triplid"

ENV LANG C.UTF-8

# Установка зависимостей (libhidapi-hidraw0 для HID в Debian)
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        libhidapi-hidraw0 \
        libhidapi-libusb0 \
        udev && \
    rm -rf /var/lib/apt/lists/* && \
    python3 -m venv /venv && \
    . /venv/bin/activate && \
    pip install --no-cache-dir hidapi && \
    deactivate

# Копируем файлы аддона
COPY minidsp_status.py /app/minidsp_status.py
COPY services.d/ /etc/services.d/

# Делаем исполняемыми (на всякий случай)
RUN chmod +x /app/minidsp_status.py && \
    find /etc/services.d -name "run" -exec chmod +x {} \;

WORKDIR /app

# S6 overlay для services.d (стандарт HA)
CMD [ "/init" ]
