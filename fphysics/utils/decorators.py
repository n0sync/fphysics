import functools
import warnings
from ..constants import *

def units(input_units=None, output_units=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            wrapper.input_units = input_units
            wrapper.output_units = output_units
            return result
        return wrapper
    return decorator

def memoize(func):
    cache = {}
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        key = str(args) + str(sorted(kwargs.items()))
        if key not in cache:
            cache[key] = func(*args, **kwargs)
        return cache[key]
    return wrapper

def deprecated(reason="This function is deprecated"):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            warnings.warn(f"{func.__name__} is deprecated. {reason}", 
                         DeprecationWarning, stacklevel=2)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def vectorize(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if hasattr(args[0], '__iter__') and not isinstance(args[0], str):
            return [func(arg, *args[1:], **kwargs) for arg in args[0]]
        return func(*args, **kwargs)
    return wrapper

def validate_physics_input(min_value=None, max_value=None, positive=False, non_negative=False):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for arg in args:
                if isinstance(arg, (int, float)):
                    if positive and arg <= 0:
                        raise ValueError("Input must be positive")
                    if non_negative and arg < 0:
                        raise ValueError("Input must be non-negative")
                    if min_value is not None and arg < min_value:
                        raise ValueError(f"Input must be >= {min_value}")
                    if max_value is not None and arg > max_value:
                        raise ValueError(f"Input must be <= {max_value}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def error_handler(error_type=ValueError, default_return=None):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except error_type:
                return default_return
        return wrapper
    return decorator

def timer(func):
    import time
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} took {end - start:.4f} seconds")
        return result
    return wrapper

def logging_decorator(log_level='INFO'):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"[{log_level}] Calling {func.__name__} with args={args}, kwargs={kwargs}")
            result = func(*args, **kwargs)
            print(f"[{log_level}] {func.__name__} returned {result}")
            return result
        return wrapper
    return decorator

def retry(max_attempts=3, delay=1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            import time
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    time.sleep(delay)
            return None
        return wrapper
    return decorator

def convert_units(from_unit, to_unit, conversion_func):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(value, *args, **kwargs):
            converted_value = conversion_func(value, from_unit, to_unit)
            return func(converted_value, *args, **kwargs)
        return wrapper
    return decorator

def dimension_check(expected_dimensions):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i, (arg, expected_dim) in enumerate(zip(args, expected_dimensions)):
                if hasattr(arg, '__len__') and len(arg) != expected_dim:
                    raise ValueError(f"Argument {i} has wrong dimensions: expected {expected_dim}, got {len(arg)}")
            return func(*args, **kwargs)
        return wrapper
    return decorator

def ensure_numpy_array(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            import numpy as np
            new_args = []
            for arg in args:
                if isinstance(arg, (list, tuple)):
                    new_args.append(np.array(arg))
                else:
                    new_args.append(arg)
            return func(*new_args, **kwargs)
        except ImportError:
            return func(*args, **kwargs)
    return wrapper

def physics_constants(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

