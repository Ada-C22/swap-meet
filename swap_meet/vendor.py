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
        best_item_condition = 0
        best_item = None

        if not self.get_by_category(category):
            return None
        
        categories_list = self.get_by_category(category)
        for i in range(len(categories_list)):
            if categories_list[i].condition > best_item_condition:
                best_item_condition = categories_list[i].condition
                best_item =categories_list[i]
        return best_item
    
    def swap_best_by_category(self,other_vendor,my_priority,their_priority):
        
        vendor_best_item = self.get_best_by_category(their_priority)
        other_vendor_best_item = other_vendor.get_best_by_category(my_priority)

        if not vendor_best_item or not other_vendor_best_item:
            return False
        
        self.swap_items(other_vendor,vendor_best_item,other_vendor_best_item)
        return True
    
    def swap_by_newest(self, other_vendor):
        my_newest_item_age = float("inf")
        their_newest_item_age = float("inf")
        my_newest_item = None
        their_newest_item = None

        # Find the newest item in self's inventory
        for item in self.inventory:
            if item.age < my_newest_item_age:
                my_newest_item_age = item.age
                my_newest_item = item

        # Find the newest item in the other vendor's inventory
        for item in other_vendor.inventory:
            if item.age < their_newest_item_age:
                their_newest_item_age = item.age
                their_newest_item = item

        # Swap items only if both items are found
        if my_newest_item and their_newest_item:
            self.swap_items(other_vendor, my_newest_item, their_newest_item)
            return True

