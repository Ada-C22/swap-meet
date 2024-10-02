import uuid

class Item:
    def __init__(self, id=None, condition=0):
        id = int(uuid.uuid4()) if not id else id
        self.id = id
        self.condition = condition

    def get_category(self):
        return "Item"
    
    def __str__(self):
        return f"An object of type Item with id {self.id}."
    
    def condition_description(self):
        conditional_phrases = ["yikes", "noth worth it", "it could work", "just a scratch",
                                "almost new", "as good as it gets"]
        return conditional_phrases[self.condition]
    
    
        
