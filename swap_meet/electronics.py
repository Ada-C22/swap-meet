from uuid import uuid4
condition_rating = {0:'Bad', 1: 'Fine', 2: 'Not Bad', 3:'Good',4:'Very good',5:'New'}

class Electronics:
    def __init__(self,id=None,type="Unknown",condition=0):
        if id is None:
            self.id = uuid4().int
        else:
            self.id = id
        self.type = type
        self.condition = condition

    def get_category(self):
        return f'Electronics'

    def __str__(self):
        return f"An object of type Electronics with id {self.id}. This is a {self.type} device."

    def condition_description(self):
        return condition_rating[self.condition]
