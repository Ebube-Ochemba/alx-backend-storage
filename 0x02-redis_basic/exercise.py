#!/usr/bin/env python3
"""A Redis client Module"""
import redis
from uuid import uuid4
from typing import Any, Callable, Optional, Union


class Cache:
    """A wrapper for Redis operations"""

    def __init__(self) -> None:
        """Initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Retrieve data from Redis and optionally convert it"""
        client = self._redis
        value = client.get(key)
        if not value:
            return
        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)
        return value

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers"""
        return int(data)
