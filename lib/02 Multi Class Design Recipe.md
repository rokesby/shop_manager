# {{PROBLEM}} Multi-Class Planned Design Recipe

## 1. Describe the Problem

Items
- List of items
    - Item : Name, price and stock level
- Add an item

Orders
- List of orders
    - Order : Customer name, Corresponding item, date_placed
- Add an order

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌─────────────────────┐                  ┌────────────────────┐
│                     │                  │                    │
│                     │                  │                    │
│    Order            │                  │   Items            │
│    - list all       ├─Made┼up┼of───────►    - list all      │
│    - add            │                  │    - add           │
│                     │                  │                    │
└─────────────────────┘                  └────────────────────┘
```

_Also design the interface of each class in more detail._

```python
class Orders:
    # User-facing properties:
    #   order_list: list of active orders

    def __init__(self):
        pass # No code here yet

    def add(self, order):
        # Parameters:
        #   order: an instance of Order
        # Side-effects:
        #   Adds the order to the order_list property of the self object
        pass # No code here yet

    def list_all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the Order objects
        pass # No code here yet

class Order:

    # User facing properties:

    
    def __init__(self):
        pass # No code here yet
            #   customer_name
        #   date_placed
        #   item_ordered
        #   number_ordered


class Items:
    # User-facing properties:
    #   None

    def __init__(self):
        # Parameters:
        # None
        # Side-effects:
        #   Seeds the initial items list based on the repository
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form Item list...... TBD
        pass # No code here yet

    def list_all(self):
        # Parameters:
        #   None
        # Returns:
        #   A list of the Item objects
        pass # No code here yet

    def add(self, Item):
        # Parameters:
        #   Item: an instance of Item
        # Side-effects:
        #   Adds the Item to the item_list property of the self object
        pass # No code here yet


class Item:

    # User-facing properties:
    #   item_id: int
    def __init__(self):
        pass # No code here yet
            #   name
            #   price
            #   stock_level


```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
When add we add two Items 
We see those Items reflected in the Items list
"""

inventory = Items()
item1 = Item('Leather chair', 150, 17)
item1 = Item('Desk lamp', 40, 19)
inventory.add(item1)
inventory.add(item2)
inventory.list_all() == [item1, item2]


"""
When add we add two Orders 
We see those order(s) reflected in the Orders list
"""
order_list = Orders()
order1 = Order(item_id, customer_name, quantity, date_placed)
order2 = Order(item_id, customer_name, quantity, date_placed)
order_list.add(Order1)
order_list.add(Order2)
order_list.list_all() == [Order1, Order2]


```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
