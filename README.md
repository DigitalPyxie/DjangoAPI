# TO DO List REST API (Django)

## Description:
This is a simple To Do list REST API built using Python and the Django REST Framework with basic CRUD functionality where a user is able to create a task, view all tasks or one, update tasks and delete a task from the list.

## Tech Stack
- Python
- Django
- Docker
- Postman
- Django REST Framework

## API Endpoints

### Get All Tasks on TO DO List
GET /api/tasks/

### Add new task to TO DO List
POST /api/tasks/

### View one task 
GET /api/tasks/<id>/

### Edit task information
PUT /api/tasks/<id>/

### Delete task from TO DO List
DELETE /api/tasks/<id>/

## Task Model Fields
- title (string)
- description (string)
- is_completed (boolean)
- created_at (timestamp)
- updated_at (timestamp)

## Installation

git clone https://github.com/DigitalPyxie/DjangoAPI.git
pip install -r requirements.txt

python manage.py migrate
python manage.py runserver