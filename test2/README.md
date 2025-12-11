# Test 2 — Ansible Automation

This section contains the Ansible inventory and playbook required to:

- Verify installation of assigned services  
- Check disk usage on all servers  
- Check the application status using the REST API from Test 1  

---

# 📁 Files Included

| File | Description |
|------|-------------|
| `inventory` | Hosts and their assigned services |
| `assignment.yml` | Main playbook controlled with `action` variable |

---

# 🚀 How to Run

Move into the folder:

```bash
cd test2
```

---

## 1️ Verify installation of services

```bash
ansible-playbook assignment.yml -i inventory -e action=verify_install
```

---

## 2️ Check disk usage (alert if >80%)

```bash
ansible-playbook assignment.yml -i inventory -e action=check-disk
```

---

## 3 Check application status (uses Test 1 REST API)

```bash
ansible-playbook assignment.yml -i inventory -e action=check-status
```

---

#  Requirements

- Ansible installed
- SSH access to all hosts
- API from Test 1 running and accessible

---

