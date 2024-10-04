import uuid
class Item:
    def __init__(self, id=None, condition=0, age=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
        self.age = age

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return type(self).__name__
    
    def condition_description(self):
        x = self.condition
        if x < 0 or x > 5:
            return "Condition unknown. Is this from another dimension?"
        elif x < 1:
            return "Yikes! This thing's seen better centuries."
        elif x < 2:
            return "Handle with care... and maybe a hazmat suit."
        elif x < 3:
            return "It's got 'character' (that's code for 'issues')."
        elif x < 4:
            return "Not too shabby, just don't look too closely."
        elif x < 5:
            return "Almost new, if you squint hard enough."
        else:
            return "Mint condition! Did you steal this from a time machine?"
    
