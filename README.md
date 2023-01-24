# projects_base

## FastAPI - Vue.JS base functions for projects

### Requirements

- Python >= 3.10.0
- Node JS >= 18.0.0

### 1. Backend

> Execute from root project folder

```bash
python -m venv .env && source .env/bin/activate
pip install -U pip setuptools
pip install .
```

### 2. Frontend

> Execute from root project folder

```bash
cd frontend && npm install -g vue && npm install && npm run build
```

#### Compiles and hot-reloads for development

```bash
npm run serve
```

#### Compiles and minifies for production

```bash
npm run build
```

#### Lints and fixes files

```bash
npm run lint
```

### 3. Run App

> Execute from root project folder

```bash
uvicorn main:app
```

App working on `localhost:8000`, you can specify a port using `-- port 1234`
