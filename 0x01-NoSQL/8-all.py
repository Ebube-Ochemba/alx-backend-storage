#!/usr/bin/env python3
"""Lists all documents in a MongoDB collection.
"""


def list_all(mongo_collection):
    """ 
    return: list of all documents, or empty list if no documents
    """
    return list(mongo_collection.find())
