#!/usr/bin/env python3
"""
Script that provides some stats about Nginx logs stored in MongoDB.
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    collection = client.logs.nginx

    total = collection.count_documents({})
    print("{} logs".format(total))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for m in methods:
        print("\tmethod {}: {}".format(m, collection.count_documents({"method": m})))

    status = collection.count_documents({"method": "GET", "path": "/status"})
    print("{} status check".format(status))

