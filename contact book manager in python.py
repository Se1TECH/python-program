# contact book manager in python
class Contact:
    def __init__(self, name,phone,email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def addContact(self,contact):
        self.contacts.append(contact)
        print("Contact Append Successfully.")
    
    def deleteContact( self,name):
        for contact in self.contacts:
            if contact.name.lower() ==  name.lower():
                self.contacts.remove(contact)
                print(f"Deleted Contact: {contact.name} ") 
                return
        print(f"Contact '{name}' not found")

    def searchContact(self,name):
        for contact in self.contacts:
            if contact.name.lower() == name.lower():
                print("\n\n----- Contact Details -----") 
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                return
        print(f"Contact '{name}' not found.")

    
    def displayContact(self):
        if not self.contacts:
            print("No Contacts in book.")
        else:
            print("Contact Book:")
            for contact in self.contacts:
                print(f"Name: {contact.name}")
                print(f"Phone: {contact.phone}")
                print(f"Email: {contact.email}")
                print("--------------------------------------\n")

# Create a contact book
contactBook = ContactBook()

# Menu loop
while True:
    print("\n----- Contact Book Manager -----")
    print("1. Add Contact")
    print("2. Delete Contact")
    print("3. Search Contact")
    print("4. Display Contact")
    print("5. Exit")

    choice = input("Enter Your Choice[1-5]: ")
    if choice == "1":
        name = input("Enter Contact Name: ")
        phone = input("Enter Phone Number: ")
        email = input("Enter Email: ")
        contact = Contact(name,phone,email)
        contactBook.addContact(contact)
    
    elif choice == "2":
        name = input("Enter Contact name to delete: ")
        contactBook.deleteContact(name)
    
    elif choice == "3":
        name = input("Enter Contact name to Search: ")
        contactBook.searchContact(name)
    
    elif choice == "4":
        contactBook.displayContact()

    elif choice == "5":
        print("You are Exiting from the contact manager.")
        break
    
    else:
        print("Invalid Choice. Please Try Again.")
    
    





