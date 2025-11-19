#!/usr/bin/with-contenv bashio

# Получаем настройки из конфигурации
UPDATE_INTERVAL=$(bashio::config 'update_interval')

# Запуск основного скрипта Python с параметрами
exec python3 /app/minidsp_status.py --interval ${UPDATE_INTERVAL}
