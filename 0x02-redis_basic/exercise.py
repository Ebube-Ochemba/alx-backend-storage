#!/usr/bin/env python3
"""A Redic client Module"""
import redis
from uuid import uuid4
from typing import Union


class Cache:
    """A wrapper for Redis operations"""

    def __init__(self) -> None:
        """Initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[bytes, float, int, str]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        client = self._redis
        client.set(key, data)
        return key
