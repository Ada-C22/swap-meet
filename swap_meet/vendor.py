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
        return False
    
                    # Wave_2 

    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):

        if not my_item in self.inventory or not their_item in other_vendor.inventory:
            return False
        

        self.remove(my_item) 
        other_vendor.add(my_item)
        self.add(their_item) 
        other_vendor.remove(their_item)

        return True


