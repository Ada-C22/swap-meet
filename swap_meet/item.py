from uuid import uuid4
condition_rating = {0:'Bad', 1: 'Fine', 2: 'Not Bad', 3:'Good',4:'Very good',5:'New'}

class Item:
    def __init__(self, id=None, condition=0):
        if id is None:
            self.id = uuid4().int
        else:
            self.id = id
        self.condition= condition

    def get_category(self):
        return self.__class__.__name__


    def __str__(self):
        return f'An object of type {self.get_category()} with id {self.id}.'

    def condition_description(self):
        return condition_rating[self.condition]