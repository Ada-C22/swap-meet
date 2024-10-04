from .item import Item

class Clothing(Item):
    """
    A subclass of Item that represents an item of clothing.

    Parameters:
    ----------
    id : int, optional
        Id of the item. Generated randomly by default
    fabric : str, optional
        Type of fabric the item is made of. Defaults to "Unknown"
    condition : int, optional
        An integer value representing the condition of the item, 
        where 1 is the worst and 5 is the best. Must be between 1 and 5. 
        Defaults to 0, indicating that no condition is unknown.
    age : tuple, optional
        A tuple of 3 integer representing date in format (yyyy, mm, dd).
        Defaults to current day.

    """

    def __init__(self, id=None, fabric="Unknown", condition=0, age=None):
        super().__init__(id, condition, age)
        self.fabric = fabric


    def __str__(self) -> str:
        item_type_line, produce_date_line = super().generate_description()
        item_fabric_line = f"It is made from {self.fabric} fabric."
        return "\n".join([item_type_line, item_fabric_line, produce_date_line])

