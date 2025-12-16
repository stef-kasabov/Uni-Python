#Ex. 3
'''
Да се сьстави програма на Python, която дефинира клас Travel с полета: ID, Destination. Flight, Price. 
Да се добави метод „Reduce", чрез който всички стойности от полето Price 
по-големи от 200 да бъдат заменени със стойност по-ниска с 10%. 
Да се добави и методът Print, чрез който да се отпечатят ID, Destination, Flight, Price.
'''

class Travel:
    def __init__(self, t_id, destination, flight, price):
        self.id = t_id
        self.destination = destination
        self.flight = flight
        self.price = price

    def reduce(self):
        # If price is greater than 200, reduce by 10%
        if self.price > 200:
            discount = self.price * 0.10
            self.price = self.price - discount

    def print_info(self):
        print(f"ID: {self.id}, Dest: {self.destination}, Flight: {self.flight}, Price: {self.price}")

trip_1 = Travel(101, "Amsterdamn", "RayanAir", 250)
trip_2 = Travel(102, "France", "Nuke", 4.99)
trip_3 = Travel(202, "NY", "America-Ya", 6969.69)

print("Before reduction:")
trip_1.print_info()
trip_2.print_info()
trip_3.print_info()

trip_1.reduce()
trip_2.reduce()
trip_3.reduce()

print("After reduction:")
trip_1.print_info()
trip_2.print_info()
trip_3.print_info()