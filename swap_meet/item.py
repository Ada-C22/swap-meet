from uuid import uuid1
from datetime import datetime

class Item:
    def __init__(self, id=None, condition=0, age=None):
        self.id = int(uuid1()) if id is None else id
        self.condition = condition
        self.age = datetime.today().date() if age is None else datetime(*age).date()

    def get_category(self):
        return self.__class__.__name__

    def generate_description(self):
        item_type_line = f"An object of type {self.get_category()} with id {self.id}."
        produce_date_line = f"It was produced on {self.age.strftime("%x")}."
        return item_type_line, produce_date_line

    def __str__(self):
        return "\n".join(self.generate_description())

    def condition_description(self):
        descriptions = {
            0: "It's basically a wreck. You might want to steer clear of this one.",
            1: "Heavily used. You probably want a glove for this one...",
            2: "Well-loved, but still hanging in there.",
            3: "In good condition! Ready for a new home.",
            4: "Like new! You can hardly tell it’s been used.",
            5: "Mint condition! An absolute treasure."
        }
        return descriptions.get(self.condition, "Condition unrecognized")
