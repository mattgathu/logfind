"""
Script    : utils
Date      : June, 2015
Author(s) : Matt Gathu <mattgathu@gmail.com>
Desc      : helper module

"""
# ============================================================================
# make necessary imports
# ============================================================================
import time
from functools import wraps

# ============================================================================
# Helper classes and functions
# ============================================================================

def auto_retry(tries=3, exc=Exception, delay=5):
    """retry decorator factory"""
    def decorator(func):
        """function decorator"""
        @wraps(func)
        def wrapper(*args, **kwargs):
            """func wrapper"""
            for _ in range(tries):
                try:
                    return func(*args, **kwargs)
                except exc:
                    time.sleep(delay)
                    continue
            raise exc
        return wrapper
    return decorator


# ============================================================================
# EOF
# ============================================================================
