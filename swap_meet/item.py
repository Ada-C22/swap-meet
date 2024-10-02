import uuid


class Item:
    
    def __init__(self, id=None, condition=0 ):
        if id is None:
            self.id = uuid.uuid4().int
        else: 
            self.id = id

        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    #Stringify an instance of Item using str()
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
      
        if self.condition == 5:
            return "Good condition bright and shine"
        elif self.condition == 4:
            return "Good condition bright"
        elif self.condition == 3:
            return "Good condition"
        elif self.condition == 2:
            return "Good"
        elif self.condition == 1:
            return "Still good"
        else:
            return "Not a good condition"

        


    

# item_a = Item(id=12345)
# print(str(item_a))
