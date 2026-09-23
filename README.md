# Alumni Web Programming

This is the Alumni Web Programming project for the Web Programming course.

## Tech Stack

- **Language:** Python 3.12
- **Framework:** Flask
- **Containerization:** Docker & Docker Compose

## Getting Started

### Run locally

```bash
pip install -r requirements.txt
python app.py
```

The app will be available at `http://localhost:5000`.

### Run with Docker Compose

```bash
docker compose up --build
```

The app will be available at `http://localhost:5000`.

## API Endpoints

| Method | Path                          | Description                          |
|--------|-------------------------------|---------------------------------------|
| GET    | `/`                           | Temporary main page                   |
| GET    | `/hello`                      | Returns `Hello, World!`               |
| GET    | `/hello/<name>`               | Returns `Hello, <name>!`              |
| GET    | `/sum/<number1>/<number2>`    | Returns the sum of two numbers        |
| GET    | `/about`                      | Temporary about page                  |
