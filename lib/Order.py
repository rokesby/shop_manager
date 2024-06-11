class Order():

    def __init__ (self, item_ordered, customer_name, date_placed):
        self.item_id = item_ordered
        self.customer_name = customer_name
        self.date_placed = date_placed

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Order (Customer name: {self.customer_name}, Item ID: {self.item_id}, Date ordered: {self.date_placed})"    