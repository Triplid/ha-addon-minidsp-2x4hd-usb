ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base-debian:bookworm
FROM $BUILD_FROM

ENV LANG C.UTF-8

# Устанавливаем зависимости
RUN apt-get update && \
    apt-get install -y \
        python3 \
        python3-pip \
        python3-venv \
        libhidapi-libusb0 \
        libglib2.0-0 && \
    rm -rf /var/lib/apt/lists/*

# Создаём venv
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Ставим pyhidapi
RUN pip3 install --no-cache-dir hid==1.0.6

COPY minidsp_status.py /app/
COPY services.d/ /etc/services.d/

WORKDIR /app

CMD [ "/init" ]
