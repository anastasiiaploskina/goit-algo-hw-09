import time
from functools import wraps


def measure_time_ms(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)
        end = time.perf_counter()

        elapsed = (end - start) * 1000
        print(f"\nExecution time for '{func.__name__}': {elapsed:.4f} ms")
        return result
    return wrapper
