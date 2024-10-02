import uuid

class Item:
    def __init__(self, id=None, condition=0):
        self.id = uuid.uuid4().int if id is None else id
        self.condition = condition
    
    def get_category(self):
        return str(self.__class__.__name__)
    
    def __str__(self): 
        return "An object of type Item with id {}.".format(self.id)
    
    def condition_description(self):
        match self.condition:
            case 0: 
                return "heavily used"
            case 1:
                return "used"
            case 2:
                return "decent"
            case 3:
                return "acceptable"
            case 4:
                return "like new"
            case 5:
                return "new"