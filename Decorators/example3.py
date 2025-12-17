# Implement a decorator that caches the result of a function, so that when it's called with the same arguments, it returns the cached result instead of recomputing it.

from typing import Any


import time


def cache(func):
    cache_dict = {}
    def wrapper(*args, **kwargs):
        key = (args, frozenset[tuple[str, Any]](kwargs.items()))
        if key in cache_dict:
            return cache_dict[args]
        else:
            cache_dict[args] = func(*args, **kwargs)
            return cache_dict[args]
    return wrapper

@cache
def long_running_function(a ,b):
    time.sleep(3)
    return a + b

print(long_running_function(1, 2))