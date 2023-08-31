#Validate email and generate random password
import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern,email):
        print(f"The Email '{email}' is valid")
    else:
        print(f"The Email '{email}' is Not valid")

email_address = "testcom"
validate_email(email_address)


import string
import random
def generate_password(length = 8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    print("Generated Password: ", password)

generate_password(12)
