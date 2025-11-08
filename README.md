Для другого человека Он клонирует проект:
bash

git clone <ссылка_на_репозиторий> И дальше:

Создаёт виртуальное окружение: bash

python -m venv venv Активирует его: bash

Windows
venv\Scripts\activate

#После этого pip install -r requirements.txt Запускает миграции и сервер: bash

python manage.py migrate python manage.py runserver
