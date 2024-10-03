class Vendor:

    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, new_item_added):
        self.inventory.append(new_item_added)
        return new_item_added

    def remove(self, item_to_remove):
        if item_to_remove not in self.inventory:
            return False
        else:
            self.inventory.remove(item_to_remove)
            return item_to_remove

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item

    def swap_helper(self, other_vendor, my_item, their_item):
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.swap_helper(other_vendor, my_item, their_item)
            return True
        return False

    def swap_first_item(self, other_vendor):
        if len(self.inventory) and len(other_vendor.inventory):
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_helper(other_vendor, my_first_item, their_first_item)
            return True
        return False
    
    def get_by_category(self, category):
        result = []
        for item in self.inventory:
            if item.get_category() == category.capitalize():
                result.append(item)
        return result

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if items_in_category:
            highest_condition = items_in_category[0]
            for item in items_in_category:
                if item.condition > highest_condition.condition:
                    highest_condition = item
            return highest_condition

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_helper(other_vendor, my_best_item, their_best_item)
            return True
        return False
    
    # helper function
    def find_newest(self, vendor):
        newest_item = vendor.inventory[0]
        for item in vendor.inventory:
            if item.age > newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor):
        if self.inventory and other_vendor.inventory:
            my_item = self.find_newest(self)
            their_item = self.find_newest(other_vendor)
            self.swap_helper(other_vendor, my_item, their_item)
            return True
        return False