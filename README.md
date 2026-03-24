# Ol_Utills

A lightweight Flask utility library providing validation, authentication decorators, and database helpers.

## Installation

```bash
pip install ol-utills
```

**Dependencies:** `flask`, `sqlite3`, `psycopg2`, `re`

---

## `packages.py` — API Reference

### `val` — Validation

A class with static methods for validating common user inputs using regex.

| Method | Description |
|---|---|
| `val.chk_p(password)` | Validates password strength (min 8 chars, 1 uppercase, 1 lowercase, 1 digit, 1 special char) |
| `val.chk_e(email)` | Validates email format (RFC 2822 compliant) |
| `val.chk_ph(phone)` | Validates international phone numbers |

All methods return `True` if valid, `None` otherwise.

**Example:**
```python
from packages import val

if val.chk_p("MyP@ss1234"):
    print("Password is strong")

if val.chk_e("user@example.com"):
    print("Email is valid")
```

---

### `req` — Authentication Decorators

Decorators for protecting Flask routes with session-based authentication.

#### `@req.login_required`

Restricts a route to logged-in users. Checks `session['logged'] == True`.

```python
from packages import req

@app.route('/dashboard')
@req.login_required
def dashboard():
    return "Welcome to your dashboard"
```

#### `@req.admin_required`

Restricts a route to admin users. Checks `session['admin'] == True`.

```python
@app.route('/admin')
@req.admin_required
def admin_panel():
    return "Admin Panel"
```

---

### `res` — Response Helpers

Utility class for building standardized API responses.

| Method | Description |
|---|---|
| `res.success_response(data)` | Returns a success JSON response *(not yet implemented)* |
| `res.error_response(message, code)` | Returns an error JSON response *(not yet implemented)* |

---

### `database` — Database Connection

Provides quick database connection helpers.

#### `database.sqlite(database)`

Opens a connection to a SQLite database and returns a cursor.

```python
from packages import database

db = database.sqlite("app.db")
db.execute("SELECT * FROM users")
results = db.fetchall()
```