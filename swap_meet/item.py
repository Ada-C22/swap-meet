import uuid

class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.condition = condition
        self.age = age
        
        self.id = uuid.uuid4().int if id is None else id

    def get_category(self):
        return type(self).__name__

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description (self):

        condition_phrase = {

            0: "it depends",
            1: "needs to function",
            2: "pairs well",
            3: "just because",
            4: "best product to exist",
            5: "you need this"
        }

        return condition_phrase.get(self.condition, "Unknown condition")
        