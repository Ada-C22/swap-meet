class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        elif item in self.inventory:
            self.inventory.remove(item)
            return item
    
    def get_by_id(self, item_id):
        for item_obj in self.inventory:
            if item_obj.id == item_id:
                return item_obj
        return None
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory: 
            return False
        if their_item not in other_vendor.inventory:
            return False            
        other_vendor.inventory.append(my_item)
        self.inventory.append(their_item)
        other_vendor.inventory.remove(their_item)
        self.inventory.remove(my_item)

        return True
    
    def swap_first_item(self, other_vendor):
        if not other_vendor.inventory or not self.inventory: 
            return False
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]

        other_vendor.inventory.append(my_first_item)
        self.inventory.append(their_first_item)
        other_vendor.inventory.remove(their_first_item)
        self.inventory.remove(my_first_item)
        return True       

    def get_by_category(self, category_str): 
        same_category = []
        for item_obj in self.inventory:
            if item_obj.get_category() == category_str: 
                same_category.append(item_obj)
        return same_category
    
    def get_best_by_category(self, category_str):
        max_condition = 0
        highest_rated_category = None
        for item_obj in self.inventory:
            if item_obj.get_category() == category_str: 
                if item_obj.condition > max_condition:
                    max_condition = item_obj.condition
                    highest_rated_category = item_obj
        return highest_rated_category 
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        other_vendor_item = other_vendor.get_best_by_category(my_priority)
        my_vendor_item = self.get_best_by_category(their_priority)

        if not other_vendor_item  or not my_vendor_item: 
            return False
        
        other_vendor.inventory.append(my_vendor_item)
        self.inventory.append(other_vendor_item)
        other_vendor.inventory.remove(other_vendor_item)
        self.inventory.remove(my_vendor_item)

        return True 