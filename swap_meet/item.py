from uuid import uuid4

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid4().int if id is None else id
        self.condition = condition

    def get_category(self):
        return type(self).__name__
    
    def __str__(self):
        return f"An object of type {self.get_category()} with id {self.id}."
    
    def condition_description(self):
        CONDITIONS  = [
        [5, "Mint condition!"],
        [4, "It's great!"],
        [3, "It's fine."],
        [2, "It's okay."],
        [1, "It's not great."],
        [0, "It's real bad."],
        ]

        if self.condition < 0 or self.condition > 5:
            return "I don't know what to do with this."

        for condition_threshold, description in CONDITIONS:
            if self.condition >= condition_threshold:
                return description

        return "I don't know what to do with this."
