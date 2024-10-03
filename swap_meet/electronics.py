from .item import Item

class Electronics(Item):
    def __init__(self, id=None, condition=0,type="Unknown", age=None):
        super().__init__(id, condition,age)
        self.type = type

    def __str__(self):
        return  f"An object of type Electronics with id {self.id}. "\
                f"This is a {self.type} device."\
                f"It was produced on {self.age.strftime("%x")}."
