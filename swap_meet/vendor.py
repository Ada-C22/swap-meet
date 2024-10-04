class Vendor:
    """
    A class to represent a vendor, managing the inventory and providing
    methods for adding, removing, and swapping items between vendors.
    """

    def __init__(self, inventory=None):
        """
        Initializes a Vendor instance with an optional inventory list.
        If no inventory is provided, an empty list is initialized.
        """
        self.inventory = inventory or []

    def add(self, new_item_added):
        """
        Adds the item to the `inventory`
        and returns item
        """
        self.inventory.append(new_item_added)
        return new_item_added

    def remove(self, item_to_remove):
        """
        Removes the specified item from the `inventory` if it exists and returns item
        """
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove

    def get_by_id(self, item_id):
        """
        Check if unique item id matches an item id in inventory and return item
        """
        for item in self.inventory:
            if item.id == item_id:
                return item

    def swap_items(self, other_vendor, my_item, their_item):
        """
        Swaps the specified items between this vendor and another vendor,
        if both vendors have the specified items in their inventory.
        """
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.append(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        """
        Swaps the first item from this vendor's inventory with the first item
        from another vendor's inventory.
        """
        if len(self.inventory) and len(other_vendor.inventory):
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            return self.swap_items(other_vendor, my_first_item, their_first_item)

    def get_by_category(self, category):
        """
        Retrieves all items in the inventory that match the given category.
        """
        result = []
        for item in self.inventory:
            if item.get_category() == category.capitalize():
                result.append(item)
        return result

    def get_best_by_category(self, category):
        """
        Finds the item with the highest `condition`and matching `category`
        """
        items_in_category = self.get_by_category(category)
        if items_in_category:
            highest_condition = items_in_category[0]
            for item in items_in_category:
                if item.condition > highest_condition.condition:
                    highest_condition = item
            return highest_condition

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        """
        Swaps the best item in this vendor's inventory (matching the `their_priority` category)
        with the best item in the other vendor's inventory (matching the `my_priority` category).
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            return self.swap_items(other_vendor, my_best_item, their_best_item)

    def find_newest(self, vendor):
        """
        Finds newest item by most latest date(age) in each inventory
        """
        newest_item = vendor.inventory[0]
        for item in vendor.inventory:
            if item.age > newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor):
        """
        Swaps the newest item from this vendor's inventory with the newest item
        from another vendor's inventory.
        """
        if self.inventory and other_vendor.inventory:
            my_item = self.find_newest(self)
            their_item = self.find_newest(other_vendor)
            return self.swap_items(other_vendor, my_item, their_item)
