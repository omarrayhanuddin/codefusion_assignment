```markdown
# CodeFusion Python Developer Assignment

## Overview

This Django-based application fetches country data from the [REST Countries API](https://restcountries.com/v3.1/all), stores it in a database, and provides **RESTful APIs** and a **secured web interface** to manage and display the data. It includes user authentication, a searchable and filterable country list, and a browsable API, styled with **Bootstrap 5.3.3** for a responsive design. Sensitive configuration (Django secret key and API URL) is managed securely using a `.env` file.

---

## Installation Steps

To set up and run the project locally, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/omarrayhanuddin/codefusion_assignment.git
   cd codefusion_assignment
   ```

2. **Create and Activate a Virtual Environment**:
   ```bash
   python3 -m venv venv  # On Windows: python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` File**:
   - Copy the provided `.env.example` to `.env`:
     ```bash
     cp .env.example .env
     ```
   - Edit `.env` to set the Django secret key and REST Countries API URL. Example:
     ```env
     SECRET_KEY=your-secret-key-here
     REST_COUNTRIES_API_URL=https://restcountries.com/v3.1/all
     ```
   - Generate a secure secret key using a tool like [Djecrety](https://djecrety.ir/) or Python:
     ```python
     from django.core.management.utils import get_random_secret_key
     print(get_random_secret_key())
     ```

5. **Apply Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a Superuser** (for admin access):
   ```bash
   python manage.py createsuperuser
   ```

7. **Fetch Country Data**:
   Run the custom management command to populate the database:
   ```bash
   python manage.py fetch_countries
   ```

8. **Run the Development Server**:
   ```bash
   python manage.py runserver
   ```

---

## Required Dependencies

The project uses the following dependencies, as specified in `requirements.txt`:

- **Django==5.2**: Web framework for backend development.
- **djangorestframework==3.16.0**: Toolkit for building RESTful APIs.
- **requests==2.32.3**: Library for fetching data from the REST Countries API.
- **django-filter==25.1**: Library for filtering API and web interface queries.
- **python-decouple==3.8**: Library for managing environment variables from a `.env` file.
- **Bootstrap 5.3.3**: Frontend framework for styling (loaded via CDN).

To install dependencies manually:
```bash
pip install Django==5.2 djangorestframework==3.16.0 requests==2.32.3 django-filter==25.1 python-decouple==3.8
```

---

## Database Setup and Configuration

- **Database**: SQLite (default Django database).
- **Database File**: `db.sqlite3` (created in the project root).
- **Configuration**:
  - Configured in `codefusion_assignment/settings.py`:
    ```python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    ```
  - No additional configuration is required.
- **Setup Steps**:
  - Run migrations to create the database schema:
    ```bash
    python manage.py migrate
    ```
  - Populate the database with country data:
    ```bash
    python manage.py fetch_countries
    ```

---

## Running the Application

With the server running (`python manage.py runserver`), access the application at:

- **Web Interface**: `http://localhost:8000/`
  - Displays a searchable and filterable country list.
- **RESTful API**: `http://localhost:8000/api/countries/`
  - Provides endpoints for country data management (requires authentication).
- **Admin Interface**: `http://localhost:8000/admin/`
  - Access with superuser credentials.
- **Registration**: `http://localhost:8000/register/`
  - Create a new user account.
- **Login**: `http://localhost:8000/login/`
  - Log in to access the country list and API.

### Web Interface Usage
- **Registration**: Register at `/register/`. After successful registration, you’ll be *automatically logged in* and redirected to the country list.
- **Login**: Log in at `/login/` to access the country list.
- **Country List**: View all countries at `/`. Use the search bar to filter by name or query parameters (e.g., `?region=Europe`, `?language=en`) to filter by region or language.
- **Details Buttons**: Each country row includes:
  - **Region**: Filter countries by the same region (e.g., `?region=Americas`).
  - **Languages**: Filter countries by a spoken language (e.g., `?language=fr`).
- **Logout**: Click the logout button in the navbar to end your session.

### RESTful API Usage
- **Browsable API**: Navigate to `http://localhost:8000/api/countries/` in a browser.
  - If not logged in, a login form appears in the top-right corner.
  - Log in with your username and password (from registration or superuser).
  - Interact with endpoints (list, create, update, delete, filter) via the browsable interface.
  - Log out using the “Log out” link in the top-right corner.
- **Endpoints**:
  - `GET /api/countries/`: List all countries.
  - `GET /api/countries/<id>/`: Retrieve a specific country.
  - `POST /api/countries/`: Create a new country.
  - `PUT /api/countries/<id>/` or `PATCH /api/countries/<id>/`: Update a country.
  - `DELETE /api/countries/<id>/`: Delete a country.
  - Filtering: Use query parameters (e.g., `?name=canada`, `?region=Europe`, `?language=en`).
- **Authentication**:
  - **Session Authentication**: For browsable API access in browsers.
  - **Basic Authentication**: For programmatic access (e.g., `curl -u username:password http://localhost:8000/api/countries/`).
- **Note**: Avoid sending `Accept: application/json` headers in browsers to ensure the browsable API renders correctly.

### Running Tests
Unit tests verify model and view functionality:
```bash
python manage.py test
```

---

## Project Features

- **Data Fetching**: Fetches and stores country data from the REST Countries API using a custom management command.
- **RESTful APIs**:
  - CRUD operations for country data.
  - Filtering by name (partial search), region, and language.
  - Secured with session and basic authentication.
- **Web Interface**:
  - Displays country details (name, cca2, capital, population, timezone, flag).
  - Supports searching by name and filtering by region/language.
  - Responsive design with Bootstrap 5.3.3.
- **Authentication**:
  - Uses Django’s default authentication system (`django.contrib.auth.models.User`).
  - Includes login, registration (with automatic login), and logout.
  - Restricts API and country list access to authenticated users.
- **Browsable API**: Interactive interface for API exploration with login support.
- **Environment Variables**: Manages sensitive configuration (Django secret key, API URL) via a `.env` file.
- **Unit Tests**: Tests for country model and view behavior (authentication, access control).

---

## Project Structure

- **`countries/models.py`**: Defines the `Country` model.
- **`countries/views.py`**: Handles web views (country list, registration) and API views (`CountryViewSet` with filtering).
- **`countries/serializers.py`**: Serializes country data for the API.
- **`countries/filters.py`**: Custom filter set for API and web interface filtering.
- **`countries/templates/countries/`**: HTML templates (`base.html`, `country_list.html`, `login.html`, `registration.html`).
- **`countries/management/commands/fetch_countries.py`**: Fetches and stores country data.
- **`countries/tests.py`**: Unit tests for models and views.
- **`codefusion_assignment/settings.py`**: Configures Django, DRF, and database settings.
- **`codefusion_assignment/urls.py`**: Defines URL routing.
- **`.env.example`**: Sample environment variable configuration.
- **`requirements.txt`**: Lists dependencies.

---
```