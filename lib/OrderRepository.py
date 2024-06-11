from lib.Order import Order

class OrderRepository():
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('SELECT item_id, customer_name, date_order_placed from Orders')
        orders = []
        for row in rows:
            item = Order(row["item_id"], row["customer_name"], row["date_order_placed"])
            orders.append(item)
        return orders
  
    def create(self, new_order):
        self._connection.execute('INSERT INTO orders (customer_name, date_order_placed, item_id) VALUES (%s, %s , %s)', [new_order.customer_name, new_order.date_placed, new_order.item_id])
        # TODO: Handle exception for a foreign key violation e.g. an ItemID which doesn't exist.


