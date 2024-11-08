FROM python:3.11

# Установите рабочую директорию
WORKDIR /app

# Установите Poetry
RUN pip install poetry

# Копируйте файлы проекта
COPY pyproject.toml poetry.lock* /app/

# Установите зависимости
RUN poetry install 

# Копируйте остальную часть проекта
COPY . /app/

# Команда для запуска приложения
CMD ["poetry", "run", "python", "manage.py", "runserver", "0.0.0.0:8000"]