from swap_meet.item import Item

class Decor(Item):
    def __init__(self, id=None, condition=0, width=0, length=0):
        super().__init__(id, condition)
        self.width = width
        self.length = length

    def __str__(self):
        basic_info = super().__str__()
        detailed_info = f" It takes up a {self.width} by {self.length} sized space."
        return basic_info + detailed_info