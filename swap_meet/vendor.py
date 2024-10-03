# from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item_to_remove):
        if item_to_remove in self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        return False

    def get_by_id(self, id_num):
        for item in self.inventory:
            if item.id == id_num:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory
                or their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]

        return self.swap_items(other_vendor, my_item, their_item)

    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]

    def get_best_by_category(self, category):

        items_in_category = self.get_by_category(category)

        max_condition = 0.0
        best_item = None

        if not self.inventory:
            return best_item

        for item in items_in_category:
            if item.condition > max_condition:
                max_condition = item.condition
                best_item = item
        return best_item


    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item_to_swap = self.get_best_by_category(their_priority)
        their_item_to_swap = other_vendor.get_best_by_category(my_priority)

        if (my_item_to_swap is None or their_item_to_swap is None):
            return False

        are_items_swapped = self.swap_items(
            other_vendor, my_item_to_swap, their_item_to_swap)

        return are_items_swapped