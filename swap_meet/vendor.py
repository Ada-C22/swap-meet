
class Vendor:
    # wave 1
    def __init__(self, inventory=None):
        self.inventory = inventory if inventory is not None else []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        
        return False
    
    # wave 2 
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    # wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        # checks if both items are in their each other's inventories
        if my_item in self.inventory and their_item in other_vendor.inventory:
            # remove the items from their own inventories
            self.remove(my_item)
            other_vendor.remove(their_item)
            # add the items to opposite inventories (swap)
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        return False
        
    # wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        self_first_item = self.inventory[0]
        self.inventory = [other_vendor.inventory[0]] + self.inventory[1:]
        other_vendor.inventory = [self_first_item] + other_vendor.inventory[1:]
        return True
    
    # wave 6
    def get_by_category(self, category):
        return [item for item in self.inventory if item.category == category]

    def get_best_by_category(self, category):
        items = self.get_by_category(category)
        if not items:
            return None
        
        # assume the first item is the best one
        best_item = items[0]
        for item in items[1:]: 
            if item.condition > best_item.condition:
                best_item = item
        return best_item
        

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        
        return self.swap_items(other_vendor, my_best_item, their_best_item)