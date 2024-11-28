try:
    # Attempting to divide by zero, which will cause an exception
    result = 10 / 0
except ZeroDivisionError as e:
    # Handle the exception
    print(f"Error: {e}")
else:
    # This block runs only if no exception occurs
    print("Division was successful")
finally:
    # This block runs no matter what
    print("This block will run regardless of exception")


class CustomError(Exception):
    pass

try:
    raise CustomError("This is a custom error!")
except CustomError as e:
    print(f"Caught an exception: {e}")
    
    
# Defining custom exceptions
class InvalidUsernameError(Exception):
    """Exception raised for invalid usernames."""
    pass

class WeakPasswordError(Exception):
    """Exception raised for weak passwords."""
    pass

# Function to register a new user
def register_user(username, password):
    # Check if username contains invalid characters
    if not username.isalnum():
        raise InvalidUsernameError("Username can only contain letters and numbers.")
    
    # Check if password is weak
    if len(password) < 6:
        raise WeakPasswordError("Password must be at least 6 characters long.")
    
    # If everything is fine, register the user (simulated here with a print statement)
    print(f"User '{username}' registered successfully!")

# Test the function with different scenarios
try:
    register_user("john@doe", "password123")  # Invalid username (contains '@')
except InvalidUsernameError as e:
    print(f"Error: {e}")
except WeakPasswordError as e:
    print(f"Error: {e}")

try:
    register_user("johndoe", "123")  # Weak password (less than 6 characters)
except InvalidUsernameError as e:
    print(f"Error: {e}")
except WeakPasswordError as e:
    print(f"Error: {e}")

try:
    register_user("johndoe", "password123")  # Valid username and password
except InvalidUsernameError as e:
    print(f"Error: {e}")
except WeakPasswordError as e:
    print(f"Error: {e}")

