# python program to Bank managment system
class BankAccount:
    def __init__(self,account_number,initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
    
    def deposit(self,amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} successfully") 
        else:
            print("Invalid amount, Deposit failed")

    def withdraw(self,amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdraw {amount} successfully.") 
        else:
            print("Insufficient funds.withdraw failed ")
        
    def check_balance(self):
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: {self.balance}")


accounts = {}

def create_account():
    account_number = input("Enter Account Number: ")
    if account_number in accounts:
        print("Account Number is already Exists.")
    else:
        initial_balance = float(input("Enter Initial balance: "))
        account = BankAccount(account_number, initial_balance)
        accounts[account_number] = account
        print("Account created successfully.")

def accessAccount():
    account_number = input("Enter Account Number: ")
    if account_number in accounts:
        account = accounts[account_number]
        print("\n\n----- Account Menu -----")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")

        while True:
            choice = input("Enter Your choice: ")
            if choice == "1":
                amount = float(input("Enter Ammount deposit: "))
                account.deposit(amount)
            elif choice == "2":
                amount = float(input("Enter Ammount to withdraw: "))
                account.withdraw(amount)
            elif choice == "3":
                account.check_balance()
            elif choice == "4":
                print("Exiting Account")
                break
            else:
                print("Invalid Choice")
    else:
        print("Account not found")

while True:
    print("\n--- Bank Account management system ---")
    print("1. Create Account")
    print("2. Access Account")
    print("3. Exit")

    choice = input("Enter your choice(1-3): ")
    if choice == "1":
        create_account()
    elif choice == "2":
        accessAccount()
    elif choice == "3":
        print("Exiting the Program")
        break
    else:
        print("Invalid choice,Please try again")
        


            


