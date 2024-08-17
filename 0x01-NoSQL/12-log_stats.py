#!/usr/bin/env python3
"""Provides some stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def getLogInfo(collection):
    """Prints stats about Nginx request logs.
    """
    coll = collection

    # Count the total number of documents
    total_logs = coll.count_documents({})
    print(f"{total_logs} logs")

    # Methods and their counts
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = coll.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    # Count documents with method GET and path /status
    status_checks = (
        coll.count_documents({"method": "GET", "path": "/status"})
    )
    print(f"{status_checks} status check")



if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    getLogInfo(client.logs.nginx)
