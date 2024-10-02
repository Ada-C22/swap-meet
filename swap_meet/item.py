from uuid import uuid4
# from swap_meet.item import Item


class Item:
    def __init__(self, id=None):
        if id is None:
            self.id = uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__


    def __str__(self):
        return f'An object of type Item with id {self.id}.'