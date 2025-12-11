# Test 1 — Linux Service Monitoring + REST API + Elasticsearch

This module includes:

- `monitor.py` → Checks status of `httpd`, `rabbitmq-server`, and `postgresql` on a Linux host and generates JSON files.
- `api.py` → Flask REST API that inserts status data into Elasticsearch and returns overall and per-service health.
- `requirements.txt` → Python dependencies.

---

# 🚀 How to Run

## 1️ Install dependencies

```bash
pip install -r requirements.txt
```

## 2️ Run monitoring script

```bash
python3 monitor.py
```

This generates:

```
httpd-status-20250115-132055.json
```

## 3️ Start REST API server

```bash
python3 api.py
```

### API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/add` | Insert service status JSON into Elasticsearch |
| GET | `/healthcheck` | Return overall UP/DOWN |
| GET | `/healthcheck/<service>` | Return specific service status |

---

