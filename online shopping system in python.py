# online shopping system in python
class Product:
    def __init__(self,id1,name,price):
        self.id1 = id1
        self.name = name
        self.price = price
    
class ShoppingCart:
    def __init__(self):
        self.items = []
    
    def add_item(self,product,quantity):
        self.items.append((product,quantity))
        print("Item Added to the Shopping Cart.")
    
    def view_cart(self):
        if not self.items:
            print("Your Shopping Cart is Empty.")
        else:
            print("\n--- Shopping Cart ---")
            total_price = 0
            for product,quantity in self.items:
                item_price = product.price * quantity
                total_price += item_price
                print(f"{product.name} - Quantity : {quantity} - Price : {item_price} ")
            print("Total Price : ", total_price )
    
    def place_order(self):
        if not self.items:
            print("Your Shopping Cart is Empty. No order placed.")
        else:
            print("Order Placed Successfully. ")

#create some product
product1 = Product(1,"Phone",1000)
product2 = Product(2,"Laptop",2000)
product3 = Product(3,"HeadPhones",1500)

#Create Shopping Cart
cart = ShoppingCart() 

#menu Loop

while True:
    print("\n----- Online Shopping System -----")
    print("1. View Products")
    print("2. Add Items to Carts ")
    print("3. View Cart")
    print("4. Place Order")
    print("5. Exit")

    choice = input("Enter Your Choice[1-5]: ")

    if choice == "1":
        print("\nProducts: ") 
        print(f"{product1.id1}. {product1.name} - ${product1.price}")
        print(f"{product2.id1}. {product2.name} - ${product2.price}")
        print(f"{product3.id1}. {product3.name} - ${product3.price}")
    
    elif choice == "2":
        product_id = int(input("Enter Product ID: "))
        quantity = int(input("Enter Product Quantity: "))
        if product_id == 1:
            cart.add_item(product1,quantity)
        elif product_id == 2:
            cart.add_item(product2,quantity)
        elif product_id == 3:
            cart.add_item(product3,quantity)
        else:
            print("Invalid Product ID.")
        
    elif choice == "3":
        cart.view_cart()

    elif choice == "4":
        cart.place_order()
    
    elif choice == "5":
        print("Exiting the online shopping system.")
        break

    else:
        print("Invalid Choice. Please Try Again. ")
    

