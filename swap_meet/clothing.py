from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, condition=0, fabric="Unknown"):
        super().__init__(id, condition)
        self.fabric = fabric

    def __str__(self):
        basic_info = super().__str__()
        detailed_info = f" It is made from {self.fabric} fabric."
        return basic_info + detailed_info