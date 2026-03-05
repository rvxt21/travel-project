# Travel Project Planner

A  Django REST API designed for planning travel projects.

---

## 🛠 Prerequisites

Before starting, ensure you have the following installed:
* **Python 3.12+**
* **uv** 

### 1. Clone and Environment Setup
First, clone the repository and use `uv` to create a virtual environment and install all dependencies (Django, DRF, drf-spectacular, etc.) in one command:
```bash
git clone <repo-url>
uv sync
```

### 2. Configure Environment Variables (.env)
Create a .env file in the project root and add the following configuration:
```bash
DJANGO_SETTINGS_MODULE="config.django.local"
DJANGO_DEBUG=True
SECRET_KEY="your-generated-key-here"
```
#### How to generate a secure SECRET_KEY:
```bash
uv run python -c 'from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())'
```

### 3. Database Migrations
```bash
python manage.py migrate
```

### 4. Seed Data
```bash
python manage.py populate_db
```

### 5. Start the Server
```bash
python manage.py runserver
```

### Documantation
Once the server is running, open your browser to view the interactive Swagger UI. 
👉 http://127.0.0.1:8000/api/schema/swagger-ui/

