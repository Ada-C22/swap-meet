import uuid 

class Item:
    def __init__(self,id=None, condition=0):
        if id is None:
            self.id = uuid.uuid4().int
        else:
            self.id=id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__
    
    def condition_description(self):
        descriptions = {
            0: "You probably want a glove for this one...",
            1: "Heavily used",
            2: "Used but still functional",
            3: "In good condition",
            4: "Like new",
            5: "Mint condition"

    }
        return descriptions.get(self.condition, "Condition not recognized")
    #Wave 3
    def __str__(self):
        # Return the formatted string as per the requirement
        return f"An object of type Item with id {self.id}."
