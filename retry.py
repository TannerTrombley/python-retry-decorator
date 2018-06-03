from functools import wraps
from typing import Callable, Tuple
import time

def retry_operation(
        retriable: Tuple[Exception, ...],
        retries: int = 5,
        delay_ms: float = 500,
        backoff_factor: int = 2) -> Callable:
    '''
    Wraps the target fn with retry policy
    :param retriable: the tuple of exceptions that will count as retriable errors
    :param retries: the max number of retries to attempt
    :param delay_ms: the delay between each retry
    :param backoff_factor: the multiplicative increase in delay after each retry
    :return: the wrapped target function
    '''

    def wrapped(target_fn: Callable) -> Callable:
        @wraps(target_fn)
        def inner_wrapped(*args, **kwargs) -> Callable:
            # don't modify the root values as they can be re-used
            num_retries: int = retries
            delay: float = delay_ms
            current_attempt: int = 0
            last_exception: Exception = None
            while current_attempt <= num_retries:
                try:
                    return target_fn(*args, **kwargs)
                except retriable as e:
                    last_exception = e
                    time.sleep(delay/1000)
                    delay *= backoff_factor
                    current_attempt += 1
            # at this point there are no retries left.
            raise last_exception
        return inner_wrapped

    return wrapped
