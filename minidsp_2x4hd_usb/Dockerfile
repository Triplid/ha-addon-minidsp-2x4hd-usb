# Используем Python slim image
FROM python:3.12-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y \
    libusb-1.0-0-dev \
    && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем все файлы
COPY . .

# Устанавливаем Python-библиотеки
RUN pip install --no-cache-dir hidapi

# Делаем скрипты исполняемыми
RUN chmod +x run.sh minidsp_status.py minidsp_control.py

# Запуск аддона
CMD [ "/app/run.sh" ]
