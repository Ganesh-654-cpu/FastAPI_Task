# FastAPI Learning Journey 🚀

This repository contains hands-on FastAPI code snippets covering core to advanced concepts — built step by step while learning backend development with Python.

## 📌 Topics Covered

### 1. Basic Routes
Simple `GET` routes to understand FastAPI basics — home route, about page, and returning JSON responses.

### 2. Path Parameters
Fetching dynamic data from the URL using path parameters (e.g. `/users/{user_id}`).

### 3. Query Parameters
Handling optional and default query parameters (e.g. `/products?limit=10`).

### 4. Request Body with Pydantic
Using `pydantic.BaseModel` to validate incoming JSON data via `POST` requests.

### 5. Nested Pydantic Models
Handling nested objects inside a request body (e.g. `User` containing an `Address` model).

### 6. CRUD API (In-Memory)
A simple Todo application supporting `Create`, `Read`, `Update`, and `Delete` operations using an in-memory list.

### 7. PUT Requests with Query Params
Updating existing records while also accepting extra query parameters like `notify`.

### 8. Response Model
Using `response_model` to control and hide sensitive fields (like passwords) from API responses.

### 9. Status Codes & HTTPException
Returning proper HTTP status codes and raising custom exceptions like `404 Not Found`.

### 10. Custom Exception Handling
Creating custom exception classes and handling them globally using `@app.exception_handler`.

### 11. Dependency Injection
Using `Depends()` for reusable logic — authentication checks, common logic, and fetching the current user.

### 12. Middleware
Logging request processing time and tracking request/response flow using custom middleware.

### 13. Database Integration — SQLite
Connecting FastAPI with a raw SQLite database using the `sqlite3` module.

### 14. Database Integration — SQLAlchemy ORM
Full CRUD operations on a Todo model using SQLAlchemy ORM with session-based database access.

### 15. Async APIs
Writing asynchronous routes using `async def` and `asyncio.sleep()` to simulate non-blocking tasks.

### 16. JWT Authentication
Implementing token-based authentication using `python-jose`, including token creation and verification.

### 17. JWT Authentication with Login (OAuth2 + Password Hashing)
Complete authentication flow with `OAuth2PasswordBearer`, password hashing using `passlib` (bcrypt), login API, and protected routes.

### 18. File Upload API
Uploading files to the server, storing them in an `uploads/` folder, and serving them as static files.

### 19. CORS Handling
Enabling Cross-Origin Resource Sharing so a frontend (e.g. React/Vite app on `localhost:5173`) can communicate with the FastAPI backend.

### 20. Consuming External APIs
Making outbound HTTP requests using the `requests` library to fetch data from a public API (`jsonplaceholder`).

### 21. Web Scraping with BeautifulSoup
Scraping live data (Hacker News headlines) using `requests` + `BeautifulSoup`.

### 22. Caching
Implementing simple time-based caching to avoid repeated scraping/API calls within a short interval.

### 23. Rate Limited API
Using `slowapi` to limit the number of requests a client can make (e.g. `5 requests/minute`), along with a custom `429 Too Many Requests` error handler.

---

## 🛠️ Tech Stack
- **Framework:** FastAPI
- **Validation:** Pydantic
- **Database:** SQLite, SQLAlchemy
- **Auth:** JWT (python-jose), Passlib (bcrypt)
- **Rate Limiting:** SlowAPI
- **Web Scraping:** BeautifulSoup4, Requests

## ▶️ Running the Project

```bash
pip install fastapi uvicorn sqlalchemy python-jose passlib bcrypt slowapi beautifulsoup4 requests

uvicorn main:app --reload
```

Visit interactive API docs at:
```
http://127.0.0.1:8000/docs
```

---

## 👤 Author
**Ganesh Mahajan**
Software Developer Intern | Python Full-Stack Developer
