from lib.database_connection import DatabaseConnection
from lib.OrderRepository import OrderRepository
from lib.Order import Order
from lib.item_repository import ItemRepository
from lib.item_repository import Item

class Application():
    def __init__(self):
        self._connection = DatabaseConnection()
        self._connection.connect()
        self._connection.seed("seeds/shop_manager.sql")


    def get_all_orders(self):
        # Retrieve all orders
        order_repository = OrderRepository(self._connection)
        orders = order_repository.all()

        # List them out
        for order in orders:
            print(order)


    def get_all_items(self):
        # Retrieve all items
        item_repository = ItemRepository(self._connection)
        item_list = item_repository.all()

        # List them out
        for item in item_list:
            print(item)

    def add_new_order(self, itemID, customerName):
        repository = OrderRepository(self._connection)
        new_order = Order(itemID, customerName, '2024-06-12')
        repository.create(new_order)

    def add_new_item(self, name, unit_price, stock_quantity):
        repository = ItemRepository(self._connection)
        new_item = Item(name, unit_price, stock_quantity)
        repository.create(new_item)

if __name__ == '__main__':

    app = Application()

    # Display welcome message
    print("Welcome to the Shop Manager! \n\n  What would you like to do?\n")

    next_instruction = ''
    while next_instruction !=7:
        next_instruction = input("\nPlease enter option: \n(1) List all orders \n(2) Add new order \n(3) List items \n(4) Add an item \n(7) Exit\n ")
        if next_instruction == '1':
            app.get_all_orders()
        elif next_instruction == '2':
            newItemID = input("Please enter the ItemID of the Item you wish to order: ")
            newCustomerName = input("Please enter the name of the customer: ")
            #newOrder = Order(newItemID, newCustomerName, '2024-06-12')
            
            app.add_new_order(newItemID, newCustomerName)
            # Orders = OrderRepository.create(newOrder)

            #1app.test_add_new_order()
        elif next_instruction == '3':
            app.get_all_items()
        elif next_instruction == '4':    
            newName = input("Please enter the name of the item to add to the catalogue: ")
            newUnitPrice = input("Please enter the price of the new item: ")
            newStock = input("Please enter the quantity of stock for this new item: ")

            app.add_new_item(newName, newUnitPrice, newStock)
        else:
            next_instruction = 7
        
        # TODO : Refactor with case statement

