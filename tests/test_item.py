from lib.Item import Item

# TODO: Writing these object classes takes forever....

"""
Order constructs......
"""
def test_item_constructs():

    myItem = Item("Football", 8.99, 101)
    assert myItem.name == "Football"
    assert myItem.unit_price == 8.99
    assert myItem.stock_quantity == 101


def test_orders_are_equal():
    
    myItem1 = Item("Swimming cap", 2.99, 400)
    myItem2 = Item("Swimming cap", 2.99, 400)
    assert myItem1 == myItem2
    # Try commenting out the `__eq__` method in lib/artist.py
    # And see what happens when you run this test again.

def test_item_constructs_with_id():

    myItem = Item("Football", 8.99, 101, 99)
    assert myItem.name == "Football"
    assert myItem.unit_price == 8.99
    assert myItem.stock_quantity == 101
    assert myItem.item_id == 99

