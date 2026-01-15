#Зад. 2

class FoodDelivery():
    def __init__(self, order_number, destination, price, delivery_term, order_status):
        self.order_number = order_number
        self.destination = destination
        self.price = price
        self.delivery_term = delivery_term
        self.order_status = order_status

    def order_info(self):
        print("\nOrder №:", self.order_number, "|| Destination:", self.destination, "|| Price:", self.price, "|| Delivery Term:", self.delivery_term, "|| Status:", self.order_status)

    def change_term (self):
        new_term = input("Въведете ново време за доставка: ")
        self.delivery_term = new_term
        print("Времето за доставка е обновено.")
    
def status_info(order_list, num):
    for order in order_list:
        if order.order_number == num:
            print(f"Статусът на поръчка {num} е '{order.order_status}'")
        else:
            print("Няма такъв номер поръчка!")

def add_order(order_list, new_order):
    order_list.append(new_order)
    print(f"Поръчка {new_order.order_number} беше добавена успешно.")

###

order_list = []

# Let's add 2 orders for testing purposes (entered by keyboard)
print("--- Въвеждане на поръчки ---")
for i in range(2): ##
    print(f"\nВъвеждане на данни за поръчка {i+1}:")
    o_num = input("Номер на поръчка: ")
    dest = input("Място на получаване: ")
    price = float(input("Цена: "))
    term = input("Срок на доставка: ")
    status = input("Статус (доставена, забавена, отказана): ")

    current_order = FoodDelivery(o_num, dest, price, term, status)

    add_order(order_list, current_order)

print("\n--- Търсене на статус ---")
search_num = input("Въведете номер на поръчка за проверка на статуса: ")
status_info(order_list, search_num)

print("\n--- Промяна на срок ---")
if len(order_list) > 0:
    print("Промяна на срока на първата поръчка в списъка:")
    order_list[0].change_term()
    order_list[0].order_info()