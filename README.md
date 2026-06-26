# 🗓️ Smart Planner Engine

A dynamic, intelligent task management and scheduling API built with Python and FastAPI. Unlike traditional rigid calendar engines, the **Smart Planner Engine** actively detects missed deadlines and applies an automated rescheduling algorithm to balance data layout anomalies. This repository serves as a backend portfolio showcase demonstrating high-performance async design, atomic transactional execution, database normalization, and structured multi-layered clean architecture.

## 🚀 Key Architectural Pillars

* **Modular Router-Service-Repository Pattern:** Strictly isolates HTTP transport handling (`api/`), business validation logic (`schemas/`), optimization engines (`services/`), and state/persistence layers (`models/`).
* **Automated Rescheduling Mechanics:** Features a declarative engine that handles temporal edge cases, updates structural task definitions, and logs granular audit trails seamlessly.
* **High Performance Engine:** Fully asynchronous routing pipeline leveraging FastAPI, Pydantic v2 data-serialization modeling, and SQLAlchemy 2.0 ORM query mapping.
* **Data Consistency Guarantee:** Wraps compound modification pipelines into atomic database transactions, preventing partial-write corruptions during high-throughput optimization sweeps.

---

## 📂 Project Architecture

```text
smart-planner-backend/
│
├── app/
│   ├── __init__.py
│   ├── main.py                  # API initialization, global configurations, and middleware
│   ├── config.py                # Strongly-typed environment schema (Pydantic BaseSettings)
│   ├── database.py              # Connection pooling and engine configurations
│   ├── models.py                # SQLAlchemy Declarative mapping layer 
│   │
│   ├── api/                     # HTTP Presentation Layer
│   │   ├── __init__.py
│   │   ├── deps.py              # Runtime dependency injectors (Context DB Session)
│   │   └── v1/
│   │       ├── endpoints/
│   │       │   ├── tasks.py     # Clean CRUD operations & scheduler optimization triggers
│   │       │   └── users.py     # Profile & target setting definitions
│   │       └── api.py           # Unified v1 Namespace Router Aggregator
│   │
│   ├── schemas/                 # Data Ingest Validation & Serialization Filters
│   │   ├── task.py              # Task input, patch validation, and payload formatting
│   │   └── user.py              # User structural rules
│   │
│   └── services/                # Core Business Logic Layer
│       └── planner.py           # Algorithmic scheduling matrix calculation engine
│
├── .env.example                 # Template for environmental keys
├── requirements.txt             # Manifest of application dependencies
└── README.md
```

---

## 📊 Database Entity Model

The relational layer is designed to track fluid data state shifts without losing historic audit capabilities:

```text
  +-------------------+              +-------------------------+
  |       tasks       |              |   reschedule_history    |
  +-------------------+              +-------------------------+
  | id (PK)           | 1      0..* | id (PK)                 |
  | title             |--------------| task_id (FK)            |
  | description       |              | original_start_time     |
  | start_time        |              | new_start_time          |
  | end_time          |              | rescheduled_at          |
  | deadline          |              | reason                  |
  | duration_minutes  |              +-------------------------+
  | priority [Enum]   |
  | status [Enum]     |
  +-------------------+

```

---

## 🛠️ Tech Stack & Dependencies

* **Language & Framework:** Python 3.10+, FastAPI
* **Web Server Interface:** Uvicorn (ASGI)
* **Data Validation:** Pydantic v2
* **Object-Relational Mapper:** SQLAlchemy 2.0
* **Database Engine:** PostgreSQL

---

## ⚡ Quick Start & Execution

### 1. Prerequisite Environments

Ensure Python 3.10+ and a clean PostgreSQL instance are running locally.

### 2. Clone and Setup Environment

```bash
git clone [https://github.com/your-username/smart-planner-backend.git](https://github.com/your-username/smart-planner-backend.git)
cd smart-planner-backend

# Initialize virtual environment
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

```

### 3. Install Core Dependencies

```bash
pip install -r requirements.txt

```

### 4. Configure Local Variables

Create a `.env` file in your root folder:

```env
DATABASE_URL=postgresql://postgres:password@localhost:5432/smart_planner

```

### 5. Launch the Server Grid

```bash
uvicorn app.main:app --reload

```

The server will bind onto `http://127.0.0.1:8000`.

---

## 🎛️ API Interface Endpoint Map

| Action | Endpoint | Payload / Schema | Context |
| --- | --- | --- | --- |
| **POST** | `/api/v1/tasks/` | `TaskCreate` | Generates new structural calendar nodes |
| **GET** | `/api/v1/tasks/` | *None* | Paginated array retrieval filter |
| **PATCH** | `/api/v1/tasks/{id}` | `TaskUpdate` | Modifies parameters (Optimistic UI Drop Target) |
| **DELETE** | `/api/v1/tasks/{id}` | *None* | Performs systematic record extraction |
| **POST** | `/api/v1/tasks/replan` | *None* | Triggers scheduling structural sweep |

### Interactive Documentation UI

FastAPI generates rich interface documentation profiles natively. Once the grid is up, visit:

* Interactive Swagger UI: `http://127.0.0.1:8000/docs`
* Alternative Redoc Layout: `http://127.0.0.1:8000/redoc`