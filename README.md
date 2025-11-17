📒 Notes API Project 

After learning the basics of Django, I wanted to explore advanced Django REST Framework features like Custom User Models, JWT Authentication, permissions, and throttling. This project is my first full API using these features.

Although it’s not fully advanced yet, it’s a solid foundation for building user-specific APIs with secure access.

This project implements:

Custom User Model (bio, age)

JWT Authentication (register, login, refresh)

Notes API (CRUD)

User-specific access with IsOwner permission

Request throttling to limit excessive usage

Fully functional admin panel

Features

User Management

Register a new user via API (/api/register/)

Login via JWT (/api/token/)

Refresh token (/api/token/refresh/)

Notes API

Create, Read, Update, Delete notes

Each user only sees their own notes

Permissions enforced: only owner can edit/delete

Throttling applied: max 60 requests/min per user, 10/min for anonymous

Admin Panel

Manage users (bio & age visible)

Manage notes

Tech Stack

Python 3.x

Django 4.x

Django REST Framework

djangorestframework-simplejwt

Installation

Clone the repository:

git clone https://github.com/banumariwan/notes_api_project.git
cd notes_api_project


Create and activate a virtual environment:

python -m venv .venv
.\.venv\Scripts\activate   # Windows
source .venv/bin/activate  # Linux/Mac


Install dependencies:

pip install -r requirements.txt


Apply migrations:

python manage.py makemigrations
python manage.py migrate


Create a superuser (for admin panel):

python manage.py createsuperuser


Run the server:

python manage.py runserver

API Endpoints
Endpoint	Method	Description
/api/register/	POST	Register a new user
/api/token/	POST	Obtain JWT token (login)
/api/token/refresh/	POST	Refresh access token
/api/notes/	GET	List all notes for the logged-in user
/api/notes/	POST	Create a new note
/api/notes/<id>/	GET	Retrieve a single note (owner only)
/api/notes/<id>/	PUT/PATCH	Update a note (owner only)
/api/notes/<id>/	DELETE	Delete a note (owner only)

Authentication: Add header:

Authorization: Bearer <access_token>

Testing Instructions

Register a user via /api/register/.

Login via /api/token/ to get JWT access & refresh tokens.

Use access token to access /api/notes/ endpoints.

Verify that users cannot access or modify other users’ notes.

Try exceeding 60 requests/min → should see 429 Too Many Requests.

Admin Panel

URL: /admin/

Manage users (CustomUser model shows bio and age)

Manage notes

Future Improvements

Add categories/tags to notes

Add search & filtering

Add Swagger/OpenAPI documentation

Add front-end client (React/Vue)

License

MIT License
