from .clothing import Clothing
from .decor import Decor
from .electronics import Electronics
from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if not inventory:
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

    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        other_vendor.inventory.remove(their_item)
        self.inventory.append(their_item)
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        return True
        
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) ==0:
            return False
        first_item = self.inventory[0]
        first_item_other = other_vendor.inventory[0]
        if  first_item  and first_item_other:
            self.inventory.remove(first_item)
            other_vendor.inventory.append(first_item)
            other_vendor.inventory.remove(first_item_other)
            self.inventory.append(first_item_other)
            return True
        return None
    
    
    def get_by_category(self, category="Unknown"):
        return[item for item in self.inventory if item.get_category() == category]
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        if not items_in_category:
            return None

        best_item = max(items_in_category, key= lambda item : item.condition)
        return best_item


    


