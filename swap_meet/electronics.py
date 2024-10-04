from .item import Item

class Electronics(Item):
    """
    A subclass of Item that represents an item of decor.

    Parameters:
    ----------
    id : int, optional
        Id of the item. Generated randomly by default
    condition : int, optional
        An integer value representing the condition of the item,
        where 1 is the worst and 5 is the best. Must be between 1 and 5.
        Defaults to 0, indicating that no condition is unknown.
    type: str
        A string value representing type of the electrinc item.
        Defaults to "Unknown"
    age : tuple, optional
        A tuple of 3 integer representing date in format (yyyy, mm, dd).
        Defaults to current day.

    """

    def __init__(self, id=None, condition=0, type="Unknown", age=None):
        super().__init__(id, condition,age)
        self.type = type

    def __str__(self):
        item_type_line, produce_date_line = super().generate_description()
        electronics_type_line = f"This is a {self.type} device."
        return "\n".join([item_type_line, electronics_type_line, produce_date_line])
