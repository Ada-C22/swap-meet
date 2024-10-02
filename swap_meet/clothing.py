# from swap_meet.item import Item
from uuid import uuid4
condition_rating = {0:'Bad', 1: 'Fine', 2: 'Not Bad', 3:'Good',4:'Very good',5:'New'}

class Clothing:
    def __init__(self,id=None, fabric="Unknown", condition=0):

        if id is None:
            self.id = uuid4().int
        else:
            self.id = id

        self.fabric = fabric if fabric else "Unknown"
        self.condition = condition

    def get_category(self):
        return f'Clothing'

    def __str__(self):
        return f'An object of type Clothing with id {self.id}. It is made from {self.fabric} fabric.'

    def condition_description(self):
        return condition_rating[self.condition]
