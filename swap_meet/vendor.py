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
        