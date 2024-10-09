# Django Tree Menu App![Python](https://img.shields.io/badge/Python-3.10-blue?style=flat&logo=python)![Django](https://img.shields.io/badge/Django-5.1.1-green)![Docker](https://img.shields.io/badge/Docker-20.10-blue?style=flat&logo=docker)![Nginx Status](https://img.shields.io/badge/Nginx-active-brightgreen?logo=nginx&logoColor=white)![Gunicorn Status](https://img.shields.io/badge/Gunicorn-active-brightgreen?logo=gunicorn&logoColor=white)

## Описание проекта
Проект доступен по адресу http://uptrader.sycorax.tech/

Django Tree Menu App — это приложение для создания древовидного меню с поддержкой кастомного template tag, позволяющего отображать меню, где все элементы над активным пунктом и первый уровень вложенности под ним развёрнуты. Меню хранится в базе данных, редактируется через стандартную админку Django, и его активный пункт определяется на основе текущего URL. Поддерживается отображение нескольких меню на одной странице по названию, а каждый пункт может содержать явный или именованный URL. Для отрисовки меню выполняется только один запрос к базе данных, обеспечивая оптимизацию работы.

## Запуск проекта
### Склонируйте репозиторий:

1. ```bash
   git clone https://github.com/maksorli/menu_tree.git
   ```
2. Проверьте версию Docker и Docker Compose, либо установите:

   ```bash
   docker --version
   docker-compose --version
   ```
3. Запустите проект с помощью Docker Compose:
   ```bash
   docker-compose up --build
   ```
 