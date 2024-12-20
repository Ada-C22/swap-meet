from swap_meet.item import Item

class Vendor:
    def __init__(self,inventory=None):
        self.inventory= inventory
        self.inventory= [] if self.inventory is None else self.inventory
        
    def add(self,item):
        self.inventory.append(item)
        return item
    
    def remove(self,item):
        if item not in self.inventory:
            return False
        else:
            self.inventory.remove(item)
        return item
    
    def get_by_id (self,id):
        for item in self.inventory:
            if item.id == id:
                return item
        return None
            
    def swap_items(self,other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False    
        self.inventory.remove(my_item)
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)     
        return True
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) > 0 and len(other_vendor.inventory) > 0:
            first_item = self.inventory[0]
            other_first_item = other_vendor.inventory[0]

            self.inventory.remove(first_item)
            other_vendor.inventory.append(first_item)
            other_vendor.inventory.remove(other_first_item)
            self.inventory.append(other_first_item)
            return True
        else:
            return False
        
    def get_by_category(self, category):
        category_list = []
        for items in self.inventory:
            if items.get_category() == category:
                category_list.append(items)
        return category_list
    
    def get_best_by_category(self, category):
        if not self.get_by_category(category):
            return None
        
        best_item = self.get_by_category(category)[0]
        for item in self.get_by_category(category):
                if item.condition  > best_item.condition:
                    best_item = item
        return best_item

    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other_vendor.get_best_by_category(my_priority)

        if my_best_item is None or their_best_item is None:
            return False
        
        result =  self.swap_items(other_vendor,my_best_item,their_best_item)
        return result








    

