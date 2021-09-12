1. Dowload keycloak https://github.com/keycloak/keycloak/releases/download/15.0.2/keycloak-15.0.2.zip
2. Start keycloak:\
win - `bin/standalone.bat`\
linux - `bin/standalone.sh`
3. Create admin account - https://www.keycloak.org/docs/latest/getting_started/#creating-the-admin-account
4. Create realm and user - https://www.keycloak.org/docs/latest/getting_started/#creating-a-realm-and-a-user <br/>
Realm name - `demo`
5. Create client - https://www.keycloak.org/docs/latest/server_admin/#_oidc_clients
5.1 <br/>
Client ID - `django` <br/>
Client Protocol - `openid-connect` <br/>
Root URL - blank <br/>
5.2 Client Settings Valid Redirect URIs - http://127.0.0.1:8000/*
5.3 Copy Secret from Credential tab
![alt text](https://github.com/dementevm/django-allauth/blob/main/readme%20screenshots/secret.jpg?raw=true)
6. Download project - git clone https://github.com/dementevm/django-allauth.git
7. Create venv - `py -m venv venv`
8. Activate venv:\
win - `venv\Scrits\activate`\
linux - `source venv/bin/activate`
9. Install requirements - `pip install -r requirements.txt`
10. Make migrations - `py manage.py migrate`
11. Create superuser - `py manage.py createsuperuser`
12. Log in to admin console and add site
![alt text](https://github.com/dementevm/django-allauth/blob/main/readme%20screenshots/site.jpg?raw=true)
Domain name: - http://localhost:8080/auth/ <br/>
Display name: - http://localhost:8080/auth/
13. Add social app: `http://127.0.0.1:8000/admin/`
![alt text](https://github.com/dementevm/django-allauth/blob/main/readme%20screenshots/social%20app.jpg?raw=true)
Provider - `Keycloak` <br/>
Name - `test` <br/>
Client id - `django` <br/>
Secret key - From 5.3 <br/>
Key - `blank` <br/>
Sites - `http://localhost:8080/auth/`
14. Run server - `py manage.py runserver`
