from uuid import uuid4
condition_rating = {0:'Bad', 1: 'Fine', 2: 'Not Bad', 3:'Good',4:'Very good',5:'New'}

class Decor:

    def __init__(self, id= None, width=0, length=0,condition=0):
        if id is None:
            self.id = uuid4().int
        else:
            self.id = id

        self.width = width
        self.length = length
        self.condition = condition


    def get_category(self):
        return f'Decor'

    def __str__(self):
        return f"An object of type Decor with id {self.id}. It takes up a {self.width} by {self.length} sized space."

    def condition_description(self):
        return condition_rating[self.condition]