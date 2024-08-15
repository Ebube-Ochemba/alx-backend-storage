#!/usr/bin/env python3
"""A wrapper for Redis operations"""
import redis
from uuid import uuid4
from typing import Union


class Cache:

    def __init__(self):
        """Initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key
