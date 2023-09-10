# Define a custom exception class
class MyCustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# Raise the custom exception with a message
try:
    # Some condition that triggers the exception
    if some_condition:
        raise MyCustomException("This is a custom exception message")
except MyCustomException as e:
    # Handle the exception here
    print(f"Custom exception caught: {e.message}")
