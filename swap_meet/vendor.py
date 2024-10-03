class Vendor:

    def __init__(self, inventory=None):
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
        Removes the matching item from the
        `inventory`and returns item
        """
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove

    def get_by_id(self, item_id):
        """
        Check if item id matches an item id in
        inventory and return item
        """
        for item in self.inventory:
            if item.id == item_id:
                return item
        # result = next(filter(lambda item: item.id == item_id, self.inventory), None)
        # return result

    def swap_helper(self, other_vendor, my_item, their_item):
        """
        Helper function that removes `my_item` from this
        `Vendor`'s inventory, and adds it to the friend's inventory
        """
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

    def swap_items(self, other_vendor, my_item, their_item):
        """
        If this `Vendor`'s inventory contain `my_item`
        or friend's inventory contain `their_item`
        it swaps.
        """
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.swap_helper(other_vendor, my_item, their_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        """
        It removes the first item from its `inventory`,
        and from friend's `inventory` and swaps the two first items
        """
        if len(self.inventory) and len(other_vendor.inventory):
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_helper(other_vendor, my_first_item, their_first_item)
            return True
        return False
    
    def get_by_category(self, category):
        """
        returns a list of objects in the inventory
        with that category provided in argument
        """
        result = []
        for item in self.inventory:
            if item.get_category() == category.capitalize():
                result.append(item)
        return result
        # result = list(filter(lambda item: item.get_category() == category.capitalize(), self.inventory))
        # return result

    def get_best_by_category(self, category):
        """
        looks through the instance's `inventory`
        for the item with the highest `condition`
        and matching `category`
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
        item in my inventory that matches `their_priority` category is swapped
        with the best item in `other_vendor`'s inventory that matches `my_priority`
        """
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_helper(other_vendor, my_best_item, their_best_item)
            return True
        return False
    
    # helper function
    def find_newest(self, vendor):
        """
        Locates newest item by most latest date in each inventory
        """
        newest_item = vendor.inventory[0]
        for item in vendor.inventory:
            if item.age > newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor):
        """
        Swaps newest item between self.inventory and other inventory
        """
        if self.inventory and other_vendor.inventory:
            my_item = self.find_newest(self)
            their_item = self.find_newest(other_vendor)
            self.swap_helper(other_vendor, my_item, their_item)
            return True
        return False