
class Vendor:

    def __init__(self, inventory=None):
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory
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

        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.remove(my_item)
            other_vendor.remove(their_item)
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        else:
            return False
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self_first_item = self.inventory.pop(0)
        other_first_item = other_vendor.inventory.pop(0)

        self.inventory.append(other_first_item)
        other_vendor.inventory.append(self_first_item)

        return True

    def get_by_category(self, category):
        items_in_category = []

        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item)

        return items_in_category

    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)

        if not items_in_category:
            return None

        best_item = items_in_category[0]
        for item in items_in_category:
            if item.condition > best_item.condition:
                best_item = item

        return best_item
    
    def find_best_item_by_category(self, category):
        return self.get_best_by_category(category)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.find_best_item_by_category(their_priority)
        their_best_item = other_vendor.find_best_item_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        
        self.swap_items(other_vendor, my_best_item, their_best_item)
        return True
    
    
    def reorder_inventory(self, new_order):
        if len(new_order) != len(self.inventory):
            raise ValueError("New order has to be the same length as the inventory.")
        
        new_inventory = []
        for index in new_order:
            new_inventory.append(self.inventory[index])

        self.inventory = new_inventory

        return self.inventory