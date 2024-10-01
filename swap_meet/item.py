import uuid
class Item:
    def __init__(self, id=uuid.uuid4().int):
        self.id = id
#      When we initialize an instance of `Item`, 
#      we can optionally pass in an integer with the keyword argument `id` to manually set the `Item`'s `id`
#      Each `Item` will have a function named `get_category`, 
#      which will return a string holding the name of the class


    def get_category(self):
        return str(type(self))
        #returns string holding name of class 
    
    def str(self):
        return f"An object of type {self.get_category} with id {str(self.id)}."
    