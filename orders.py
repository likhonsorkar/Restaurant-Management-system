class Order:
    def __init__(self):
        self.items = {}
    def add_item(self,item,quentity):
        if item in self.items:
            self.items[item] += quentity
        else:
            self.items[item] = quentity
    def remove(self,item):
        if item in self.items:
            del self.items[item]
    @property
    def total_price(self):
        total = sum( item.price * quentity for item,quentity in self.items.items() )
        return total
    def clear(self):
        self.items = {}