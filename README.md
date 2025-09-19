# pc_show_off
`Django` web project using an `sqlite3` database. `Dockerfile` & `docker-compose` configured for easy containerization.

Create a profile. Add hardware parts to the Components Library. Select the parts that resemble your PC configuration and show it to the community.

<img width="1919" height="417" alt="Screenshot from 2025-09-19 16-15-02" src="https://github.com/user-attachments/assets/f6796b18-8d73-4275-aead-d783f30ce8b0" />

Each hardware component's models & views 'live' inside a dedicated `Django` app. `CRUD` operations on the hardware component objects are possible through the use of `forms.ModelForm` forms. The `Pc` model class has `ForeignKey` relationships with every other component.

<img width="1919" height="463" alt="Screenshot from 2025-09-19 16-07-45" src="https://github.com/user-attachments/assets/a76774dd-a825-4bb6-bb5a-ba4a3f05af36" />

If a regular user creates a new PC component, the data needs to be checked and verified against the manufacturer's product specification by a staff/superuser person. Until verified, the item will be displayed under the `Entries Under Review` section of the list view for the relevant PC component. By default, PC component creation forms submitted by staff/superusers get automatically verified. 

<img width="1919" height="383" alt="Screenshot from 2025-09-19 16-09-55" src="https://github.com/user-attachments/assets/cda67012-ffa3-48db-8f5c-31998e6875c3" />

----

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
docker compose run web bash # Starts a new container based on the web service
docker exec -it <NAMES> bash # Attaches to an already running container named web
>>> python manage.py shell

docker compose exec web python manage.py migrate
docker compose exec web python manage.py createsuperuser
```

---
