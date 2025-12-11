import subprocess
import json
import socket
import datetime

# Services to monitor
services = ["httpd", "rabbitmq-server", "postgresql"]


def check_service(service_name):
    """Check Linux service state"""
    try:
        result = subprocess.run(
            ["systemctl", "is-active", service_name],
            capture_output=True,
            text=True
        )
        status = "UP" if result.stdout.strip() == "active" else "DOWN"
    except Exception:
        status = "UNKNOWN"

    return status


def main():
    hostname = socket.gethostname()

    for svc in services:
        status = check_service(svc)
        data = {
            "service_name": svc,
            "service_status": status,
            "host_name": hostname
        }

        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        filename = f"{svc}-status-{timestamp}.json"

        with open(filename, "w") as f:
            json.dump(data, f, indent=2)

        print(f"Generated: {filename}")


if __name__ == "__main__":
    main()

