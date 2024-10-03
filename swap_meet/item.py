import uuid
class Item:
    def __init__(self,id=None):
        if id == None: 
            self.id = uuid.uuid4().int
        else:
            self.id = id


    def get_category(self):
        class_category = type(self).__name__
        return str(class_category)
    
    def __str__(self):
        category = self.get_category()
        str_id= str(self.id)
        return f"An object of type {category} with id {str_id}."
    