# password manager program in python

import hashlib

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self,account,password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        self.passwords[account] = hashed_password
        print("Password Added successfully") 
    
    def get_password(self,account):
        if account in self.passwords:
            hashed_password = self.passwords[account] 
            print("Password: ",hashed_password)
        else:
            print("Account not found.")
    
    def delete_password(self,account):
        if account in self.passwords:
            del self.passwords[account]
            print("Account deleted Successfully.")
        else:
            print("Account not found.")
    
    def display_accounts(self):
        if not self.passwords:
            print("No Accounts in the password manager.")
        else:
            print("----- Accounts -----")
            for account in self.passwords:
                print(account)
    
#create a password manager
password_manager = PasswordManager()

#Menu loop

while True:
    print("\n\n----- Password Manager -----")
    print("1. Add Password")
    print("2. Get Password")
    print("3. Delete Password")
    print("4. Display Accounts")
    print("5. Exit")

    choice = input("Enter Your Choice(1-5) : ")

    if choice == "1":
        account = input("Enter Account Name: ")
        password = input("Enter Password: ")
        password_manager.add_password(account,password)
    
    elif choice == "2":
        account = input("Enter Account Name: ")
        password_manager.get_password(account)
    
    elif choice == "3":
        account = input("Enter Account Name: ")
        password_manager.delete_password(account)
    
    elif choice == "4":
        password_manager.display_accounts()
    
    elif choice == "5":
        print("Exiting from the password manager.")
        break

    else:
        print("Invalid Choice, Please Try Again. ")

        
    
