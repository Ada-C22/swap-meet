from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, id=None, width=None, length=None, condition=None, fabric="Unknown", age=None):
        super().__init__(id, condition, age)
        self.fabric = fabric

    def __str__(self):
        return f"An object of type {self.__class__.__name__} with id {self.id}. "\
        f"It is made from {self.fabric} fabric."
        