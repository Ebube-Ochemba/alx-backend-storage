# Redis basic

> This project was basics of Redis

## Summary

I learnt about how to use redis for basic operations as well ashow to use redis as a simple cache.

## Files

> Each file contains the solution to a task in the project.

- [x] [exercise.py #0](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py): Create a `Cache` class. In the `__init__` method, store an instance of the Redis client as a private variable named `_redis` (using `redis.Redis()`) and flush the instance using `flushdb`.
- Create a `store` method that takes a `data` argument and returns a string. The method should generate a random key (e.g. using `uuid`), store the input data in Redis using the random key and return the key.
- [x] [exercise.py #1](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py): Create a `get` method that take a `key` string argument and an optional `Callable` argument named `fn`. This callable will be used to convert the data back to the desired format.
- [x] [exercise.py #2](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py): Implement a system to count how many times methods of the `Cache` class are called.
- [4] [exercise.py #3](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py): Define a `call_history` decorator to store the history of inputs and outputs for a particular function.
- [x] [exercise.py #4](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/exercise.py): Implement a `replay` function to display the history of calls of a particular function.
- [ ] [web.py](https://github.com/Ebube-Ochemba/alx-backend-storage/blob/main/0x02-redis_basic/web.py): Implement a `get_page` function (prototype: `def get_page(url: str) -> str:`). The core of the function is very simple. It uses the `requests` module to obtain the HTML content of a particular URL and returns it.

> [main.py](./main.py): A main file for test cases. Provided by Alx.
