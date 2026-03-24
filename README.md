<p align="center">
  <h1 align="center">🛠️ Ol_Utills</h1>
  <p align="center">
    A lightweight Flask utility library for validation, authentication, and database helpers.
  </p>
</p>

<p align="center">
  <a href="https://pypi.org/project/ol-utills/">
    <img src="https://img.shields.io/pypi/v/ol-utills?color=blue&label=PyPI" alt="PyPI Version">
  </a>
  <a href="https://pypi.org/project/ol-utills/">
    <img src="https://img.shields.io/pypi/pyversions/ol-utills" alt="Python Versions">
  </a>
  <a href="https://github.com/OverLimit-OL/Ol_Utills/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/OverLimit-OL/Ol_Utills" alt="License">
  </a>
</p>

---

## ✨ Features

- **Input Validation** — Password, email, and phone number validation using battle-tested regex patterns.
- **Auth Decorators** — Drop-in `@login_required` and `@admin_required` decorators for Flask routes.
- **Database Helpers** — Quick-connect utilities for **SQLite** and **PostgreSQL**.
- **Zero Config** — Works out of the box with any Flask app.

---

## 📦 Installation

```bash
pip install ol-utills
```

### Requirements

| Dependency | Purpose |
|---|---|
| `flask` | Session management & JSON responses |
| `psycopg2` | PostgreSQL connectivity |

> **Note:** `sqlite3` and `re` are part of the Python standard library.

---

## 🚀 Quick Start

```python
from Ol_Utills import val, req, database

# Validate an email
if val.chk_e("user@example.com"):
    print("Valid email!")

# Connect to a SQLite database
db = database.sqlite("app.db")
db.execute("SELECT * FROM users")
```

---

## 📖 API Reference

### `val` — Validation

Static methods for validating common user inputs.

| Method | Description | Returns |
|---|---|---|
| `val.chk_p(password)` | Password strength check — min 6 chars, at least 1 uppercase, 1 lowercase, and 1 digit | `True` or `None` |
| `val.chk_e(email)` | Email format validation (RFC 2822 compliant) | `True` or `None` |
| `val.chk_ph(phone)` | International phone number validation | `True` or `None` |

**Example:**

```python
from Ol_Utills import val

val.chk_p("MyP@ss1234")   # True
val.chk_p("weak")          # None

val.chk_e("user@example.com")  # True
val.chk_e("not-an-email")      # None
```

---

### `req` — Authentication Decorators

Session-based decorators that protect your Flask routes.

#### `@req.login_required`

Restricts a route to logged-in users. Requires `session['logged'] == True`.

```python
from Ol_Utills import req

@app.route('/dashboard')
@req.login_required
def dashboard():
    return "Welcome to your dashboard"
```

#### `@req.admin_required`

Restricts a route to admin users. Requires `session['admin'] == True`.

```python
@app.route('/admin')
@req.admin_required
def admin_panel():
    return "Admin Panel"
```

> Both decorators return an empty JSON response via `jsonify()` if the session check fails.

---

### `res` — Response Helpers

Utility class for building standardized JSON API responses.

| Method | Description | Status |
|---|---|---|
| `res.success_response(data)` | Returns a success JSON response | 🔜 Coming soon |
| `res.error_response(message, code)` | Returns an error JSON response | 🔜 Coming soon |

---

### `database` — Database Connections

Quick-connect helpers for common databases.

#### `database.sqlite(database)`

Opens a connection to a **SQLite** database and returns a cursor.

```python
from Ol_Utills import database

db = database.sqlite("app.db")
db.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")
```

#### `database.postgresql(database, user, password, host)`

Opens a connection to a **PostgreSQL** database and returns a cursor.

```python
db = database.postgresql(
    database="mydb",
    user="admin",
    password="secret",
    host="localhost"
)
db.execute("SELECT * FROM users")
results = db.fetchall()
```

---

## 🧪 Running Tests

```bash
cd tests
python test.py
```

---

## 🤝 Contributing

Contributions are welcome! Here's how to get started:

1. **Fork** the repository
2. **Create** your feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](LICENSE) for more information.

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/OverLimit-OL">OverLimit (OL)</a>
</p>