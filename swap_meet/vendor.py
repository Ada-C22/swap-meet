class Vendor:
    # wave 1
    def __init__(self, inventory=None):
        if inventory is None:
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
        else:
            return False
    # wave 2      
    def get_by_id(self, id):
        for item in self.inventory:
            if id == item.id:
                return item
        return None
    
    # wave 3
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:

            my_index = self.inventory.index(my_item)
            their_index = other_vendor.inventory.index(their_item)

            self.inventory[my_index] = their_item
            other_vendor.inventory[their_index] = my_item
            return True
        else:
            return False

    # wave 4
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False
        
        my_first_item = self.inventory[0]
        their_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_first_item, their_first_item)

        return True
    
    # wave 6
    def get_by_category(self, category):
        items_matching_category = []
        for item in self.inventory:
            if item.get_category() == category:
                items_matching_category.append(item)
        return items_matching_category
    
    def get_best_by_category(self, category):
        items_matching_category = self.get_by_category(category)
 
        if not items_matching_category:
            return None
        
        max_condition = -1
        max_item = None

        for item in items_matching_category:
            if item.condition > max_condition:
                max_condition = item.condition
                max_item = item
        return max_item
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        their_best_item_my_priority = other_vendor.get_best_by_category(my_priority)
        my_best_item_their_priority = self.get_best_by_category(their_priority)

        if not their_best_item_my_priority or not my_best_item_their_priority:
            return False
        
        self.swap_items(other_vendor, my_best_item_their_priority, their_best_item_my_priority)
        return True

        


            
