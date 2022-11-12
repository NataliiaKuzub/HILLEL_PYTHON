from functools import wraps


def add_thousands_separator(fn):

    @wraps(fn)
    def wrapper(*args, **kwargs):
        return f'{fn(*args, **kwargs):,}'.replace(',', "'")

    return wrapper


@add_thousands_separator
def multiply(a, b):
    return a * b


print(multiply(9336, 1223))
