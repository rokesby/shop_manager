class Item():

    def __init__ (self, name, unit_price, stock_quantity, id=None):
        self.name = name
        self.unit_price = unit_price
        self.stock_quantity = stock_quantity
        self.item_id = id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"#{self.item_id} {self.name} - Unit price: {self.unit_price} - Quantity: {self.stock_quantity}"  
        # #1 Super Shark Vacuum Cleaner - Unit price: 99 - Quantity: 30