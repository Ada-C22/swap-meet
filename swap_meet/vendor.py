
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
        