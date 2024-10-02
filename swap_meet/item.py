import uuid


class Item:
    
    def __init__(self, id=None):
        if id is None:
            self.id = uuid.uuid4().int
        else: 
            self.id = id

    def get_category(self):
        return self.__class__.__name__
    
    #Stringify an instance of Item using str()
    def __str__(self):
        return f"An object of type Item with id {self.id}."

    

# item_a = Item(id=12345)
# print(str(item_a))