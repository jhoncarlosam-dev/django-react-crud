# Task API

## Overview

Task API is a Django-based REST API that allows users to manage tasks efficiently.
The project uses Django REST Framework (DRF) for API development and `drf-spectacular` for OpenAPI schema generation and API documentation.

## Author
**Jhon Carlos Acevedo Mendoza**

## Features
- Create, retrieve, update and delete tasks.
- API documentation using Swagger and Redoc.
- OpenAPI schema generation for better integration with external tools.

## Project Structure
```
project_root/     
|
|-- task/          # Task app containing views, models and urls
|   |-- urls.py    # URL routing for task-related endpoints
|
|-- project_root/  # Root app containing settings and main urls
|   |-- urls.py    # Entry points for project routing
|
|-- manage.py      # Django management script
```

## Prerequisites
- Python 3.12+
- Django 5.1+
- Django REST Framework (DRF) 3.13+
- `drf-spectacular`

## Installation
1. Clone the repository:
```
git clone <repository_url>
cd project_root
```
2. Create a virtual environment and activate it:
```
python -m venv env
source env/bin/activate # On Windows: env\Scripts\activate
```
3. Install the required dependencies:
```
pip install -r requirements.txt
```
4. Apply migrations:
```
python manage.py migrate
```
5. Run the development server:
```
python manage.py runserver
```

## API Endpoints
### Base URL
```
http://127.0.0.1:8080/task/
```
### Endpoints
| Endpoint | Method | Description |
| --- | --- | --- |
| `/api/v1/task` | GET | Retrieve all tasks |
| `/api/v1/task` | POST | Create a new task |
| `/api/v1/task/{id}/` | GET | Retrieve a task by ID |
| `/api/v1/task/{id}/` | PUT | Update a task by ID |
| `/api/v1/task/{id}/` | DELETE | Delete a task by ID |
| `schema/` | GET | OpenAPI schema |
| `/docs/swagger/` | GET | Swagger UI documentation |
| `/docs/redoc/` | GET | Redoc UI documentation

## API Documentation
### Swagger UI
Accessible at:
```
http://127.0.0.1:8000/task/docs/swagger/
```
### Redoc
Accessible at:
```
http://127.0.0.1:8000/task/docs/redoc/
```

## Contributing
Feel free to contribute to this project by submitting pull requests or issues.

## License
This project is open-source and available under the MIT License.

---

Developed by **Jhon Carlos Acevedo Mendoza**