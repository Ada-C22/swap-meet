from uuid import uuid4


class Item:
    def __init__(self, id=None):
        if id is None:
            self.id = uuid4().int # ".int" converts UUID(128 bit number) to (single bit)16 bit number
        else:
            self.id = id # if id provided at function call it will assign that id

    def get_category (self):
        return "Item"
    

