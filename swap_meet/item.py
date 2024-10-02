from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        descript_dict ={
            0: "Just burn it",
            1: "Maybe re-gift to someone you don't like.",
            2: "It's not good, but I've seen worse.",
            3: "It's not bad, but I've seen better.",
            4: "Basically perfect.",
            5: "Pristine!"
        }
        
        return descript_dict[self.condition]

