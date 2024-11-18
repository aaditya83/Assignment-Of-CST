import logging
from functools import wraps

# Configure the logger
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("function_calls.log"), logging.StreamHandler()],
)

logger = logging.getLogger(__name__)

# Create the decorator
def log_function_call(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Log the function call and its parameters
        logger.info(
            f"Function '{func.__name__}' called with args: {args}, kwargs: {kwargs}"
        )
        result = func(*args, **kwargs)
        # Log the result
        logger.info(f"Function '{func.__name__}' returned: {result}")
        return result
    return wrapper

# Example usage
@log_function_call
def add(a, b):
    return a + b

@log_function_call
def greet(name="World"):
    return f"Hello, {name}!"

# Test the logging system
if __name__ == "__main__":
    add(2, 3)
    greet(name="Alice")
    greet()
