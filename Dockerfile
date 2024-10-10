FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

RUN pip install gunicorn


COPY . .

RUN python manage.py collectstatic --noinput


CMD ["gunicorn", "--workers=3", "--bind=0.0.0.0:8002", "menu_tree_project.wsgi:application"]