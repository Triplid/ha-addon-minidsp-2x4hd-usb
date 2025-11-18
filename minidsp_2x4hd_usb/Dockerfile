ARG BUILD_FROM=ghcr.io/hassio-addons/base:3.16
FROM ${BUILD_FROM}

# Только runtime-зависимости (без build-tools)
RUN apk add --no-cache \
    python3 \
    py3-pip \
    libusb-dev \
    libhidapi-dev  # Для HID runtime

# Установка без компиляции (wheels only)
RUN pip install --no-cache-dir --only-binary=all hidapi cython

WORKDIR /app
COPY run.sh minidsp_status.py ./
RUN chmod +x run.sh minidsp_status.py

CMD ["./run.sh"]
