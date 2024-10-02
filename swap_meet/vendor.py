# from item import Item
class Vendor:
    
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory 
    
    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        try:
            self.inventory.remove(item)
            return item
        except ValueError:
            return False
    
    
    def get_by_id(self, item_id):
        for item in self.inventory:
            if item.id == item_id:
                return item
        return None
    
    def get_by_category(self, category):
        items_in_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_in_category.append(item) 
        return items_in_category
    
    def get_best_by_category(self, category):
        items_in_category = self.get_by_category(category)
        best_condition = 0.0
        best_in_category = None
        for item in items_in_category:
            if item.condition > best_condition:
                best_condition = item.condition
                best_in_category = item
        return best_in_category
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        best_item_my_priority = other_vendor.get_best_by_category(my_priority)
        best_item_their_priority = self.get_best_by_category(their_priority)
        if best_item_my_priority and best_item_their_priority:
            self.remove(best_item_their_priority)
            other_vendor.add(best_item_their_priority)
            other_vendor.remove(best_item_my_priority)
            self.add(best_item_my_priority)
            return True
        else:
            return False


    def swap_items(self, other_vendor, my_item, thier_item):
        my_item_exists = self.get_by_id(my_item.id)
        thier_item_exists = other_vendor.get_by_id(thier_item.id)
        if my_item_exists and thier_item_exists:
            self.remove(my_item)
            other_vendor.add(my_item)
            other_vendor.remove(thier_item)
            self.add(thier_item)
            return True
        else:
            return False
        
    def swap_first_item(self, other_vendor):
        try:
            my_first_item = self.inventory[0]
            thier_first_item = other_vendor.inventory[0]
        except IndexError:
            return False 
        self.remove(my_first_item)
        other_vendor.add(my_first_item)
        other_vendor.remove(thier_first_item)
        self.add(thier_first_item)
        return True
        
