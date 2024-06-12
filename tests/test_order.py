#from datetime import date
from lib.Order import Order

"""
Order constructs......
"""
def test_order_constructs():
    # today = date.today()

    myOrder = Order(1, "Mr Smith", '2024-06-12')
    assert myOrder.item_id == 1
    assert myOrder.customer_name == "Mr Smith"
    assert myOrder.date_placed == '2024-06-12'


def test_orders_are_equal():
    # today = date.today()

    myOrder1 = Order(1, "Mr Jones", '2024-06-12')
    myOrder2 = Order(1, "Mr Jones", '2024-06-12')
    assert myOrder1 == myOrder2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.

