# Используем Python slim image
FROM python:3.12-slim

# Устанавливаем зависимости
RUN apt-get update && apt-get install -y libusb-1.0-0-dev && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем все файлы
COPY minidsp_status.py run.sh ./

# Устанавливаем Python-библиотеки
RUN pip install --no-cache-dir hidapi

# Делаем скрипт запуска исполняемым
RUN chmod +x run.sh minidsp_status.py

# Запуск аддона
CMD [ "/app/run.sh" ]
