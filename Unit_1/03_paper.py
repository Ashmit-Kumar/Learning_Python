# def Sort(s):
#     words=s.split(', ')
#     print(words)
#     words=sorted(words)
#     print(words)



# Sort("without, hello, bag, should, be")

import re

def is_valid_password(password):
    """
    Checks if the given password meets the specified criteria.
    """
    # Criteria 1: At least one lowercase letter
    if not re.search(r'[a-z]', password):
        return False
    
    # Criteria 2: At least one digit
    if not re.search(r'[0-9]', password):
        return False
    
    # Criteria 3: At least one uppercase letter
    if not re.search(r'[A-Z]', password):
        return False
    
    # Criteria 4: At least one special character from [$#@]
    if not re.search(r'[$#@]', password):
        return False
    
    # Criteria 5: Length between 6 and 12 characters
    if not (6 <= len(password) <= 12):
        return False
    
    return True

def validate_passwords(passwords):
    """
    Validates a sequence of comma-separated passwords and returns the valid ones.
    """
    password_list = passwords.split(', ')
    valid_passwords = [password for password in password_list if is_valid_password(password)]
    return ', '.join(valid_passwords)

# Example usage
if __name__ == "__main__":
    # Sample input
    input_passwords = "abc123, Passw0rd!, 12345, Valid$Pass1, Too$LongPassword123, Short1@"

    # Validate and print valid passwords
    print(validate_passwords(input_passwords))
