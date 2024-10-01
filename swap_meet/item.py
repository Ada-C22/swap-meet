import uuid

class Item:
    # wave 2
    def __init__(self, id=None):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id

    def get_category(self):
        return self.__class__.__name__
    
    # wave 3
    def __str__(self):
        '''
        `item_a = Item(id=12345)`, 
        the output of `str(item_a):
        should be `"An object of type Item with id 12345."`
        '''
        return f"An object of type {self.get_category()} with id {self.id}."
    
item_a = Item(id=12345)

print(item_a)
