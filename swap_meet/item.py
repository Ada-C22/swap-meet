from uuid import uuid4

class Item:
    def __init__(self, id=None):
        if id is None:
            self.id = uuid4().int
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
