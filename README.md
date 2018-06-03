# python-retry-decorator
Simple package that exposes a decorator function that retries operation after detecting a specified exception

## Usage
```Python
from retry import retry_operation

class RetriableException(Exception):
  pass

@retry_operation(RetriableException, retries = 4, delay_ms = 700, backoff_factor = 2)
def operation():
  # do stuff. Possibly raising RetriableException
  pass
```
