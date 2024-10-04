import uuid
from .condition_dict import condition_table
class Item:
    ''' 
    Represents an item with a unique ID. 
    When stringified, returns a description including its type of ID.
    '''
    
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id == None else id
       
        self.condition = condition
        print(self.condition)
        
    def __str__(self):
        ''' Returns a string representing of the item. '''
        
        return f"An object of type Item with id {self.id}."
    
    def get_category(self):
        ''' Returns the category of the item'''
        
        return "Item"
    
    def condition_description(self):
        '''
        Returns a description of the items condition based on its condition value.
        '''
       
        if self.condition in condition_table.keys():
            return condition_table[int(self.condition)]
        


        
        


    
    
