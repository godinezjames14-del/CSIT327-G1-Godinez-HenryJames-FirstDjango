# CampusConnect

- **Name:** Henry James M. Godinez
- **Section:** G1

CampusConnect is a Django web application with account registration and login, user profiles, a member dashboard, and an admin panel restricted to administrators. It uses SQLite for its local database.

## Requirements

- Python
- pip

## Run the project

From the project directory, open PowerShell and run:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Open <http://127.0.0.1:8000/> in your browser. Create an account at <http://127.0.0.1:8000/accounts/signup/> and then log in to access the dashboard. To access Django's administration site, first create a superuser with `python manage.py createsuperuser`, then visit <http://127.0.0.1:8000/admin/>.
