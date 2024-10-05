import uuid
class Item:
    def __init__(self, id=None, condition= 0, age = 0):
        self.condition = condition
        self.age = age
        if id == None: 
            self.id = uuid.uuid4().int
        else:
            self.id = id
        


    def get_category(self):
        class_category = type(self).__name__
        return str(class_category)
    
    def __str__(self):
        category = self.get_category()
        str_id = str(self.id)
        return f"An object of type {category} with id {str_id}."
    
    def condition_description(self):

        if self.condition == 0: 
            return "This will leave a film on you"
        elif self.condition == 1: 
            return "Definitely wash hands after touching me"
        elif self.condition == 2: 
            return "Might still smell after washing"
        elif self.condition == 3: 
            return "How we all feel once we turn 35"
        elif self.condition == 4:
            return "Feeling young and confident yet still slightly jaded about the world"
        elif self.condition == 5: 
            return "Fresh as a daisy on a dewey spring morning"
        else : 
            return "unknown condition"
        
    def get_vintage_description(self):
        item_age = self.age 
        if item_age > 0 and item_age < 20: 
            return "Not Vintage"
        elif item_age > 20 and item_age < 30: 
            return "Almost Vintage"
        elif item_age > 30 and item_age < 100: 
            return "It's vintage"
        elif item_age >100:
            return "SUPER DUPER VINTAGE"
    
    def get_vintage_status(self):
        if self.age > 30:
            return True
        else: 
            return False
        
        