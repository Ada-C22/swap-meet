from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self,item):
        self.inventory.append(item)
        return item
        
    def remove(self,item):
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
        
        if not my_item in self.inventory or their_item not in other_vendor.inventory:
            return False 
        
        self.inventory.remove(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        other_vendor.inventory.append(my_item)
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        self.inventory[0] = their_first_item
        other_vendor.inventory[0] = my_first_item

        return True
    
    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if item.get_category() == category:
                category_list.append(item)

        return category_list
    
    def get_best_by_category(self,category):
        best_item = 0

        if not self.get_by_category(category):
            return None
        
        for item in self.get_by_category(category):

            if item.condition > best_item:
                best_item = item.condition
                
        
        return item