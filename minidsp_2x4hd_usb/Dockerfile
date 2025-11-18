# Используем Python slim image
FROM python:3.12-slim

# Создаем рабочую директорию
WORKDIR /app

# Копируем все файлы
COPY minidsp_status.py ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir hidapi

# Делаем скрипт исполняемым
RUN chmod +x minidsp_status.py

# Запуск скрипта
CMD [ "python3", "/app/minidsp_status.py" ]
