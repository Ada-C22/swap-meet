# import uuid
import random

class Item:
    
    def __init__(self, id=None):
        
        if id is None:
            # Generate a random integer with 32 digits using exponent operator
            self.id = random.randint(10**31, (10**32)-1)
            # return true if id is int
        elif isinstance(id, int):
            # If id is an integer, use it as is
            self.id = id
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    # try dunder name class method
    def get_category(self):
        return "Item"
    
    
