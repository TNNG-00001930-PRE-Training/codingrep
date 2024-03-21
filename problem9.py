import re

def is_valid_password(password):

    pattern = re.compile(r"^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$")
    

    if pattern.match(password):
        return True
    else:
        return False


passwords = input("Enter passwords separated by commas: ")


password_list = passwords.split(',')

valid_passwords = []


for password in password_list:
    if is_valid_password(password):
        valid_passwords.append(password)


print(','.join(valid_passwords))