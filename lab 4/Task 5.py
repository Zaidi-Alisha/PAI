class Restaurant:
    def __init__(self):
        self.menu_items = {}
        self.booked_tables = []
        self.customer_orders = []

    def add_item_to_menu(self, item_name, price):
        self.menu_items[item_name] = price

    def book_table(self, table_number):
        self.booked_tables.append(table_number)

    def customer_order(self, order):
        self.customer_orders.append(order)

    def print_menu(self):
        print("Menu:")
        for item, price in self.menu_items.items():
            print(f"{item}: ${price}")

    def print_table_reservations(self):
        print("Tables that have been booked: ", self.booked_tables)

    def print_customer_orders(self):
        print("Orders:", self.customer_orders)

restaurant = Restaurant()
restaurant.add_item_to_menu("Lasagna", 12)
restaurant.add_item_to_menu("Burger", 15)
restaurant.book_table(3)
restaurant.customer_order("Burger")

restaurant.print_menu()
restaurant.print_table_reservations()
restaurant.print_customer_orders()

