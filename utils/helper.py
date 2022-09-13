from functools import wraps


def retry(max_retry=2):
    def decorate(func):
        @wraps(func)
        def max_try(*args, **kwargs):
            res = func(*args, **kwargs)
            temp = 0
            while res is False and max_retry >= temp:
                res = func(*args, **kwargs)
                temp = 1 + temp
            return func(*args, **kwargs)

        return max_try

    return decorate
