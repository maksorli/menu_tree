# Используем официальный Python-образ
FROM python:3.10-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Копируем requirements и устанавливаем зависимости
COPY requirements.txt .
RUN pip install -r requirements.txt

# Установка gunicorn
RUN pip install gunicorn

# Копируем исходный код приложения
COPY . .

# Команда для запуска gunicorn
CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8002", "menu_tree_project.wsgi:application"]