def validate_positive(value, name: str):
    if value <= 0:
        raise ValueError(f"{name} must be positive")
    return True

def validate_non_negative(value, name: str):
    if value < 0:
        raise ValueError(f"{name} must be non-negative")
    return True

def validate_range(value, min_value, max_value, name: str):
    if not (min_value <= value <= max_value):
        raise ValueError(f"{name} must be between {min_value} and {max_value}")
    return True

def validate_type(value, expected_type, name: str):
    if not isinstance(value, expected_type):
        raise TypeError(f"{name} must be of type {expected_type}")
    return True

def validate_dimensions(value, expected_shape, name: str):
    if len(value) != len(expected_shape) or any(v != e for v, e in zip(value, expected_shape)):
        raise ValueError(f"{name} must have shape {expected_shape}")
    return True

def validate_array(array, condition, name: str):
    for idx, elem in enumerate(array):
        if not condition(elem):
            raise ValueError(f"{name}[{idx}] is invalid")
    return True

def requires_positive(numbers):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name, value in zip(numbers, args):
                validate_positive(value, name)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def requires_non_negative(numbers):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name, value in zip(numbers, args):
                validate_non_negative(value, name)
            return func(*args, **kwargs)
        return wrapper
    return decorator

def requires_range(numbers, min_value, max_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for name, value in zip(numbers, args):
                validate_range(value, min_value, max_value, name)
            return func(*args, **kwargs)
        return wrapper
    return decorator
