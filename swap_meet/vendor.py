from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if inventory is None else inventory
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, int=None):
        for item in self.inventory:
            if item.id == int:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if self.get_by_id(my_item.id) not in self.inventory or other_vendor.get_by_id(their_item.id) not in other_vendor.inventory:
            return False
        
        self.remove(my_item)
        other_vendor.add(my_item)
        other_vendor.remove(their_item)
        self.add(their_item)
        return True

