#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def main():
    """Prints stats about Nginx request logs.
    """
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    nginx_col = db.nginx

    # Count the total number of documents
    total_logs = nginx_col.count_documents({})
    print(f"{total_logs} logs")

    # Methods and their counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = nginx_col.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with method GET and path /status
    status_checks = (
        nginx_col.count_documents({"method": "GET", "path": "/status"})
    )
    print(f"{status_checks} status check")


if __name__ == "__main__":
    main()
