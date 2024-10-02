from uuid import uuid1
class Item:
    def __init__(self, id=None, condition=0.0):
        self.id = int(uuid1()) if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self):
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        # Round to nearest whole number
        round_condition = round(self.condition)
        descriptions = {
            0: "It's basically a wreck. You might want to steer clear of this one.",
            1: "Heavily used. You probably want a glove for this one...",
            2: "Well-loved, but still hanging in there.",
            3: "In good condition! Ready for a new home.",
            4: "Like new! You can hardly tell it’s been used.",
            5: "Mint condition! An absolute treasure."
        }


        return descriptions.get(round_condition, "Condition unrecognized")
