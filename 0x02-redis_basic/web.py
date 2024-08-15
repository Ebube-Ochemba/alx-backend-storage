#!/usr/bin/env python3
"""A requests caching module"""
import redis
import requests
from functools import wraps
from typing import Callable

# Create a Redis client
client = redis.Redis()


def url_access_count(func: Callable) -> Callable:
    """Count the number of times a function is called"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wraps called method and increments its call count
        in redis before execution"""
        client.incr(f"count:{url}")
        return func(url)
    return wrapper


def cache_result(func: Callable) -> Callable:
    """Caches the result of a function"""
    @wraps(func)
    def wrapper(url: str) -> str:
        """Wraps called method and Caches the result"""
        # Check if result is cached
        cached_result = client.get(url)
        if cached_result:
            return cached_result.decode('utf-8')

        # If not cached, call the function
        response = func(url)

        # Cache the result
        client.setex(url, 10, response)
        return response
    return wrapper


@url_access_count
@cache_result
def get_page(url: str) -> str:
    """GETs the HTML content of a particular URL and returns it"""
    response = requests.get(url)
    return response.text
