# Используем официальный Python образ
FROM python:3.12

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем файл requirements.txt
COPY ./requirements.txt /app/


# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы проекта
COPY . /app/

# Открываем порт для контейнера
EXPOSE 8000

# Запускаем приложение
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
