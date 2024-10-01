import uuid

class Item:
    # wave 2
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = int(uuid.uuid4())
        else:
            self.id = id
            
        self.condition = condition
        
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
    
    def condition_description(self):
        if self.condition == 5:
            return "Mint condition - it's been in a museum"
        elif self.condition == 4:
            return "Almost new - barely touched"
        elif self.condition == 3:
            return "Gentle used, with stories to tell"
        elif self.condition == 2:
            return "Moderated used, but still kickin'!"
        elif self.condition == 1:
            return "Heavily used - but full of character"
        else:
            return "This one's a true survivor!"
        
        
item_a = Item(id=12345)

print(item_a)
