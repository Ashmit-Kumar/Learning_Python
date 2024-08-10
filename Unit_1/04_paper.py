import re
def validate(password):
    if not re.search(r'[a-z]',password):
        return False
    if not re.search(r'[0-9]',password):
        return False
    if not re.search(r'[A-Z]',password):
        return False
    if not re.search(r'[$#@]',password):
        return False

    return True


input_passwords = "abc123, Passw0rd!, 12345, Valid$Pass1, Too$LongPassword123, Short1@"

password=input_passwords.split(', ')
x=[x for x in password if validate(password)]
x=','.join(x)
print(x)