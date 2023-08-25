# python program to basic ticket booking system for a cinema.

class Cinema:
    def __init__(self):
        self.seats =  []
        for _ in range(10):
            row = ["X"] * 10
            self.seats.append(row)

    def display_seats(self):
        print("\n----- Cinema Layout -----")
        print(" 1 2 3 4 5 6 7 8 9 10")
        for row in range (len(self.seats)):
            print(row + 1, " ".join(self.seats[row]))
        print()
    
    def book_ticket(self,row,seat):
        if row < 1 or row > len(self.seats) or seat < 1 or seat > len(self.seats[0]):
            print("Invalid Seat Selection.")
        elif self.seats[row - 1][seat - 1] == "X":
            self.seats[row - 1][seat - 1] = "B"
            print("Ticket Booked Successfully.")
        else:
            print("Seat Already Booked.")
    
#create a cinema
cinema = Cinema()

#menuloop
while True:
    print("\n----- Cinema Ticket Booking System -----")
    print("1. Display Tickets")
    print("2. Book Tickets")
    print("3. Exit")

    choice = input("Enter Your Choice[1-3]: ")
    
    if choice == "1":
        cinema.display_seats()

    elif choice == "2":
        row = int(input("Enter The Row Number: "))        
        seat = int(input("Enter The Seat Number: "))
        cinema.book_ticket(row,seat)

    elif choice == "3":
        print("Exiting the ticket booking system.")
        break
    
    else:
        print("Invalid Choice, Please Try Again.")
