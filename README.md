# Back-End Developer Capstone Project
Django-developed Back-End application connected to MySQL for sustainability. Implemented APIs for Menu, Menu Items, and Table Reservations.

### API endpoints:
- restaurant/menu
- restaurant/booking/tables

### Cloning the repository:
1. Clone the repository (via HTTPS)
```bash
git clone https://github.com/cabaraj/LittleLemon.git
```
2. Create/activate a virtual environment
```python
pipenv shell
```
3. Install dependencies
```python
pipenv install
```
4. If it is the first time running the program, you must apply migrations to create the models into your database
```python
python manage.py makemigrations
python manage.py migrate
```
5. Run the server
```python
python manage.py runserver
```

If want to create an admin user:
```python
python manage.py createsuperuser
```
use the '/admin' endpoint to access to the admin portal

NOTE: if plan to clone this repository, keep in mind to modify the database configurations to the appropriate ones based on your DataBase credentials. The database connects to a local database. Thus, the program will not have any data stored in it!
