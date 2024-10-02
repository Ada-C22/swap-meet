from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None):
        super().__init__(id)
        self.category = "Clothing"