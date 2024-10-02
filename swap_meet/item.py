import uuid

class Item:
    
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id == None else id
       
        self.condition = condition
        print(self.condition)
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def get_category(self):
        return "Item"
    
    def condition_description(self):
        condition_table = {
            5: "Brand New",
            4: "Used - Like New/ Open Box/ Without Tags",
            3: "Used - Good",
            2: "Used - Fair",
            1: "Used - Poor",
            0: "For Parts - Not Working"
        }

        if self.condition in condition_table.keys():
            return condition_table[int(self.condition)]
        


        
        


    
    
