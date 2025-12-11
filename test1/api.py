from flask import Flask, request, jsonify
from elasticsearch import Elasticsearch

app = Flask(__name__)

# Connect to Elasticsearch
es = Elasticsearch("http://localhost:9200")


@app.route("/add", methods=["POST"])
def add_status():
    """Insert JSON payload into Elasticsearch"""
    data = request.json
    es.index(index="service-status", document=data)
    return jsonify({"message": "Inserted"}), 201


@app.route("/healthcheck", methods=["GET"])
def healthcheck():
    """Return overall UP/DOWN"""
    res = es.search(index="service-status", size=500)
    statuses = [doc["_source"]["service_status"] for doc in res["hits"]["hits"]]

    overall = "DOWN" if "DOWN" in statuses else "UP"
    return jsonify({"application_status": overall})


@app.route("/healthcheck/<service>", methods=["GET"])
def service_health(service):
    """Return status of a specific service"""
    query = {"query": {"match": {"service_name": service}}}
    res = es.search(index="service-status", query=query)

    if res["hits"]["hits"]:
        status = res["hits"]["hits"][0]["_source"]["service_status"]
    else:
        status = "UNKNOWN"

    return jsonify({"service": service, "status": status})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
