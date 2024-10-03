from .item import Item

class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown", condition=0, age=None):
        super().__init__(id, condition, age)
        self.fabric = fabric


    def __str__(self) -> str:
        str_to_print = f"An object of type Clothing with id {self.id}. " \
                        f"It is made from {self.fabric} fabric.\
                        It was prodused on {self.age.strftime("%x")}"
        return str_to_print
