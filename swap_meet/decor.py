from .item import Item

class Decor(Item):
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
    width : int, optional
        An integer value representing width of the item.
        Defaults to 0.
    length : int, optional
        An integer value representing length of the item.
        Defaults to 0.
    age : tuple, optional
        A tuple of 3 integer representing date in format (yyyy, mm, dd).
        Defaults to current day.

    """
    def __init__(self,id=None, condition=0, width=0, length=0, age=None):
        super().__init__(id, condition, age)
        self.width = width
        self.length = length

    def __str__(self):
        item_type_line, produce_date_line = super().generate_description()
        item_size_line = f"It takes up a {self.width} by {self.length} sized space. "
        return "\n".join([item_type_line, item_size_line, produce_date_line])


