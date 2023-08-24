# inventory management system in python

class Product:
    def __init__(self, id, name, price, quantity):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)
        print("Product added successfully.")

    def view_products(self):
        if not self.products:
            print("No products found.")
        else:
            print("Products:")
            for product in self.products:
                print(f"ID: {product.id}\nName: {product.name}\nPrice: ${product.price}\nQuantity: {product.quantity}\n")

    def update_product(self, product_id, new_quantity):
        for product in self.products:
            if product.id == product_id:
                product.quantity = new_quantity
                print("Product quantity updated successfully.")
                return
        print("Product not found.")


# Create an inventory
inventory = Inventory()

# Menu loop
while True:
    print("\n--- Inventory Management System ---")
    print("1. Add Product")
    print("2. View Products")
    print("3. Update Product Quantity")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "1":
        product_id = input("Enter product ID: ")
        name = input("Enter product name: ")
        price = float(input("Enter product price: "))
        quantity = int(input("Enter product quantity: "))
        product = Product(product_id, name, price, quantity)
        inventory.add_product(product)
    elif choice == "2":
        inventory.view_products()
    elif choice == "3":
        product_id = input("Enter product ID: ")
        new_quantity = int(input("Enter new product quantity: "))
        inventory.update_product(product_id, new_quantity)
    elif choice == "4":
        print("Exiting the inventory management system.")
        break
    else:
        print("Invalid choice. Please try again.")
