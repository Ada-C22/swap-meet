from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=None):
        if inventory is not None:
            self.inventory = inventory
        else: 
            self.inventory = []

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
        if my_item is None or their_item is None:
            return False
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
        
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0: 
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            self.swap_items(other_vendor, my_first_item, their_first_item)
            return True
        else: 
            return False
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:  
            if item.get_category() == category: 
                items_in_category.append(item)
        return items_in_category

    def get_best_by_category(self, category):
        best_item = None
        items_in_category = self.get_by_category(category)
        for item in items_in_category:
            if best_item == None: 
                best_item = item
            elif best_item.condition < item.condition:
                best_item = item
        return best_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_item_swap = self.get_best_by_category(their_priority)
        their_item_swap = other_vendor.get_best_by_category(my_priority)
        return self.swap_items(other_vendor, my_item_swap, their_item_swap)
        

        

