# pc_show_off
`Django` web project using an `sqlite3` database. `Dockerfile` & `docker-compose` configured for easy containerization.

Create a profile. Add hardware parts to the Components Library. Select the parts that resemble your PC configuration and show it to the community.

Each hardware component's models & views 'live' inside a dedicated `Django` app. `CRUD` operations on the hardware components are possible through the use of `forms.ModelForm` forms. The `Pc` model class has `ForeignKey` relationships with every other component.

## Project Structure
```css
app/
├── pc_show_off/
│   ├── accounts/
│   ├── case/
│   ├── common/
│   ├── cpu/
│   ├── gpu/
│   ├── mobo/
│   ├── pc/
│   ├── psu/
│   ├── ram/
│   ├── storage/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── static/
│   ├── css/
│   └── images/
├── templates/
│   ├── accounts/
│   ├── case/
│   ├── common/
│   ├── cpu/
│   ├── gpu/
│   ├── mobo/
│   ├── pc/
│   ├── psu/
│   ├── ram/
│   ├── storage/
│   └── base.html
├── .env
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── manage.py
└── requirements.py
```

## Imports & Dependencies
The project runs on Python 3.11

Requirements:
```docker
asgiref==3.7.2
Django==5.0.2
django-dotenv==1.4.2
sqlparse==0.4.4
tzdata==2024.1
```


## Build, Run & Stop the Container
```bash
docker compose build
docker compose up
docker compose down -v
```

## Execute Commands in the Container
```bash
docker compose exec web python manage.py collectstatic --noinput
docker compose exec web ls staticfiles/
docker compose run web bash

docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---
