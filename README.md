# App Monitoring – Full QA Automation Assignment  
### Python | Flask | Elasticsearch | Ansible | CSV Processing

This repository contains a complete, 
It demonstrates experience in:

- Linux service monitoring  
- REST API development  
- Elasticsearch integration  
- Infrastructure automation using Ansible  
- Python scripting & data processing  
- Clean project structure and documentation  

---

# 📁 Repository Structure

```
rbcapp-monitoring-assignment/
│
├── test1/                # Python monitoring script + REST API
│   ├── monitor.py
│   ├── api.py
│   ├── requirements.txt
│   └── README.md
│
├── test2/                # Ansible automation
│   ├── inventory
│   ├── assignment.yml
│   └── README.md
│
├── test3/                # CSV data processing
│   ├── process_sales.py
│   └── README.md
│
└── README.md             # Main documentation (you are here)
```

---

# 🧪 Test 1 — Linux Service Monitoring + REST API

### ✔ `monitor.py`  
Python script checks status of:
- `httpd`
- `rabbitmq-server`
- `postgresql`

Outputs JSON files such as:

```
httpd-status-20250115-132055.json
```

---

### ✔ `api.py`  
A Flask-based REST API that:

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/add` | Inserts service status JSON into Elasticsearch |
| GET | `/healthcheck` | Returns overall application health |
| GET | `/healthcheck/<service>` | Returns individual service status |

Elasticsearch index used: **service-status**

---

# ⚙ Test 2 — Ansible Infrastructure Automation

###  Playbook supports three actions:

| Action | Description |
|--------|-------------|
| `verify_install` | Ensures expected service is installed on the host |
| `check-disk` | Flags disk usage > 80% |
| `check-status` | Returns application status using Test1 REST API |

Run examples:

```bash
ansible-playbook assignment.yml -i inventory -e action=verify_install
ansible-playbook assignment.yml -i inventory -e action=check-disk
ansible-playbook assignment.yml -i inventory -e action=check-status
```

---

# Test 3 — CSV Data Processing

### ✔ Script: `process_sales.py`  
Reads `sales-data.csv` and outputs a filtered CSV containing properties whose:

**price per square foot < average price per square foot**

Run:

```bash
python3 process_sales.py
```

Outputs:

```
filtered_sales.csv
```

---

# 🛠 Requirements

- Python 3  
- Flask  
- Pandas  
- Elasticsearch  
- Ansible  

Install requirements for Test 1:

```bash
pip install -r test1/requirements.txt
```

---

 Author  
**Manisha Tripathi**  
 Automation Engineer  

---
