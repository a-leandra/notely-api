# 📝 Notely API

**Notely API** is a lightweight, asynchronous RESTful API for managing personal notes. Built with FastAPI and PostgreSQL.

---

## Tech Stack

- **Backend Framework**: FastAPI
- **Database**: PostgreSQL
- **Async Database Driver**: `asyncpg`
- **ORM**: SQLAlchemy (with asynchronous support)
- **Data Validation**: Pydantic
- **Environment Management**: `python-dotenv`

---

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/a-leandra/notely-api.git
   cd notely-api
   ```

2. **Create a Virtual Environment**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**

   Create a `.env` file in the root directory and add your database credentials:

   ```env
   DATABASE_URL=postgresql+asyncpg://user:password@localhost/database-name
   ```

5. **Run the Application**

   ```bash
   uvicorn main:app --reload
   ```

   The API will be accessible at `http://127.0.0.1:8000`.

---

## API Documentation

FastAPI provides automatic interactive API documentation:

- **Swagger UI**: [http://127.0.0.1:8000](http://127.0.0.1:8000)
- **ReDoc**: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)
