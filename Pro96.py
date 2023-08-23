def encrypt_file(file_name, key):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()

        encrypted_contents = ""

        for char in contents:
            if char.isalpha():
                encrypted_char = chr((ord(char.lower()) - ord('a') + key) % 26 + ord('a'))
                if char.isupper():
                    encrypted_char = encrypted_char.upper()
                encrypted_contents += encrypted_char
            else:
                encrypted_contents += char

        encrypted_file_name = f"encrypted_{file_name}"
        with open(encrypted_file_name, 'w') as encrypted_file:
            encrypted_file.write(encrypted_contents)

        print("File encrypted successfully.")
        print("Encrypted file name:", encrypted_file_name)

    except FileNotFoundError:
        print("File not found.")

def decrypt_file(file_name, key):
    try:
        with open(file_name, 'r') as file:
            contents = file.read()

        decrypted_contents = ""

        for char in contents:
            if char.isalpha():
                decrypted_char = chr((ord(char.lower()) - ord('a') - key) % 26 + ord('a'))
                if char.isupper():
                    decrypted_char = decrypted_char.upper()
                decrypted_contents += decrypted_char
            else:
                decrypted_contents += char

        decrypted_file_name = f"decrypted_{file_name}"
        with open(decrypted_file_name, 'w') as decrypted_file:
            decrypted_file.write(decrypted_contents)

        print("File decrypted successfully.")
        print("Decrypted file name:", decrypted_file_name)

    except FileNotFoundError:
        print("File not found.")

# Menu loop
while True:
    print("\n--- File Encryption/Decryption Tool ---")
    print("1. Encrypt File")
    print("2. Decrypt File")
    print("3. Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        file_name = input("Enter the name of the file to encrypt: ")
        key = int(input("Enter the encryption key (integer): "))
        encrypt_file(file_name, key)
    elif choice == "2":
        file_name = input("Enter the name of the file to decrypt: ")
        key = int(input("Enter the decryption key (integer): "))
        decrypt_file(file_name, key)
    elif choice == "3":
        print("Exiting the encryption/decryption tool.")
        break
    else:
        print("Invalid choice. Please try again.")
