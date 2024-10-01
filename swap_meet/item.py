import uuid
class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition

    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."

    def get_category(self):
        return type(self).__name__
    
    def condition_description(self):
        match self.condition:
            case _ if 0 <= self.condition < 1:
                return "Yikes! This thing's seen better centuries."
            case _ if 1 <= self.condition < 2:
                return "Handle with care... and maybe a hazmat suit."
            case _ if 2 <= self.condition < 3:
                return "It's got 'character' (that's code for 'issues')."
            case _ if 3 <= self.condition < 4:
                return "Not too shabby, just don't look too closely."
            case _ if 4 <= self.condition < 5:
                return "Almost new, if you squint hard enough."
            case _ if self.condition == 5:
                return "Mint condition! Did you steal this from a time machine?"
            case _:
                return "Condition unknown. Is this from another dimension?"
    
