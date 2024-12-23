from os import *
system("clear")

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} so'm"
    

class Dish:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.name} - {self.price} so'm"


class Menu:
    def __init__(self):
        self.dishes = []

    def add_dish(self, dish):
        self.dishes.append(dish)

    def show_menu(self):
        print("\n--- Menu ---")
        for i, dish in enumerate(self.dishes, 1):
            print(f"{i}. {dish}")


class Order:
    order_counter = 1

    def __init__(self, selected_dishes):
        self.order_id = Order.order_counter
        Order.order_counter += 1
        self.selected_dishes = selected_dishes
        self.total_price = sum(dish.price for dish in selected_dishes)

    def __str__(self):
        dish_list = "\n".join([str(dish) for dish in self.selected_dishes])
        return f"Order ID: {self.order_id}\nDishes:\n{dish_list}\nTotal Price: {self.total_price} so'm"


class Customer:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone


class DeliveryPerson:
    def __init__(self, name, vehicle_number):
        self.name = name
        self.vehicle_number = vehicle_number


class DeliverySystem:
    def __init__(self):
        self.menu = Menu()
        self.orders = []
        self.delivery_person = None

    def setup_menu(self):
        self.menu.add_dish(Dish("Osh", 20000))
        self.menu.add_dish(Dish("Lag'mon", 18000))
        self.menu.add_dish(Dish("Shashlik", 15000))
        self.menu.add_dish(Dish("Somsa", 8000))
        self.menu.add_dish(Dish("Choy", 2000))

    def take_order(self, customer):
        self.menu.show_menu()
        selected_dishes = []
        while True:
            choice = input("Ovqat tanlang (yoki '0' tugmasini bosing): ")
            if choice == '0':
                break
            try:
                dish = self.menu.dishes[int(choice) - 1]
                selected_dishes.append(dish)
            except (IndexError, ValueError):
                print("Noto'g'ri tanlov. Iltimos, qayta urinib ko'ring.")
        if selected_dishes:
            order = Order(selected_dishes)
            self.orders.append(order)
            print("\nBuyurtma qabul qilindi:")
            print(order)
        else:
            print("Buyurtma qilinmadi.")

    def assign_delivery_person(self, name, vehicle_number):
        self.delivery_person = DeliveryPerson(name, vehicle_number)

    def deliver_orders(self):
        if not self.orders:
            print("Hozircha buyurtmalar yo'q.")
            return
        if not self.delivery_person:
            print("Yetkazib beruvchi tayinlanmagan.")
            return
        print("\n--- Buyurtmalar yetkazilmoqda ---")
        for order in self.orders:
            print(f"Buyurtma ID {order.order_id} yetkazildi. Yetkazib beruvchi: {self.delivery_person.name} ({self.delivery_person.vehicle_number})")
        self.orders.clear()


system = DeliverySystem()
system.setup_menu()

customer = Customer("Ali", "+998901234567")
system.take_order(customer)

system.assign_delivery_person("Vali", "01A123AA")
system.deliver_orders()
