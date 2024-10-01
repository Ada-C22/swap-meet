from uuid import uuid1
class Item:
    def __init__(self, id=None):
        self.id = int(uuid1()) if id is None else id

    def get_category(self):
        return self.__class__.__name__

    def __str__(self) -> str:
        return f"An object of type Item with id {self.id}."
