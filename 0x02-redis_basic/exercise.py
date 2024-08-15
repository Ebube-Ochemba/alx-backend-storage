#!/usr/bin/env python3
"""A Redis client Module"""
import redis
from uuid import uuid4
from functools import wraps
from typing import Any, Callable, Optional, Union


def count_calls(method: Callable) -> Callable:
    """Count the number of times a function is called"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wraps called method and increments its call count
        in redis before execution"""
        key = method.__qualname__
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """Stores the history of inputs and outputs"""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> str:
        """Wraps called method and stores its input and output"""
        # Create input and output list keys
        input_key = f"{method.__qualname__}:inputs"
        output_key = f"{method.__qualname__}:outputs"

        # Store input arguments
        self._redis.rpush(input_key, str(args))

        # Execute the wrapped function
        output = method(self, *args, **kwargs)

        # Store the output
        self._redis.rpush(output_key, str(output))

        return output
    return wrapper


def replay(method: Callable) -> None:
    """Displays the history of calls of a particular function"""
    # Get the method's qualified name
    qualified_name = method.__qualname__

    # Create Redis client
    redis_client = redis.Redis()

    # Get the call count
    call_count = redis_client.get(qualified_name).decode('utf-8')

    print(f"{qualified_name} was called {call_count} times:")

    # Get inputs and outputs
    inputs = redis_client.lrange(f"{qualified_name}:inputs", 0, -1)
    outputs = redis_client.lrange(f"{qualified_name}:outputs", 0, -1)

    # Zip inputs and outputs together and print
    for input_data, output_data in zip(inputs, outputs):
        input_str = input_data.decode('utf-8')
        output_str = output_data.decode('utf-8')
        print(f"{qualified_name}(*{input_str}) -> {output_str}")


class Cache:
    """A wrapper for Redis operations"""

    def __init__(self) -> None:
        """Initialize redis client"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Store data in redis"""
        key = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Any:
        """Retrieve data from Redis and optionally convert it"""
        value = self._redis.get(key)
        if value is None:
            return None
        if fn is None:
            return value

        if fn is int:
            return self.get_int(value)
        if fn is str:
            return self.get_str(value)
        if callable(fn):
            return fn(value)

    def get_str(self, data: bytes) -> str:
        """ Converts bytes to string"""
        return data.decode('utf-8')

    def get_int(self, data: bytes) -> int:
        """ Converts bytes to integers"""
        return int(data)
