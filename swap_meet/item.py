import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.condition = condition
        
        if id == None:
            self.id = uuid.uuid4().int
        else:
            self.id = id

    def get_category(self):
        return "Item"

    def __str__(self):
        return f'An object of type Item with id {self.id}.'
    
    def condition_description (self):
        condition_phrases = ['it depends', 'needs to function', 'pairs well', 'just because', 'best product to exist', 'you need this']
        return condition_phrases[self.condition]

'''
another possible solution to condition_description using a dictionary.

def condition_description(self):
        descriptions={
            0: “Heavy used”,
            1: “Some notorious wear”,
            2: “Mild scratches or wear”,
            3: ” used”,
            4: “like new”,
            5: “new”
        }
        return descriptions.get(self.condition, “Unknown condition”)
'''