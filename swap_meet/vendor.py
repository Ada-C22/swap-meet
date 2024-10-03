from swap_meet.item import Item


class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        first_item = self.remove(self.inventory[0])
        other_vendor.add(first_item)

        other_first_item = other_vendor.remove(other_vendor.inventory[0])
        self.add(other_first_item)

        return True

    def get_by_category(self, category):
        category_list = []

        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)
        
        return category_list
    
    def get_best_by_category(self, category):
            best_item = None
            highest_condition = 0

            for item in self.inventory:
                if item.get_category() == category and item.condition > highest_condition:
                    highest_condition = item.condition
                    best_item = item

            return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other_vendor, my_best_item, their_best_item)
            return True

        return False