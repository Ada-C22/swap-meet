from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        

    def add(self,item):
        inventory = self.inventory
        inventory.append(item)
        return item
    
    def remove(self,item):
        if item in self.inventory:
            inventory = self.inventory 
            inventory.remove(item)
            return item
        else: 
            return False
    
    def get_by_id(self,item_id):
        for item in self.inventory: 
            if item.id == item_id:
                return item
        return None

    def swap_items(self,other_vendor,my_item,their_item):
        other_vendor = Vendor(other_vendor)
        my_removed_item = self.remove(my_item)
        their_removed_item = other_vendor.remove(their_item)
        if my_removed_item is not False and their_removed_item is not False: 
            self.add(their_item)
            other_vendor.add(my_item)
            return True
        else: 
            if my_removed_item is not False:
                self.add(my_item)
            if their_removed_item is not False: 
                other_vendor.add(their_item)
            return False
