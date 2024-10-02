from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, id=None):
        super().__init__(id)
        self.category = "Electronics"
