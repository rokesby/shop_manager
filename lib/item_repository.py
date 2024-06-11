from lib.Item import Item

class ItemRepository():
    
    def __init__(self, connection):
        self._connection = connection

    def all(self):
        rows = self._connection.execute('select id, name, unit_price, stock_quantity from items;')
        items = []
        for row in rows:
            item = Item(row["name"], row["unit_price"], row["stock_quantity"], row["id"])
            items.append(item)
        return items
  
    def create(self, new_item):
        self._connection.execute('INSERT INTO items (name, unit_price, stock_quantity) VALUES (%s, %s , %s)', [new_item.name, new_item.unit_price, new_item.stock_quantity])

