#!/usr/bin/env python3
"""Inserts a new document in a MongoDB collection based on kwargs."""


def insert_school(mongo_collection, **kwargs):
    """
    return: the new _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
