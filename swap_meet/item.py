from uuid import uuid1
class Item:
    def __init__(self, id=None, condition=0):
        self.id = int(uuid1()) if id is None else id
        self.condition = condition

    def get_category(self):
        return self.__class__.__name__

    def __str__(self) -> str:
        return f"An object of type Item with id {self.id}."

    def condition_description(self):
        if self.condition in range(0, 6):
            condition_descriptions = {
                1: "Acceptable",
                2: "Good",
                3: "Very Good",
                4: "Like New",
                5: "Brand New",
                0: "Unknown"
            }
            return condition_descriptions[self.condition]
