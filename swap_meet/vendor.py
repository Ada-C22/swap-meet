from .item import Item

class Vendor:
    def __init__(self, inventory=None):
        inventory = [] if not inventory else inventory
        self.inventory = inventory
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
            return item
        
    def get_by_id(self, id):
        for item in self.inventory:
            if item.id == id:
                return item

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            self.inventory += [their_item]
            other_vendor.inventory.remove(their_item)
            other_vendor.inventory += [my_item]
        return True




    
       

