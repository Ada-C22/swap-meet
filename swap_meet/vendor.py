class Vendor:
    def __init__(self, inventory=None):
        self.inventory = [] if inventory is None else inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
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
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
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
        other_first_item = other_vendor.inventory[0]
        self.swap_items(other_vendor, my_first_item, other_first_item)
        return True

    def get_by_category(self, category):
        return [item for item in self.inventory if item.get_category() == category]
       
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if not category_items:
            return None
        
        best_condition_item = category_items[0]
        best_condition = category_items[0].condition

        for item in category_items:
            if item.condition > best_condition:
                best_condition = item.condition
                best_condition_item = item

        return best_condition_item
        # return max(category_items, key=lambda item : item.condition)
    
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):
        my_swap_item = self.get_best_by_category(their_priority)
        their_swap_item = other_vendor.get_best_by_category(my_priority)

        if not my_swap_item or not their_swap_item:
            return False
        return self.swap_items(other_vendor, my_swap_item, their_swap_item)
    
    def get_newest(self):
        return min(self.inventory, key=lambda item:item.age)
    
    def swap_by_newest(self, other_vendor):
        my_swap_item = self.get_newest()
        their_swap_item = other_vendor.get_newest()
        return self.swap_items(other_vendor, my_swap_item, their_swap_item)