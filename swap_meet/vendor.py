class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if not inventory else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        self.inventory.remove(item)
        return item

    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if (my_item not in self.inventory or 
            their_item not in other_vendor.inventory):
            return False

        self.remove(my_item)
        other_vendor.add(my_item)

        other_vendor.remove(their_item)
        self.add(their_item)
        return True

    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        return self.swap_items(other_vendor, self.inventory[0], 
                               other_vendor.inventory[0])

    def get_by_category(self, category):
        return [item for item in self.inventory 
                if item.get_category() == category]

    def get_best_by_category(self, category):
        highest_item = None
        for item in self.get_by_category(category):
            if not highest_item or item.condition > highest_item.condition:
                highest_item = item
        return highest_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other_vendor.get_best_by_category(my_priority)

        if not my_best or not their_best:
            return False

        return self.swap_items(other_vendor, my_best, their_best)

    # Optional enhancements to swap newest items, optionally by category
    def get_newest(self, category=None):
        newest_item = None
        items = self.inventory if not category else self.get_by_category(category)
        for item in items:
            if not newest_item or item.age < newest_item.age:
                newest_item = item
        return newest_item

    def swap_by_newest(self, other_vendor, my_priority=None, their_priority=None):
        my_newest = self.get_newest(their_priority)
        their_newest = other_vendor.get_newest(my_priority)

        if not my_newest or not their_newest:
            return False

        return self.swap_items(other_vendor, my_newest, their_newest)
    