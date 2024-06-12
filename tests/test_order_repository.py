from lib.Order import Order
from lib.OrderRepository import OrderRepository


def test_get_all_orders(db_connection):
    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)
    orders = repository.all()

    # TODO: Change the date_order_placed into a DATE field (in SQL) and the unit test will break - need to recheck the python date type for this property.
    assert orders == [
        Order(1, 'Mr Smith','2024-06-11'),
        Order(2, 'Mr Canes','2024-06-11'),
        Order(3, 'Mr Jones','2024-06-11'),
        Order(4, 'Mr Green','2024-06-11'),
        Order(1, 'Mr Brown','2024-06-11')
    ]

def test_add_new_order(db_connection):

    db_connection.seed("seeds/shop_manager.sql")
    repository = OrderRepository(db_connection)

    new_order = Order(1, 'Mr Blobby', '2024-06-12')
    repository.create(new_order)
    # We can return the list and check for the existence of the new order.

    orders = repository.all()
    
    assert orders == [
        Order(1, 'Mr Smith','2024-06-11'),
        Order(2, 'Mr Canes','2024-06-11'),
        Order(3, 'Mr Jones','2024-06-11'),
        Order(4, 'Mr Green','2024-06-11'),
        Order(1, 'Mr Brown','2024-06-11'),
        Order(1, 'Mr Blobby','2024-06-12')
    ]

