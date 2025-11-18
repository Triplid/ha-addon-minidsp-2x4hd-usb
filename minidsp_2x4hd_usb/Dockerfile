# Базовый образ Home Assistant для aarch64
ARG BUILD_FROM=ghcr.io/home-assistant/aarch64-base:latest
FROM ${BUILD_FROM}

# Метаданные
ARG BUILD_DATE
ARG BUILD_VERSION
LABEL maintainer="Твой Email или GitHub" \
      org.label-schema.build-date=$BUILD_DATE \
      org.label-schema.version=$BUILD_VERSION \
      org.label-schema.vcs-url="https://github.com/твой_репозиторий" \
      org.label-schema.vcs-ref=$BUILD_VERSION \
      org.label-schema.license="MIT" \
      org.label-schema.name="MiniDSP 2x4HD USB"

# Установка зависимостей Python и USB
RUN apk add --no-cache \
    python3 \
    py3-hidapi \
    libusb \
    eudev

# Копируем файлы аддона
WORKDIR /usr/src/app
COPY run.sh .

# Скрипт запуска делаем исполняемым
RUN chmod a+x run.sh

# Порт (если нужен)
EXPOSE 5000

# Точка входа
CMD [ "/usr/src/app/run.sh" ]
