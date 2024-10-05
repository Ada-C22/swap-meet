class Vendor:
    def __init__(self, inventory=None):
        self.inventory = inventory or []
    
    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item not in self.inventory:
            return False
        
        self.inventory.remove(item)
        return item
    
    def get_by_id(self, num=None):
        for item in self.inventory:
            if item.id == num:
                return item
        return None

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False

        other_vendor.add(my_item)
        self.add(their_item)
        other_vendor.remove(their_item)
        self.remove(my_item)
        
        return True
    
    def swap_first_item(self, other_vendor):
        if not self.inventory or not other_vendor.inventory:
            return False

        self.swap_items(other_vendor, self.inventory[0], other_vendor.inventory[0])

        return True

    def get_by_category(self, category):

        items = [item for item in self.inventory if item.get_category() == category]
        return items
    
    def get_best_by_category(self, category):

        items = self.get_by_category(category)

        if not items:
            return None
        
        best_item = None
        for item in items:
            if best_item is None or item.condition > best_item.condition:
                best_item = item
    
        return best_item
            
    def swap_best_by_category(self, other_vendor, my_priority, their_priority):

        best_from_other = other_vendor.get_best_by_category(my_priority)
        best_from_self = self.get_best_by_category(their_priority)
        
        return self.swap_items(other_vendor, best_from_self, best_from_other)
    
    def find_newest_item(self, items):
        if not items:
            return None
            
        newest_item = None
        for item in items:
            if newest_item is None or item.age < newest_item.age:
                newest_item = item

        return newest_item
    
    def swap_by_newest(self, other_vendor):
        my_new_item = self.find_newest_item(self.inventory)
        their_new_item = self.find_newest_item(other_vendor.inventory)

        if not my_new_item or not their_new_item:
            return False
        
        return self.swap_items(other_vendor, my_new_item, their_new_item)