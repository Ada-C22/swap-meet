import uuid

class Item:
    def __init__(self,id=None, condition=0, age=0):
        self.id = id if id is not None else uuid.uuid4().int
        self.condition = condition
        self.age = age
    
    def get_category(self):
        return self.__class__.__name__
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        if self.condition == 0:
            return "Broken"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 2:
            return "Fair"
        elif self.condition == 3:
            return "Good"
        elif self.condition == 4:
            return "Like New"
        elif self.condition == 5:
            return "New, In Box"
    


