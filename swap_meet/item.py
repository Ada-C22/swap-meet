import uuid
class Item:
    def __init__(self, id=[]):
        self.id = id
        if self.id == []:
            self.id = uuid.uuid4().int
#      When we initialize an instance of `Item`, 
#      we can optionally pass in an integer with the keyword argument `id` to manually set the `Item`'s `id`
#      Each `Item` will have a function named `get_category`, 
#      which will return a string holding the name of the class

    def get_category(self):
        class_category = type(self).__name__
        print("class category here -----------", class_category)
        return str(class_category)
        #returns string holding name of class 
    
    def str(self):
        return f"An object of type {self.get_category} with id {str(self.id)}."
    